import streamlit as st
import common

common.page_config()

st.title("2021-2022년 한국 박스오피스 영화 ")

st.image("img/box_office.jpg")

# 영화 산업 데이터 분석 프로젝트 소개
st.markdown("### Page 소개")
st.markdown("RAW_DATA : 영화의 제목, 매출액, 관객수, 대표장르, 대표국적 등의 정보")
st.markdown("TOP_10 : 2021/2022년도 각 년도 매출액과 관객수 TOP 10")
st.markdown("2021_2022 : 2021 대비 2022년도 매출액, 관객수 변화 추이, 특정 장르/국가별 영화 관객수 ")

import streamlit as st

st.sidebar.title("박스오피스 데이터")
# year = st.sidebar.radio("년도 선택", ['2021', '2022'])

st.title("2021-2022년 한국 박스오피스")

if st.button("2021년", key='2021'):
    tabs = st.tabs(["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th"])
    for i, tab in enumerate(tabs):
        tab.image(f"./img/2021/{i+1}.png", width=300)

if st.button("2022년", key='2022'):
    tabs = st.tabs(["1st", "2nd", "4th", "5th", "6th", "7th", "8th", "9th", "10th"])
    for i, tab in enumerate(tabs):
        tab.image(f"./img/2022/{i+1}.jpg", width=300)

