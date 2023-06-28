import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import streamlit as st
import plotly.express as px
import common

common.page_config()

st.title("2022년 박스오피스 Top 10")

df = common.get_2022()

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