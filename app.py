import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import streamlit as st
import plotly.express as px
import common

common.page_config()

st.title("21-22년 기간별 박스오피스")

st.image("img/box_office.jpg")

# Year selection
year = st.selectbox("년도 선택", ['2021년', '2022년'])

if year == '2021년':
    df = common.get_2021()  # Get 2021 data
else:
    df = common.get_2022()  # Get 2022 data

# Show the selected year's data
st.write(f"{year} 데이터:")
st.write(df)

# Visualization on the next page
if st.button("다음 페이지로"):
    # Store the selected year's data in session state
    st.session_state['selected_year_data'] = df
    # Store the selected year in session state
    st.session_state['selected_year'] = year
    # Redirect to the next page
    st.experimental_rerun()

# Next page
if 'selected_year_data' in st.session_state:
    selected_year_data = st.session_state['selected_year_data']
    selected_year = st.session_state['selected_year']

    if selected_year == '2021년':
        st.title("2021년 박스오피스 Top 10")

        # Define custom colors
        custom_colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1', '#955251', '#B565A7', '#009B77', '#DD4124', '#D65076']

        tab1, tab2 = st.tabs(["Sales", "Numbers"])

        with tab1:
            # Select the top 10 movies by revenue
            sales_top10 = selected_year_data[['영화명', '매출액']].sort_values(by='매출액', ascending=False).head(10)

            # Create the bar plot using Plotly Express
            fig = px.bar(sales_top10, x='영화명', y='매출액', labels={'영화명': '영화명', '매출액': '매출액'}, color='영화명', color_discrete_sequence=custom_colors)
            fig.update_yaxes(tickformat="~s", ticksuffix="원")
            fig.update_layout(title_text='2021년 매출액 top 10')

            # Display the plot using Streamlit
            st.plotly_chart(fig)

        with tab2:
            # Select the top 10 movies by audience count
            audience_top10 = selected_year_data[['영화명', '관객수']].sort_values(by='관객수', ascending=False).head(10)

            # Create the bar plot using Plotly Express
            fig = px.bar(audience_top10, x='영화명', y='관객수', labels={'영화명': '영화명', '관객수': '관객수'}, color='영화명', color_discrete_sequence=custom_colors)
            fig.update_yaxes(tickformat="~s", ticksuffix="명")
            fig.update_layout(title_text='2021년 관객수 top 10')

            # Display the plot using Streamlit
            st.plotly_chart(fig)

    else:
        st.title("2022년 박스오피스 Top 10")

        # Define custom colors
        custom_colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1', '#955251', '#B565A7', '#009B77', '#DD4124', '#D65076']

        tab1, tab2 = st.tabs(["Sales", "Numbers"])

        with tab1:
            # Select the top 10 movies by revenue
            sales_top10 = selected_year_data[['영화명', '매출액']].sort_values(by='매출액', ascending=False).head(10)

            # Create the bar plot using Plotly Express
            fig = px.bar(sales_top10, x='영화명', y='매출액', labels={'영화명': '영화명', '매출액': '매출액'}, color='영화명', color_discrete_sequence=custom_colors)
            fig.update_yaxes(tickformat="~s", ticksuffix="원")
            fig.update_layout(title_text='2022년 매출액 top 10')

            # Display the plot using Streamlit
            st.plotly_chart(fig)

        with tab2:
            # Select the top 10 movies by audience count
            audience_top10 = selected_year_data[['영화명', '관객수']].sort_values(by='관객수', ascending=False).head(10)

            # Create the bar plot using Plotly Express
            fig = px.bar(audience_top10, x='영화명', y='관객수', labels={'영화명': '영화명', '관객수': '관객수'}, color='영화명', color_discrete_sequence=custom_colors)
            fig.update_yaxes(tickformat="~s", ticksuffix="명")
            fig.update_layout(title_text='2022년 관객수 top 10')

            # Display the plot using Streamlit
            st.plotly_chart(fig)


# st.write("[Data](/Data)")