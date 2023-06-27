import streamlit as st
import common

common.page_config()
st.title("2022년 박스오피스 Data")
st.dataframe(common.get_2022(),
             use_container_width=True,
             hide_index=True)