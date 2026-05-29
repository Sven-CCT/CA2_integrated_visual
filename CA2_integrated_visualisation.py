import streamlit as st
import pandas as pd
import numpy as np
import time
#import matplotlib.pyplot as plt

#st.title("Grocery Analysis")

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


#st.markdown('''
 #           **This is a data exploration of grocery transactions over a two
  #  year time period, 2014-2015**.
#''')
st.markdown(
    """
    <div style="
        background-color:#E8F1FA;
        padding:15px;
        border-radius:10px;
    ">
    <h1> Grocery Shopping Dashboard</h1>
    <p><b>Data exploration of grocery transactions over a two
    year time period, 2014-2015</b></p>
    </div>
    """,
    unsafe_allow_html=True
)

st.header("Introduction")


st.header("Data metrics overview")

st.markdown('''
            At the start of the document there is a breakdown of general metrics
            followed by visual explorations of specific data items.
            
            For the Grocery dataset we explore the following items: 

             - Basic Metrics
             - Dataset overview
             - Product popularity distribution
             - Transactions over time
             - Product analyser
             
            
''')

st.divider()

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

st.divider()    

st.info(
    'This dashboard shows a sample of the dataset. Select "Show Detailed Data to access the full dataset."'
)
st.subheader("Dataset overview - sample")
st.write(data.head())

if st.checkbox("Show Detailed Data"):
    st.dataframe(data)

product_counts = data["itemdescription"].value_counts()

product_df = product_counts.reset_index()
product_df.columns = ["product", "count"]

#st.subheader("Most popular products")
#st.dataframe(product_df)

st.divider()

st.success(
    "Below we find the product listed as a bar chart. On the left side (Y-axis)" \
    "we find the number of items sold indicated and at the bottom (x-axis) all products " \
    "sold are listed."
)

st.subheader("Most Popular Products")

st.bar_chart(
    product_df.set_index("product").head(20)
)

top10 = product_df.head(10)

# Transactions per day
daily_transactions = data.groupby("date").size()

st.divider()

st.subheader("Transactions Over Time")

st.line_chart(daily_transactions)

st.divider()

st.subheader("Product Analyser")

selected_product = st.selectbox(
    "Choose Product",
    sorted(data["itemdescription"].unique())
)

filtered_product = data[
    data["itemdescription"] == selected_product
]

st.write(filtered_product)



