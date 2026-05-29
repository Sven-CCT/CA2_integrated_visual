import streamlit as st
import pandas as pd
import numpy as np
import time
#import matplotlib.pyplot as plt

st.title("Grocery Analysis")

DATE_COLUMN = 'date'

def load_data(nrows):
    data=pd.read_csv("Groceries_dataset.csv", nrows=nrows)

    lowercase=lambda x:str(x).lower()
    data.rename(lowercase, axis="columns", inplace=True)
    data.columns = data.columns.str.strip()
    data[DATE_COLUMN] = pd.to_datetime(
        data[DATE_COLUMN],
        dayfirst=True
    )

    data["transaction"] = (
        data["member_number"].astype(str)
        + "_"
        + data["date"].dt.strftime("%d-%m-%Y")
    )

    # Drop column transaction
    data = data.drop("transaction", axis="columns")

    return data

data_load_state=st.text("Data loading..")
data=load_data(5000)
time.sleep(2)
data_load_state.empty()

data_load_state=st.text("Finished loading data..")

time.sleep(2)
data_load_state.empty()

st.header("Introduction")

st.markdown('''
            **This is a data exploration of grocery transactions over a two
    year time period, 2014-2015**.
''')

st.header("Data metrics overview")

st.markdown('''
            At the start of the document there is a breakdown of general metrics
            followed by visual explorations of specific data items.
            
            For the Grocery dataset we explore the following items: 

             - Basic Metrics
             - Dataset overview
             - Metric 3 
''')

st.subheader("Basic Metrics")
# Information cards placed horizontally
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Number of customers",
        data["member_number"].nunique()
    )

with col2:
    st.metric(
        "Number of products",
        data["itemdescription"].nunique()
    )

with col3:
    st.metric(
        "Number of transactions",
        len(data)
    )

st.subheader("Dataset overview")
st.write(data.head())

product_counts = data["itemdescription"].value_counts()

product_df = product_counts.reset_index()
product_df.columns = ["product", "count"]

#st.subheader("Most popular products")
#st.dataframe(product_df)

st.subheader("Top Products Bar Chart")

st.bar_chart(
    product_df.set_index("product").head(20)
)

top10 = product_df.head(10)

# Transactions per day
daily_transactions = data.groupby("date").size()

st.subheader("Transactions Over Time")

st.line_chart(daily_transactions)

selected_product = st.selectbox(
    "Choose Product",
    sorted(data["itemdescription"].unique())
)

filtered_product = data[
    data["itemdescription"] == selected_product
]

st.write(filtered_product)



