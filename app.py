import streamlit as st
import math

st.title("Building a calculator")

st.write("Enter a number to perform calculation")

n= st.number_input("Enter a number for calculation",value=1,step=1)

sq= math.pow(n,2)
cube= math.pow(n,3)

sqr=math.sqrt(n)
sqr =round(sqr,4)


st.write("Square of a number is ",sq)
st.write("Cube of a number is ",cube)
st.write("Square root of a number is ",sqr)
