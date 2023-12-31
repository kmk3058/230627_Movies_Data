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
df = common.get_2021() if year == '2021' else common.get_2022()

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

    # st.divider()
  


with tab2:

    # Create the bar plot for audience Top 10 using Plotly Express
    fig2 = px.bar(audience_top10, x='영화명', y='관객수', labels={'영화명': '영화명', '관객수': '관객수'}, color='영화명', color_discrete_sequence=custom_colors)
    fig2.update_yaxes(tickformat="~s", ticksuffix="명")
    fig2.update_layout(title_text=f'{year}년 관객수 Top 10')

    # Display the audience Top 10 plot using Streamlit
    st.plotly_chart(fig2)