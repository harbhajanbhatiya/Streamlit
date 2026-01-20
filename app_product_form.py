import streamlit as st
st.title("Product Form")
st.sidebar.header("Enter Product Details")
product_name = st.sidebar.text_input("Product Name")
category = st.sidebar.selectbox("Category", ["Electronics", "Clothing", "Books", "Home & Kitchen"])
st.sidebar.number_input("Price")
st.sidebar.number_input("Quantity", min_value=1, step=1)
button=st.sidebar.button("Add Product")
st.write(f"Product Name: {product_name}")
st.write(f"Category: {category}")   
if button:
    st.write("Product added successfully!")