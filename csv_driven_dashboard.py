import streamlit as st
import pandas as pd
st.title("CSV Driven Dashboard")
file=st.file_uploader("Upload a CSV File", type=["csv"])
if file:
    df=pd.read_csv(file)
    st.write("Data Preview:")
    st.dataframe(df)
    st.write("Statistical Summary:")
    st.write(df.describe())
    st.write("Column-wise Data:")
    butt=st.button("Show Average Sales")
    if butt:
        if "Sales" in df.columns:
            avg_sales=df["Sales"].mean()
            st.write(f"Average Sales: {avg_sales}")
        else:
            st.write("The 'Sales' column is not present in the uploaded CSV.")
    st.write("Data Visualization:")
    butt2=st.button("Show Sales Over Time")
    if butt2:
        if "Sales" and "Date" in df.columns:
            st.line_chart(df.set_index("Date")["Sales"])
        else:
            st.write("The required columns for visualization are not present in the uploaded CSV.")