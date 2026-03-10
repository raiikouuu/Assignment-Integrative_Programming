import streamlit as st

st.title("My First Streamlit App")

st.header("Welcome!")

st.write("This is a simple page created using Streamlit.")

name = st.text_input("Enter your name:")

if st.button("Submit"):
    st.success(f"Hello, {name}! Welcome to the app.")

age = st.slider("Select your age", 10, 50)

st.write("Your age is:", age)

if st.checkbox("Show message"):
    st.write("Streamlit makes Python apps easy to build!")

st.subheader("Sample Data")
st.table({
    "Name": ["John", "Anna", "Mike"],
    "Score": [90, 85, 88]
})
