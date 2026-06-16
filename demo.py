import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.DataFrame({
    "Name": ["Dimple", "Nitasha", "Nisha", "Komal"],
    "Roll no": [101, 102, 103, 104],
    "Obtained_marks": [97, 95, 76, 80]
})

fig = px.bar(
    df,
    x="Name",
    y="Obtained_marks",
    text="Obtained_marks"
)

st.plotly_chart(fig)