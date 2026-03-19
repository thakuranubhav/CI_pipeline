import streamlit as st
import math


# Logic functions (testable)
def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def square_root(x):
    return round(math.sqrt(x), 4)

def fifth_power(x):
    return x ** 5


# Streamlit UI
st.title("Building a calculator")

st.write("Enter a number to perform calculation")

n = st.number_input("Enter a number for calculation", value=1, step=1)

#  Use functions (DO NOT overwrite names)
sq = square(n)
cb = cube(n)
fifth = fifth_power(n)
sqr = square_root(n)

st.write("Square:", sq)
st.write("Cube:", cb)
st.write("Fifth Power:", fifth)
st.write("Square root:", sqr)