import os
import streamlit as st




st.set_page_config(page_title="NewsBlaster", page_icon="📰", layout="wide")
st.title("NewsBlaster 📰")



if os.path.exists("summaries") and len(os.listdir("summaries")) > 0:
    st.subheader("🗂️ Generated Article Summaries:")
    for file in os.listdir("summaries"):
        path = os.path.join("summaries", file)
        try:
            with open(path, "r", encoding='utf-8') as f:
                summary = f.read()
            with st.expander(file):
                st.write(summary)
        except Exception as e:
            st.warning(f"⚠️ Could not read {file}: {e}")
else:
    st.info("📭 No summaries found. Try running NewsBlaster.")
