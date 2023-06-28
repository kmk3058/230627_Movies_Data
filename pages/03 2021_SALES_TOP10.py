import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import streamlit as st
import plotly.express as px
import common

common.page_config()

st.title("2021년 박스오피스 Top 10")

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


st.divider()
st.write("2021년 매출액 기준 순위 포스터")
tab_menus = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th"]
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs(tab_menus)
tab1.image("./img/2021/01.png")
tab2.image("./img/2021/02.png")
tab3.image("./img/2021/03.png")
tab4.image("./img/2021/04.png")
tab5.image("./img/2021/05.jpg")
tab6.image("./img/2021/06.png")
tab7.image("./img/2021/07.png")
tab8.image("./img/2021/08.png")
tab9.image("./img/2021/09.jpg")
tab10.image("./img/2021/10.png")