import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Dimitrov-S-Dev")
    content = """
    Hi, This is Dimitrov-S!\n
    A Python programmer and developer.\n
    Graduated 2023 Python Software Engineering Program with SoftUni University Bulgaria.\n
    With focus on using:\n
    Python, MSSQL, Postgres, JS, CSS, HTML,STREAMLIT, DJANGO, FLASK, FASTAPI
    """
    st.info(content)

text = "Below you can find some of the apps I have build in Python.Feel free to contact me"
st.write(text)
