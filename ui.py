import streamlit as st
from page.currency import currency
from page.length import length
from page.num_sys import num
from page.speed import speed
from page.temp import temp
from page.time_1 import time
from page.vol import vol
from page.weight import weight

if "page" not in st.session_state:
    st.session_state.page = "ui"

page = st.session_state.page

st.set_page_config(
    page_title="Generic Converter",
    page_icon="🔄",
    layout="centered",
)

if page == "ui":
    
    st.markdown(
    """
    <style>
    .title {
        text-align: center; 
    }
    </style>
    <h1 class="title">GENERIC CONVERTER</h1>
    """,
    unsafe_allow_html=True
)
    st.text("")
    st.text("")
    st.subheader("UNIT CONVERSIONS")
    st.text("")
    st.text("")

    col1, spacer1, col2, spacer2, col3 = st.columns([1, 0.2, 1, 0.2, 1])
    
    with col1:
        st.image("pictures/weight-removebg-preview.png", width=80)
        if st.button("Weight"):
            st.session_state.page = "weight"
            st.rerun()

    with col2:
        st.image("pictures/length.png", width=78)
        if st.button("Length"):
            st.session_state.page = "length"
            st.rerun()

    with col3:
        st.image("pictures/speed1-removebg-preview (1).png", width=76)
        if st.button("Speed"):
            st.session_state.page = "speed"
            st.rerun()

    st.text("")
    st.text("")
    col4, spacer, col5, spacer, col6= st.columns([1,0.2,1,0.2,1])
    with col4:
        st.image("pictures/temp.png", width=74)
        if st.button("Temperature"):
            st.session_state.page = "temp"
            st.rerun()

    with col5:
        st.image("pictures/time-removebg-preview.png",width=72)
        if st.button("Time"):
            st.session_state.page="time_1"
            st.rerun()

    with col6:
        st.image("pictures/volume.png",width=70)
        if st.button("Volume"):
            st.session_state.page="vol"
            st.rerun()

    for i in range(5):
        st.text("")
    st.subheader("CURRENCY CONVERSIONS")
    st.text("")
    st.text("")
    col1=st.columns(1)[0]
    with col1:
        st.image("pictures/currency.png",width=76)
        if st.button("Currency"):
            st.session_state.page="currency"
            st.rerun()

    
    for i in range(5):
        st.text("")
    st.subheader("NUMBER SYSTEM CONVERSIONS")
    st.text("")
    st.text("")
    col1=st.columns(1)[0]
    with col1:
        st.image("pictures/num-removebg-preview.png",width=85)
        if st.button("Number System"):
            st.session_state.page="num_sys"
            st.rerun()


elif page == "weight":
    weight()

elif page == "length":
    length()

elif page == "speed":
    speed()

elif page == "temp":
    temp()

elif page == "time_1":
    time()

elif page == "vol":
    vol()

elif page == "currency":
    currency()

elif page == "num_sys":
    num()