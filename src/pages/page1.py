import streamlit as st
import pandas as pd
import numpy as np

st.title("Page 1 - Widgets Galore")
st.write("This page demonstrates various Streamlit widgets.")

# Checkbox
if st.checkbox("Show DataFrame"):
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.line_chart(chart_data)

# Radio Buttons
genre = st.radio("What's your favorite genre?", ("Comedy", "Drama", "Documentary"))

if genre == "Comedy":
    st.write("You selected Comedy.")
else:
    st.write("You didn't select Comedy.")

# File Uploader
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.read()
    st.write("Filename:", uploaded_file.name)
    st.write(bytes_data)
