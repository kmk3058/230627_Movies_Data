import streamlit as st
import common

common.page_config()

st.markdown("# 2021-2022 KOREA BOX OFFICE")
st.image("img/box_office.jpg")
st.divider()
# 영화 산업 데이터 분석 프로젝트 소개
st.markdown("### 🎬 프로젝트 목표")
st.markdown("영화 산업의 성장과 변동 추세, 인기 장르, 국가별 시장 동향 등에 대한 인사이트 도출")
st.divider()
st.markdown("### 🎬 Page 소개")
st.markdown("#### 🎞 RAW_DATA")
st.markdown("🔈영화의 제목, 매출액, 관객수, 대표장르, 대표국적 등의 정보")
st.markdown("#### 🎟 TOP_10") 
st.markdown("🔉2021/2022년도 각 년도 매출액과 관객수 TOP 10")
st.markdown("#### 🎫 2021_2022")
st.markdown("🔊2021 대비 2022년도 매출액, 관객수 변화 추이, 특정 장르/국가별 영화 관객수 등")
st.divider()
st.markdown("### 🎬 21/22 한국 박스오피스 미리보기")
if st.button("2021년", key='2021'):
    tabs = st.tabs(["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th"])
    for i, tab in enumerate(tabs):
        tab.image(f"./img/2021/{i+1}.png", width=400)

if st.button("2022년", key='2022'):
    tabs = st.tabs(["1st", "2nd", "4th", "5th", "6th", "7th", "8th", "9th", "10th"])
    for i, tab in enumerate(tabs):
        tab.image(f"./img/2022/{i+1}.jpg", width=400)

