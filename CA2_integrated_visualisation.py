import streamlit as st
import pandas as pd
import numpy as np

st.title("Retail Dashboard Exploration")

DATE_COLUMN = 'date'

def load_data(nrows):
    data=pd.read_csv("Groceries_dataset.csv", nrows=nrows)

    lowercase=lambda x:str(x).lower()
    data.rename(lowercase, axis="columns", inplace=True)
    data[DATE_COLUMN]=pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state=st.text("Data loading..")
data=load_data(1000)
data_load_state=st.text("Finished loading data..")

st.subheader("Original Data")
st.write(data)

product_counts = data["itemdescription"].value_counts()

product_df = product_counts.reset_index()
product_df.columns = ["product", "count"]

st.subheader("Product Frequency")
st.dataframe(product_df)

st.subheader("Top Products Bar Chart")

st.bar_chart(
    product_df.set_index("product").head(20)
)

top10 = product_df.head(10)


st.subheader("Top 10 Products - Pie Chart")

st.pyplot(
    top10.set_index("product")
         .plot.pie(
             y="Count",
             figsize=(8,8),
             legend=False
         ).figure
)