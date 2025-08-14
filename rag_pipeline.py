import os
from pathlib import Path
import re

from langchain.chains import RetrievalQA, LLMChain
from langchain.prompts import PromptTemplate, ChatPromptTemplate

# from langchain.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI

# from langchain.embeddings import OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings

# from langchain.vectorstores import FAISS
from langchain_community.vectorstores import FAISS

from langchain.retrievers import EnsembleRetriever
from langchain_community.retrievers import BM25Retriever

from langchain.schema import Document

import spacy
import streamlit as st
import subprocess
import importlib.util

# ===== 检查 spaCy 模型是否存在，不存在就自动下载 ===== 
model_name = "en_core_web_sm"
if not importlib.util.find_spec(model_name):
    subprocess.run(["python", "-m", "spacy", "download", model_name])

nlp = spacy.load(model_name)

def spacy_tokenizer(text: str) -> list[str]:
    return [token.text for token in nlp(text) if not token.is_space]

# ===== 设置 OpenAI API Key =====
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# ===== 加载 spaCy 分词器（用于 BM25）=====
# nlp = spacy.load("en_core_web_sm")
# def spacy_tokenizer(text):
#     return [token.text for token in nlp(text)]

nlp = spacy.load("en_core_web_sm")
def spacy_tokenizer(text: str) -> list[str]:
    return [token.text for token in nlp(text) if not token.is_space]

# ===== 加载文档 =====
chunk_path = Path("data/handbook_chunks.txt")
with open(chunk_path, "r", encoding="utf-8") as f:
    content = f.read()

raw_chunks = content.split("\n\n")
docs = [Document(page_content=chunk) for chunk in raw_chunks if chunk.strip()]

bm25_retriever = BM25Retriever.from_documents(docs, tokenizer=spacy_tokenizer)

# ===== 初始化检索器 =====
bm25_retriever = BM25Retriever.from_documents(docs, tokenizer=spacy_tokenizer)
embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")
db = FAISS.load_local("faiss_index", embedding_model, allow_dangerous_deserialization=True)
faiss_retriever = db.as_retriever(search_kwargs={"k": 10})

retriever = EnsembleRetriever(
    retrievers=[bm25_retriever, faiss_retriever],
    weights=[0.5, 0.5]
)

# ===== 问题改写模块 =====
rewrite_llm = ChatOpenAI(temperature=0, model_name="gpt-4o", max_tokens=4000)
query_rewrite_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an assistant that reformulates user queries to improve document retrieval in a knowledge-based system. \
Your rewritten query should be specific, semantically rich, and suitable for searching in a vector database."),
    ("human", "Original query: {original_query}\n\nRewritten query:")
])
query_rewriter = query_rewrite_prompt | rewrite_llm

def rewrite_query(original_query: str) -> str:
    try:
        response = query_rewriter.invoke({"original_query": original_query})
        return response.content.strip() if response.content.strip() else original_query
    except:
        return original_query

# ===== 定义 RAG Prompt =====
custom_prompt = PromptTemplate.from_template("""
You are an assistant that answers questions strictly based on the internal documentation.

Your first task is to extract and display **all relevant Process IDs** found in the context.
You must list the Process IDs explicitly before giving any answer.

Example:
Relevant Process IDs: 291, 295

Then provide a clear, concise, **logical** answer in the form of a workflow:
- Start by identifying the **first step** a person should take.
- Clearly describe each subsequent step, referencing the relevant Process ID.
- Use transition words such as "First", "Next", "Then".
- Briefly explain what each process does and why it matters.

--- 

Question: {question}
Context:
{context}

Answer:
""")

# ===== 构建 RAG 问答链 =====
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True,
    chain_type="stuff",
    chain_type_kwargs={"prompt": custom_prompt},
    verbose=True,
)

# ===== 主程序入口 =====
if __name__ == "__main__":
    while True:
        user_question = input("\n🧠 Please Input your question:(Input 'exit' to exit): \n> ")
        if user_question.lower() in ["exit", "quit"]:
            break

        rewritten = rewrite_query(user_question)
        print(f"\n🔁 question after rewrting: {rewritten}")

        result = qa_chain.invoke({"query": rewritten})

        print("\n🤖 AI Bot Answer: ")
        print(result["result"])

        print("\n📚 Relevant Processes:")
        for doc in result["source_documents"]:
            lines = doc.page_content.strip().split("\n")
            title_line = next((line for line in lines if line.lower().startswith("process ")), None)
            if title_line:
                print(f"- {title_line.strip()}")
            else:
                # If no title line, show first line as fallback
                print(f"- {lines[0].strip()}")