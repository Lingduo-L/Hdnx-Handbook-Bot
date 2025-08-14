import streamlit as st
from rag_pipeline import rewrite_query, qa_chain
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

    # st.markdown("### 📚 Relevant Processes:")
    # for i, doc in enumerate(result["source_documents"]):
    #     lines = doc.page_content.strip().splitlines()
    #     if lines:
    #         title_line = lines[0]
    #         # Try to match process ID and full title from line
    #         match = re.search(r"# Process\s+(\d+)\s*–\s*(.+)", title_line)
    #         if match:
    #             process_id = match.group(1)
    #             clean_title = match.group(2).strip()
    #             st.markdown(f"<hr><p style='font-size: 14px;'>📄 Process {process_id} – {clean_title}</p>", unsafe_allow_html=True)
    #         else:
    #             # Fallback to plain title line
    #             st.markdown(f"<hr><p style='font-size: 14px;'>📄 {title_line}</p>", unsafe_allow_html=True)