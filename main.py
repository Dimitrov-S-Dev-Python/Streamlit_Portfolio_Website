import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Ardit Sulce")
    content = """
    Hi, This is Ardit! 
    A Python programmer, teacher, and founder of PythonHow.
    Graduated 2013 with Master of Science from University of Muenster Germany.
    With focus on using Python
    """
    st.info(content)
