import streamlit as st
import pandas as pd
import numpy as np

@st.cache_data
def get_2022():
    data = pd.read_csv("./kobis_data_2021.csv")
    return data

def get_2021():
    data = pd.read_csv("./kobis_data_2022.csv")
    return data

def page_config():
    st.set_page_config(
        page_title="movie",
        page_icon="🚋",
    )