import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import streamlit as st
import plotly.express as px
import common

common.page_config()

st.title("2021/2022 BoxOffice Comparison Analysis")

df_2021 = common.get_2021()
df_2022 = common.get_2022()

tab1, tab2 = st.tabs(["Country", "Genre"])

with tab1:

    sale_grp_2021 = df_2021.groupby('대표국적')['매출액'].sum().nlargest(5)
    sale_grp_2022 = df_2022.groupby('대표국적')['매출액'].sum().nlargest(5)

    # 데이터프레임 생성
    data_2021 = {
        '국가': list(sale_grp_2021.index),
        '매출(단위 억원)': list(sale_grp_2021.values // 100_000_000)
    }

    data_2022 = {
        '국가': list(sale_grp_2022.index),
        '매출(단위 억원)': list(sale_grp_2022.values // 100_000_000)
    }

    # 2021년 데이터 그래프 생성
    fig_2021 = px.bar(data_frame=data_2021, x='국가', y='매출(단위 억원)',
                    labels={'국가': '국가', '매출(단위 억원)': '매출(단위 억원)'}, color_discrete_sequence=['#FF6F61'])

    # 2022년 데이터 그래프 생성
    fig_2022 = px.bar(data_frame=data_2022, x='국가', y='매출(단위 억원)',
                    labels={'국가': '국가', '매출(단위 억원)': '매출(단위 억원)'}, color_discrete_sequence=['#6B5B95'])

    # 2021년 그래프 출력
    st.plotly_chart(fig_2021)

    # 2022년 그래프 출력
    st.plotly_chart(fig_2022)


with tab2: 

    gnr_repl_2021 = df_2021['대표장르']
    gnr_grp_2021 = gnr_repl_2021.groupby(gnr_repl_2021.values).count()

    gnr_repl_2022 = df_2022['대표장르']
    gnr_grp_2022 = gnr_repl_2022.groupby(gnr_repl_2022.values).count()

    # 데이터프레임 생성
    data_2021 = {
        '장르': list(gnr_grp_2021.index),
        '상영수': list(gnr_grp_2021.values)
    }

    data_2022 = {
        '장르': list(gnr_grp_2022.index),
        '상영수': list(gnr_grp_2022.values)
    }

    # 2021년 데이터 그래프 생성
    fig_2021 = px.bar(data_frame=data_2021, x='장르', y='상영수',
                    labels={'장르': '장르', '상영수': '상영수'}, color_discrete_sequence=['#FF6F61'])

    # 2022년 데이터 그래프 생성
    fig_2022 = px.bar(data_frame=data_2022, x='장르', y='상영수',
                    labels={'장르': '장르', '상영수': '상영수'}, color_discrete_sequence=['#6B5B95'])

    # 2021년 그래프 출력
    st.plotly_chart(fig_2021)

    # 2022년 그래프 출력
    st.plotly_chart(fig_2022)
