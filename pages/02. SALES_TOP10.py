import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import streamlit as st
import plotly.express as px
import common
common.page_config()

# Sidebar
st.sidebar.title("박스오피스 Top 10")
year = st.sidebar.radio("년도 선택", ['2021', '2022'])

# Display selected year's Top 10 data and images
st.title(f"{year}년 박스오피스 Top 10")
df = common.get_2021() if year == '2021년' else common.get_2022()

# Select the top 10 movies by revenue
sales_top10 = df[['영화명', '매출액']].sort_values(by='매출액', ascending=False).head(10)

# Select the top 10 movies by audience count
audience_top10 = df[['영화명', '관객수']].sort_values(by='관객수', ascending=False).head(10)

# Define custom colors
custom_colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1', '#955251', '#B565A7', '#009B77', '#DD4124', '#D65076']

tab1, tab2 = st.tabs(["매출액 Top 10", "관객수 Top 10"])

with tab1:
    # Create the bar plot for sales Top 10 using Plotly Express
    fig1 = px.bar(sales_top10, x='영화명', y='매출액', labels={'영화명': '영화명', '매출액': '매출액'}, color='영화명', color_discrete_sequence=custom_colors)
    fig1.update_yaxes(tickformat="~s", ticksuffix="원")
    fig1.update_layout(title_text=f'{year}년 매출액 Top 10')

    # Display the sales Top 10 plot using Streamlit
    st.plotly_chart(fig1)

    st.divider()
    st.write("{year}년도 매출액 기준 순위 포스터")
    tab_menus = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th"]
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs(tab_menus)

    if year == '2021':
        tab1.image("./img/2021/1.png")
        tab2.image("./img/2021/2.png")
        tab3.image("./img/2021/3.png")
        tab4.image("./img/2021/4.png")
        tab5.image("./img/2021/5.jpg")
        tab6.image("./img/2021/6.png")
        tab7.image("./img/2021/7.png")
        tab8.image("./img/2021/8.png")
        tab9.image("./img/2021/9.jpg")
        tab10.image("./img/2021/10.png")
    
    elif year == '2022':
        tab1.image("./img/2022/1.png")
        tab2.image("./img/2022/2.png")
        tab4.image("./img/2022/4.png")
        tab5.image("./img/2022/5.jpg")
        tab6.image("./img/2022/6.png")
        tab7.image("./img/2022/7.png")
        tab8.image("./img/2022/8.png")
        tab9.image("./img/2022/9.jpg")
        tab10.image("./img/2022/10.png")



with tab2:
    # Create the bar plot for audience Top 10 using Plotly Express
    fig2 = px.bar(audience_top10, x='영화명', y='관객수', labels={'영화명': '영화명', '관객수': '관객수'}, color='영화명', color_discrete_sequence=custom_colors)
    fig2.update_yaxes(tickformat="~s", ticksuffix="명")
    fig2.update_layout(title_text=f'{year}년 관객수 Top 10')

    # Display the audience Top 10 plot using Streamlit
    st.plotly_chart(fig2)