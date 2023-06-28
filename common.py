import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns


def get_2021():
    data_2021 = pd.read_csv("./kobis_data_2021.csv")
    return data_2021

def get_2022():
    data_2022 = pd.read_csv("./kobis_data_2022.csv")
    return data_2022

def page_config():
    st.set_page_config(
        page_title="movie"
        ,page_icon=":클래퍼:"
    )