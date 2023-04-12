import streamlit as st
import pandas

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

content2 = """
Below you can find some of the apps I have build in Python.Feel free to contact me.
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write("[Source Code](https://pythonhow.com)")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write("[Source Code](https://pythonhow.com)")