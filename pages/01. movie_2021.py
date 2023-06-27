import streamlit as st
import commmon

common.page_config()
st.title("Data")
st.dataframe(common.get_2021(),
             use_container_width=True,
             hide_index=True)