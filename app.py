from gettext import install
from turtle import title
import streamlit as st
import random
import altair as alt
import numpy as np
import pandas as pd
from vega_datasets import data

st.header('Streamlit Github Homework')

#import data

air_data = pd.read_csv('Environment_Data_Atlas.csv')
air = air_data.astype(str)
st.dataframe(air_data)

bar = alt.Chart(air_data).mark_bar().encode(
    x = 'Country Name:Q',
    y = 'Value:N'
)


st.altair_chart(bar, use_container_width=True)
