import streamlit as st

import pandas

st.set_page_config(layout="wide")

st.title("Frontizo Business Services")
content = """
We are a company that provide customer service solutions as a global outsourcing partner to one of India’s largest 
online marketplace websites. Services are provided in mediums like phone, email, 
and chat and in the English and Hindi languages.
"""
st.info(content)

st.header("Our Team")

col1, empty_col1, col2, empty_col2, col3 = st.columns([2, 0.5, 1.5, 0.5, 1.5])

df = pandas.read_csv("data-2.csv", sep=",")

with col1:
    for index, row in df[:4].iterrows():
        name = st.header(f'{row["first name"].capitalize()} {row["last name"].capitalize()}')
        st.write(row["role"])
        st.image("images-2/" + row["image"])
with col2:
    for index, row in df[4:8].iterrows():
        name = st.header(f'{row["first name"].capitalize()} {row["last name"].capitalize()}')
        st.write(row["role"])
        st.image("images-2/" + row["image"])
with col3:
    for index, row in df[8:].iterrows():
        name = st.header(f'{row["first name"].capitalize()} {row["last name"].capitalize()}')
        st.write(row["role"])
        st.image("images-2/" + row["image"])
        