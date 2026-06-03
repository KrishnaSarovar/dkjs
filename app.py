import streamlit as st

st.set_page_config(page_title="File Downloader")

st.title("Download My Python File")

with open("code.py", "rb") as file:
    st.download_button(
        label="📥 Download code.py",
        data=file,
        file_name="Code.py",
        mime="text/x-python"
    )
