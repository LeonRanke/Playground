import streamlit as st

st.title("Playground")
age = st.slider('Input your age?', 0, 100, 1)
st.write("You are ", age, 'years old')