import streamlit as st
import common

common.page_config()

# Sidebar
st.sidebar.title("박스오피스 데이터")
year = st.sidebar.radio("년도 선택", ['2021년', '2022년'])

# Display selected year's data
st.title(f"{year} 박스오피스 Data")
if year == '2021년':
    df_2021 = common.get_2021()
    df_2021 = df_2021.iloc[:, 1:]  # Exclude the first column
    st.dataframe(df_2021, use_container_width=True, hide_index=True)
else:
    df_2022 = common.get_2022()
    df_2022 = df_2022.iloc[:, 1:]  # Exclude the first column
    st.dataframe(df_2022, use_container_width=True, hide_index=True)
