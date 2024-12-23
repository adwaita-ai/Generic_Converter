import streamlit as st
from conversions.vol_conversions import convert_vol

def vol():
    st.title("VOLUME")
    
    col1, col2 = st.columns(2)

    with col1:
        op1 = ['Cubic meter','Cubic kilometer','Cubic centimeter','Cubic millimeter','Litre','Kilolitre',
               'Millilitre','Barrel','Gallon','Quart','Pint','Cubic mile','Cubic inch']
        from_unit = st.selectbox("From", op1)

    with col2:
        op2 = ['Cubic meter','Cubic kilometer','Cubic centimeter','Cubic millimeter','Litre','Kilolitre',
               'Millilitre','Barrel','Gallon','Quart','Pint','Cubic mile','Cubic inch']
        to_unit = st.selectbox("To", op2)

    value = st.number_input("Enter input:", min_value=0.0, format="%.4f")

    if st.button("Convert"):
        if value == 0:
            st.warning("Please enter a value greater than 0.")
        else:
            result = convert_vol(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} is equal to {result:.4f} {to_unit}.")

    if st.button("Back to Main Page"):
        st.session_state.page = "ui"
        st.rerun()