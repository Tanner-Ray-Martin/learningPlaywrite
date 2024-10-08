import streamlit as st
import pandas as pd
import numpy as np
import datetime

st.set_page_config(page_title="Streamlit Feature Showcase", layout="wide")

st.title("Streamlit Feature Showcase")
st.write("Welcome to the Streamlit Feature Showcase App!")

st.sidebar.title("Navigation")
st.sidebar.write("Use the pages in the sidebar to explore different features.")

# Sample DataFrame
df = pd.DataFrame(np.random.randn(50, 3), columns=["A", "B", "C"])

st.subheader("Sample Data")
st.dataframe(df)

# Line Chart
st.subheader("Line Chart")
st.line_chart(df)

# Button
if st.button("Say hello"):
    st.write("Hello!")
else:
    st.write("Goodbye")

# Slider
age = st.slider("How old are you?", 0, 130, 25)
st.write("I'm ", age, "years old")

# Text Input
name = st.text_input("What's your name?", "John Doe")
st.write("Hello, ", name)

# Date Input
d = st.date_input("When's your birthday", datetime.date(1990, 1, 1))
st.write("Your birthday is:", d)

# Selectbox
option = st.selectbox("Which number do you like best?", df["A"])

st.write("You selected:", option)
