import streamlit as st
st.title("Discount Calculator")
price = st.number_input("Enter the original price",)
st.write(f"Original Price: {price}")
discount = st.slider("Select discount percentage", 0, 50, 10)
st.write(f"Discount: {discount}%")
button=st.button("Calculate Final Price")
final_price = price * (1 - discount / 100)
if button:
    st.write(f"Final Price after {discount}% discount: {final_price}")    
table=st.button("Show Summary Table")
if table:
    st.table({
        "Original Price": [price],
        "Discount (%)": [discount],
        "Final Price": [final_price]
    })