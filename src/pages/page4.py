import streamlit as st
import time

st.title("Page 4 - Interactive Widgets")

# Progress Bar
st.subheader("Progress Bar")
my_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1)

# Form
st.subheader("Form Example")
with st.form(key="my_form"):
    text_input = st.text_input("Enter some text")
    submit_button = st.form_submit_button(label="Submit")

if submit_button:
    st.write("Submitted Text:", text_input)

# Sidebar Widgets
st.sidebar.title("Sidebar Widgets")
contact_method = st.sidebar.selectbox(
    "How would you like to be contacted?", ("Email", "Home Phone", "Mobile Phone")
)

range_values = st.sidebar.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))
st.sidebar.write("Range Values:", range_values)
