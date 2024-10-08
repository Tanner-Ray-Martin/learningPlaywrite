import streamlit as st
import plotly.express as px
from bokeh.plotting import figure
import altair as alt

st.title("Page 2 - Data Visualization")

# Plotly Chart
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
st.plotly_chart(fig)

# Bokeh Chart
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]
p = figure(title="Simple Line Example", x_axis_label="x", y_axis_label="y")

p.line(x, y, legend_label="Trend", line_width=2)
st.bokeh_chart(p, use_container_width=True)

# Altair Chart
c = (
    alt.Chart(df)
    .mark_circle()
    .encode(x="sepal_width", y="sepal_length", color="species")
)
st.altair_chart(c, use_container_width=True)
