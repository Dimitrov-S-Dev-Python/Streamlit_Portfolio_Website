import streamlit as st
import pandas
import requests

# Prepare API key and API url

api_key = "CcZrS9EatIXPSHyW9EtnySNGkHfxwtG3CCoIlRoi"
url = "https://api.nasa.gov/planetary/apod?"\
        f"api_key={api_key}"

# Get requested data as a dictionary
response1 = requests.get(url)
data = response1.json()

# Extract the image title, url, and explanation
image_url = data["url"]
title = data["title"]
explanation = data["explanation"][:84] + "..."

# Download the image
image_filepath = "img.png"
response2 = requests.get(image_url)
with open(image_filepath, "wb") as file:
    file.write(response2.content)

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image(image_filepath)


with col2:

    content = """
    Hi,\n
    This is Dimitrov-S-Dev!\n
    I mainly code in Python, but I am always learning.\n
    Graduated Python Software Engineering Program at:\n
    "SoftUni University Bulgaria".\n
    With knowledge focused on:\n
    Python, JS, CSS, HTML\n
    STREAMLIT, DJANGO, FLASK, FASTAPI\n
    MSSQL, Postgres, Sqlite, Mysql\n
    Docker, Cloud, Linux Shell\n
    ....
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have build in Python.Feel free to contact
me at Contact Me page form.
"""
st.info(content2)

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
