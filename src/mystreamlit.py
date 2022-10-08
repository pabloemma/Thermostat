import streamlit as st
import random as ra
import time


mytemp = 'current temperature  ' + str(60)
st.header(mytemp)
x = st.slider('Temperature',min_value = 60, max_value=80)
newtemp = 'the new temperature is '+str(x)
st.header(newtemp)
print(x)
time.sleep(5)
