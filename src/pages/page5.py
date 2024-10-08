import streamlit as st
import time

st.title("Page 5 - Advanced Features")

# Caching
st.subheader("Caching Example")


@st.cache_data
def expensive_computation(a, b):
    time.sleep(2)  # Simulate a long computation
    return a * b


a = st.number_input("Insert a number for a", value=1)
b = st.number_input("Insert a number for b", value=1)
result = expensive_computation(a, b)
st.write("Result:", result)

# Session State
st.subheader("Session State Example")
if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Increment"):
    st.session_state.count += 1

st.write("Count = ", st.session_state.count)

# Theme Configuration
st.subheader("Current Theme")
st.write("Current theme:", st.get_option("theme"))
