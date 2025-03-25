import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.write("Simple Data Dashboard")

up_load_flie = st.file_uploader("Choose CSV File", type="csv")

if up_load_flie is not None:
    df = pd.read_csv(up_load_flie)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    colums = df.columns.tolist()
    selected_column = st.selectbox("selecte colum to filter by", colums)
    unique_value = df[selected_column].unique()
    seleted_value = st.selectbox("select value", unique_value)

    filter_df = df[df[selected_column]  == seleted_value ]
    st.write(filter_df)

    st.subheader("Plot Data")
    x_colmn = st.selectbox("select x_axis column ", colums)
    y_colmn = st.selectbox("select y_axis column ", colums)

    if st.button("Generate plot"):
        st.line_chart(filter_df.set_index(x_colmn)[y_colmn])

else:
    st.write("waiting onfile upload...")
    