import streamlit as st
import pandas as pd

# Page Title
st.title("My Streamlit Portal Application")

st.write("This application demonstrates multiple Streamlit components.")

# User Input Section
name = st.text_input("Enter your name")

age = st.slider("Select your age", min_value=0, max_value=120, value=20)

gender = st.radio("Select your gender", ["Male", "Female", "Other"])

languages = st.multiselect(
    "Select programming languages you know",
    ["Python", "Java", "C++", "HTML", "JavaScript"]
)

submit = st.button("Submit Details")

if submit:
    st.success("Details submitted successfully!")
    st.write("### User Information")
    st.write("Name:", name)
    st.write("Age:", age)
    st.write("Gender:", gender)
    st.write("Languages:", languages)

# Checkbox Section
show_sample_data = st.checkbox("Show sample dataset")

# Sample Dataset
data = {
    "Name": ["Ali", "Maryam", "Zara"],
    "Age": [28, 20, 30],
    "Favorite Language": ["Python", "Java", "C++"],
    "City": ["New York", "USA", "Pakistan"]
}

df = pd.DataFrame(data)

if show_sample_data:
    st.write("### Sample Data")
    st.dataframe(df)

# File Upload Section
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    uploaded_df = pd.read_csv(uploaded_file)
    st.write("### Uploaded CSV Data")
    st.dataframe(uploaded_df)

# Metrics Section
st.write("### App Statistics")
st.metric(label="Total Sample Records", value=len(df))

st.subheader("Components Used")

st.markdown("""
- **st.title()**
- **st.text_input()**
- **st.slider()**
- **st.radio()**
- **st.multiselect()**
- **st.button()**
- **st.checkbox()**
- **st.file_uploader()**
- **st.dataframe()**
- **st.metric()**
- **st.subheader()**
- **st.markdown()**
""")