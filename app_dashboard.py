import streamlit as st
st.title("Simple Sales Dashboard")
st.header("This is a Simple Sales Dashboard using Streamlit.")
sales={"January": 1200, "February": 1500, "March": 900, "April": 2000}
sale_month=st.selectbox("Select Month to View Sales", list(sales.keys()))
st.metric(label="Sales Amount", value=f"{sales[sale_month]}")
st.bar_chart(list(sales.values()))




