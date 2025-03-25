import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Data Dashboard")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    # Data Preview
    st.subheader("Data Preview")
    st.write(df.head())
    
    # Data Summary
    st.subheader("Data Summary")
    st.write(df.describe())
    
    # Data Filtering
    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value", unique_values)
    
    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)
    
    # Data Plotting
    st.subheader("Plot Data")
    x_column = st.selectbox("Select X-axis column", columns)
    y_column = st.selectbox("Select Y-axis column", columns)
    
    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])
else:
    st.warning("Waiting for file upload...")
