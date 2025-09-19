import streamlit as st
st.title("I am Diamante")
name=st.text_input("what is your name?")
if name:
  st success(f"hi {name}")
