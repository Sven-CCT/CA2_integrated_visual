import streamlit as st
import pandas as pd
import numpy as np

st.title("Retail Dashboard Exploration")

DATE_COLUMN = 'Date'

def load_data(nrows):
    data=pd.read_csv("Groceries_dataset.csv", nrows=nrows)

    lowercase=lambda x:str(x).lower
    data.rename(lowercase, axis="columns", inplace=True)
    data[DATE_COLUMN]=pd.to_datetime(data[DATE_COLUMN])
    return data