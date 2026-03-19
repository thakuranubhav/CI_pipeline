import streamlit as st
from app import square, cube, square_root, fifth_power

st.title("Calculator")

n = st.number_input("Enter number", value=1)

st.write("Square:", square(n))
st.write("Cube:", cube(n))
st.write("Fifth Power:", fifth_power(n))
st.write("Square root:", square_root(n))