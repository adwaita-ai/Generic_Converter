import streamlit as st
from conversions.temp_conversions import convert_temp

def temp():
    st.title("TEMPERATURE")

    col1,col2=st.columns(2)

    with col1:
        op1 = ['Fahrenheit','Kelvin','Newton','Celsius']
        from_unit = st.selectbox("From", op1)

    with col2:
        op2 = ['Fahrenheit','Kelvin','Newton','Celsius']
        to_unit = st.selectbox("To", op2)

    value = st.number_input("Enter input:", min_value=0.0, format="%.4f")

    if st.button("Convert"):
            result = convert_temp(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} is equal to {result:.4f} {to_unit}.")

    if st.button("Back to Main Page"):
        st.session_state.page = "ui"
        st.rerun()