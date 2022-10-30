import streamlit as st

st.title("Titel")
nr = st.slider('Input a number?', 0, 100, 1)
st.write("The number ism ", nr, 'years old')