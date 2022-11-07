from gettext import install
from turtle import title
import streamlit as st
import random
import altair as alt
import numpy as np
import pandas as pd
from vega_datasets import data

st.header('Streamlit Github Homework: California Housing')

#import data


CA_H = pd.read_csv('California_Housing.csv')
#ca = CA_H.astype(str)
st.dataframe(CA_H)


st.sidebar.header("Pick two variables for the charts")
x_val = st.sidebar.selectbox("Pick your x-axis",CA_H.select_dtypes(include=np.number).columns.tolist())
y_val = st.sidebar.selectbox("Pick your y-axis",CA_H.select_dtypes(include=np.number).columns.tolist())

scatter = alt.Chart(CA_H, title = f"Correlation between {x_val} and {y_val} ").mark_point().encode(
    alt.X(x_val, title = f"{x_val}"),
    alt.Y(y_val, title = f"{y_val}"),
    tooltip=[x_val,y_val])
st.altair_chart(scatter, use_container_width=True)

#Calculate the correlation
corr = round(CA_H[x_val].corr(CA_H[y_val]),2)
st.write(f"The correlation between {x_val} and {y_val} is {corr}")





bar = alt.Chart(CA_H, title = f" {x_val} and {y_val} ").mark_bar(fill = 'green',color = 'green').encode(
    alt.X(x_val, title = f"{x_val}"),
    alt.Y(y_val, title = f"{y_val}"),
    tooltip=[x_val,y_val]
    )

rule = alt.Chart(CA_H).mark_rule(color='red').encode(y='mean(y_val):Q')

st.altair_chart(bar, use_container_width=True)


