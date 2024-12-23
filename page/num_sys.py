import streamlit as st
from conversions.num_conversions import convert_num

def num():
    st.title("NUMBER SYSTEM")

    col1, col2 = st.columns(2)

    with col1:
        op1 = ['Binary(base 2)','Octal(base 8)','Decimal(base 10)','Hexadecimal(base 16)']
        from_unit = st.selectbox("From", op1)

    with col2:
        op2 = ['Binary(base 2)','Octal(base 8)','Decimal(base 10)','Hexadecimal(base 16)']
        to_unit = st.selectbox("To", op2)

    value = st.text_input("Enter input:")

    if st.button("Convert"):
        if value == 0:
            st.warning("Please enter a value greater than 0.")
        else:
            result = convert_num(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} is equal to {result} {to_unit}.")

    if st.button("Back to Main Page"):
        st.session_state.page = "ui"
        st.rerun()