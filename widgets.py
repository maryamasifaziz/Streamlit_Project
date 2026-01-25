import streamlit as st
import pandas as pd

st.title('Data Science and AI Batch 05')

name = st.text_input('Enter your name:')
# age = st.number_input('Enter your age:', min_value=0, max_value=120, step=1)

age = st.slider('Select your age:', 0, 120, 25)

if name:
    st.write(f'Hello, {name}! You are {age} years old.')

options = ['Python', 'Java', 'C++', 'HTML', 'JavaScript']
choice = st.selectbox("Choose your favorite language", options)

if choice:
    st.write(f'You selected: {choice}')

data = {
    "Name": ["John", "Jane", "Alice"],
    "Age": [28, 34, 29],
    "Favorite Language": ["Python", "Java", "C++"],
    "City": ["New York", "San Francisco", "Los Angeles"]
}

df = pd.DataFrame(data)

df.to_csv('sampledata.csv', index=False)
st.write("Here is the sample data:")
st.write(df)

uploadedfile = st.file_uploader("Upload your CSV file", type=["csv"])

if uploadedfile is not None:
    df_uploaded = pd.read_csv(uploadedfile)
    st.write("Here is the uploaded data:")
    st.write(df_uploaded)
