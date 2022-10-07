import streamlit as st

mytemp = 'current temperature  ' + str(65)
st.header(mytemp)
x = st.slider('Temperature',min_value = 60, max_value=80)
st.header(x)
print(x)
