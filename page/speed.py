import streamlit as st
from conversions.speed_conversions import convert_speed

def speed():
    st.title("SPEED")

    col1, col2 = st.columns(2)

    with col1:
        op1 = ['m/s','m/hr','m/min','km/s','km/hr','km/min','cm/s','cm/hr','cm/min',
               'mm/s','mm/hr','mm/min','mile']
        from_unit = st.selectbox("From", op1)

    with col2:
        op2 = ['m/s','m/hr','m/min','km/s','km/hr','km/min','cm/s','cm/hr','cm/min',
               'mm/s','mm/hr','mm/min','mile']
        to_unit = st.selectbox("To", op2)

    value = st.number_input("Enter input:", min_value=0.0, format="%.4f")

    if st.button("Convert"):
        if value == 0:
            st.warning("Please enter a value greater than 0.")
        else:
            result = convert_speed(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} is equal to {result:.4f} {to_unit}.")

    if st.button("Back to Main Page"):
        st.session_state.page = "ui"
        st.rerun()