import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import streamlit as st
import plotly.express as px
import common

common.page_config()

st.title("2022년 박스오피스 Top 10")

df = common.get_2021()

# Define custom colors
custom_colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1', '#955251', '#B565A7', '#009B77', '#DD4124', '#D65076']

tab1, tab2 = st.tabs(["Sales", "Numbers"])

with tab1:
    # Select the top 10 movies by revenue
    sales_top10 = df[['영화명', '매출액']].sort_values(by='매출액', ascending=False).head(10)

    # Create the bar plot using Plotly Express
    fig = px.bar(sales_top10, x='영화명', y='매출액', labels={'영화명': '영화명', '매출액': '매출액'}, color='영화명', color_discrete_sequence=custom_colors)
    fig.update_yaxes(tickformat="~s", ticksuffix="원")
    fig.update_layout(title_text='2022년 매출액 top 10')

    # Display the plot using Streamlit
    st.plotly_chart(fig)

with tab2:
    # Select the top 10 movies by audience count
    audience_top10 = df[['영화명', '관객수']].sort_values(by='관객수', ascending=False).head(10)

    # Create the bar plot using Plotly Express
    fig = px.bar(audience_top10, x='영화명', y='관객수', labels={'영화명': '영화명', '관객수': '관객수'}, color='영화명', color_discrete_sequence=custom_colors)
    fig.update_yaxes(tickformat="~s", ticksuffix="명")
    fig.update_layout(title_text='2022년 관객수 top 10')

    # Display the plot using Streamlit
    st.plotly_chart(fig)

tab3, tab4 = st.tabs(["Country", "Genre"])

with tab3:
    # 데이터프레임 생성
    data = {
        'Year': ['2021'] * len(sale_grp_2021) + ['2022'] * len(sale_grp_2022),
        '국가': list(sale_grp_2021.index) + list(sale_grp_2022.index),
        '매출(단위 억원)': list(sale_grp_2021.values // 100_000_000) + list(sale_grp_2022.values // 100_000_000)
    }

    # Plotly Express를 사용하여 막대 그래프 생성
    fig = px.bar(data_frame=data, x='국가', y='매출(단위 억원)', color='Year',
                labels={'국가': '국가', '매출(단위 억원)': '매출(단위 억원)', 'Year': '연도'})

    # 그래프 레이아웃 설정
    fig.update_layout(
        title='국가별 매출 성장률',
        xaxis_tickangle=-45,
        legend_title='연도'
    )

    # Streamlit에서 그래프 출력
    st.plotly_chart(fig)

with tab4:
    gnr_repl_20021 = df_2021['대표장르']
    gnr_grp_2021 = gnr_repl_20021.groupby(gnr_repl_20021.values).count()

        # 데이터프레임 생성
    data = {
        'Year': ['2021'] * len(gnr_grp_2021) + ['2022'] * len(gnr_grp_2022),
        '장르': list(gnr_grp_2021.index) + list(gnr_grp_2022.index),
        '상영수': list(gnr_grp_2021.values) + list(gnr_grp_2022.values)
    }

    # Plotly Express를 사용하여 막대 그래프 생성
    fig = px.bar(data_frame=data, x='장르', y='상영수', color='Year',
                labels={'장르': '장르', '상영수': '상영수', 'Year': '연도'})

    # 그래프 레이아웃 설정
    fig.update_layout(
        title='장르별 상영수',
        xaxis_tickangle=-45,
        legend_title='연도'
    )

    # Streamlit에서 그래프 출력
    st.plotly_chart(fig)