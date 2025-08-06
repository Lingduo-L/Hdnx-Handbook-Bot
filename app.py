import streamlit as st
from main import rewrite_query, qa_chain
import re

st.set_page_config(page_title="Hdnx Handbook Bot", page_icon="🤖")

st.title("🤖 Hdnx Handbook Bot")
st.markdown("Ask me anything about the internal documentation.")

# 用户输入问题
user_input = st.text_input("🧠 Your Question:")

# 按钮触发
if st.button("🔍 Submit") and user_input:
    with st.spinner("Rewriting and retrieving..."):
        rewritten = rewrite_query(user_input)
        result = qa_chain.invoke({"query": rewritten})

    st.markdown(f"### 🔁 Rewritten Query:\n`{rewritten}`")
    st.markdown("### 🤖 Answer:")
    st.write(result["result"])

    st.markdown("### 📚 Relevant Process IDs:")
    for i, doc in enumerate(result["source_documents"]):
        headers = re.findall(r"^####.*", doc.page_content, flags=re.MULTILINE)
        ids = []
        for header in headers:
            ids += re.findall(r"\b\d+\b", header)
        if ids:
            unique_ids = sorted(set(ids), key=int)
            st.write(f"From Source #{i+1}: " + ", ".join(unique_ids))