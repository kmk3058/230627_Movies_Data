import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import streamlit as st
import plotly.graph_objects as go
import common

# Streamlit File *.py
import platform
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Window':
    rc('font', family='NanumGothic')

# # 폰트 경로 설정
# font_path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'
# # 폰트 이름 얻어오기
# font_name = fm.FontProperties(fname=font_path).get_name()
# # 한글 폰트 설정
# plt.rcParams['font.family'] = 'NanumGothic'

common.page_config()

st.title("2021 Top 10")

df = common.get_2021()

# genre_counts = df['Genre'].value_counts().sort_values(ascending=False)

tab1, tab2 = st.tabs(["Sales", "Numbers"])

with tab1:
    # Select the top 10 movies by revenue
    sales_top10 = df[['영화명', '매출액']].sort_values(by='매출액', ascending=False).head(10)
    # Create the bar plot
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=sales_top10, x='영화명', y='매출액', ax=ax)
    # 축의 눈금 표시 방식 조정
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{x/1e8:.0f}억 원'))
    # x축 눈금 회전
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    plt.title('2021년 매출액 top 10', fontsize=15)
    plt.xlabel('영화명', fontsize=15)
    plt.ylabel('매출액', fontsize=15)
    st.pyplot(fig)

with tab2:
    # Select the top 10 movies by audience count
    audience_top10 = df[['영화명', '관객수']].sort_values(by='관객수', ascending=False).head(10)

    # Create the bar plot
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=audience_top10, x='영화명', y='관객수', ax=ax)

    # Customize the plot
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{x/1e4:.0f}만 명'))
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    plt.title('2021년 관객수 top 10', fontsize=15)
    plt.xlabel('영화명', fontsize=15)
    plt.ylabel('관객수', fontsize=15)

    # Display the plot using Streamlit
    st.pyplot(fig)