import streamlit as st
from conversions.time_conversions import convert_time

def time():
    st.title("TIME")

    col1,col2=st.columns(2)

    with col1:
        op1 = ['Second','Millisecond','Microsecond','Nanosecond','Minute','Hour','Day','Week',
               'Month','Year','Decade','Century','Millenium']
        from_unit = st.selectbox("From", op1)

    with col2:
        op2 = ['Second','Millisecond','Microsecond','Nanosecond','Minute','Hour','Day','Week',
               'Month','Year','Decade','Century','Millenium']
        to_unit = st.selectbox("To", op2)

    value = st.number_input("Enter input:")

    if st.button("Convert"):
            result = convert_time(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} is equal to {result:.4f} {to_unit}.")

    if st.button("Back to Main Page"):
        st.session_state.page = "ui"
        st.rerun()
