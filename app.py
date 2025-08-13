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

    st.markdown("### 📚 Relevant Processes:")
    for i, doc in enumerate(result["source_documents"]):
        match = re.search(r"# Process\s+(\d+)", doc.page_content)
        if match:
            process_id = match.group(1)
            # Extract the first line as the title
            title_line = doc.page_content.strip().splitlines()[0]
            st.markdown(f"---\n#### 📄 {title_line}")
        else:
            st.markdown("---\n#### 📄 Unlabeled Process")