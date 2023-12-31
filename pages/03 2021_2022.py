import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import common
import matplotlib.font_manager as fm
font_path = './NanumGothic.ttf'
##
# # 폰트 로드
font_prop = fm.FontProperties(fname=font_path)
# # 기본 폰트 설정
plt.rcParams['font.family'] = font_prop.get_name()
common.page_config()
st.title("2021/2022 BoxOffice Analysis")
df_2021 = common.get_2021()
df_2022 = common.get_2022()
data_2021 = common.get_2021()
data_2022 = common.get_2022()
top10_2021 = data_2021.head(10)
top10_2022 = data_2022.head(10)
# top10_2021_sorted = top10_2021.sort_values(by='매출액', ascending=False)
# top10_2022_sorted = top10_2022.sort_values(by='매출액', ascending=False)
# index = np.arange(len(top10_2021_sorted))
# w = 0.4
# 순위 = [f"{i+1}위" for i in range(10)]
# plt.title('2021년과 2022년 TOP10 매출 비교', fontproperties=font_prop)
# plt.bar(index - w/2, top10_2021_sorted['매출액'], width=w, label='2021', color='#FFD0D0')
# plt.bar(index + w/2, top10_2022_sorted['매출액'], width=w, label='2022', color='#3AA6B9')
# plt.xticks(index, 순위, fontproperties=font_prop)
# # y축의 형식을 변경하기 위해 ticker를 사용합니다.
# plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{x/1e8:.0f}억 원'))
# # y축 레이블에 폰트 적용
# plt.gca().set_yticklabels(plt.gca().get_yticklabels(), fontproperties=font_prop)
# plt.legend()
# st.pyplot(plt.gcf())
tab_names = ['국가/장르 비교','국가별 관객 수', '매출/관객 수 비교']
active_tab = st.sidebar.radio('', tab_names)
if active_tab == '국가/장르 비교':
    tab1, tab2 = st.tabs(["국가별", "장르별"])
    with tab1:
        sale_grp_2021 = df_2021.groupby('대표국적')['매출액'].sum().nlargest(5)
        sale_grp_2022 = df_2022.groupby('대표국적')['매출액'].sum().nlargest(5)
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
            title='국가별 매출 성장 수준',
            xaxis_tickangle=-45,
            legend_title='연도',
            bargap=0.5  # 막대 간격 조정 (기본값은 0.2)
        )
        # Streamlit에서 그래프 출력
        st.plotly_chart(fig)
    with tab2:
        gnr_repl_2021 = df_2021['대표장르']
        gnr_grp_2021 = gnr_repl_2021.groupby(gnr_repl_2021.values).count()
        gnr_repl_2022 = df_2022['대표장르']
        gnr_grp_2022 = gnr_repl_2022.groupby(gnr_repl_2022.values).count()
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
        legend_title='연도',
        bargap=0.5  # 막대 간격 조정 (기본값은 0.2)
        )
        # Streamlit에서 그래프 출력
        st.plotly_chart(fig)
elif active_tab == '국가별 관객 수':
    tab3, tab4= st.tabs(["2021년", "2022년"])
    with tab3:
        grp_audi_2021 = df_2021.groupby('대표국적')['관객수'].sum()
        # 전체 관객수 대비 비중 계산
        total_audi_2021 = grp_audi_2021.sum()
        grp_audi_2021 = grp_audi_2021 / total_audi_2021
        # 1% 미만 비중을 가지는 국가들을 기타로 묶기
        threshold = 0.01
        other_audi_2021 = grp_audi_2021[grp_audi_2021 < threshold]
        other_audi_2021_sum = other_audi_2021.sum()
        grp_audi_2021 = grp_audi_2021[grp_audi_2021 >= threshold]
        grp_audi_2021['기타'] = other_audi_2021_sum
        # 데이터프레임 생성
        labels = grp_audi_2021.index
        values = grp_audi_2021.values
        # 파이 차트 생성
        data = [go.Pie(labels=labels, values=values)]
        # 레이아웃 설정
        layout = go.Layout(title='국가별 영화 관객수')
        # 그래프 생성
        fig = go.Figure(data=data, layout=layout)
        # Streamlit에서 그래프 출력
        st.plotly_chart(fig)
    with tab4:
        grp_audi_2022 = df_2022.groupby('대표국적')['관객수'].sum()
        # 전체 관객수 대비 비중 계산
        total_audi_2022 = grp_audi_2022.sum()
        grp_audi_2022 = grp_audi_2022 / total_audi_2022
        # 1% 미만 비중을 가지는 국가들을 기타로 묶기
        threshold = 0.01
        other_audi_2022 = grp_audi_2022[grp_audi_2022 < threshold]
        other_audi_2022_sum = other_audi_2022.sum()
        grp_audi_2022 = grp_audi_2022[grp_audi_2022 >= threshold]
        grp_audi_2022['기타'] = other_audi_2022_sum
        # 데이터프레임 생성
        labels = grp_audi_2022.index
        values = grp_audi_2022.values
        # 파이 차트 생성
        data = [go.Pie(labels=labels, values=values)]
        # 레이아웃 설정
        layout = go.Layout(title='국가별 영화 관객수')
        # 그래프 생성
        fig = go.Figure(data=data, layout=layout)
        # Streamlit에서 그래프 출력
        st.plotly_chart(fig)
elif active_tab == '매출/관객 수 비교':
    tab5, tab6= st.tabs(["매출 비교", "관객 수 비교"])
    with tab5:
        top10_2021_sorted = data_2021.sort_values(by='매출액', ascending=False).head(10)
        top10_2022_sorted = data_2022.sort_values(by='매출액', ascending=False).head(10)
        x = top10_2021_sorted['영화명']
        y1 = top10_2021_sorted['매출액']
        y2 = top10_2022_sorted['매출액']
        fig = go.Figure()
        fig.add_trace(go.Bar(x=x, y=y1, name='2021', marker_color='#FFD0D0'))
        fig.add_trace(go.Bar(x=x, y=y2, name='2022', marker_color='#3AA6B9'))
        fig.update_layout(
            title={
            'text': '2021/2022 TOP10 매출 비교',
            'font': {'size': 20},
            'x': 0.25
        },
                        # xaxis_tickangle=-45,
            yaxis=dict(
                ticksuffix='원',
                tickfont=dict(size=15)
            ),
            xaxis=dict(
                tickmode='array',
                tickvals=[i for i in range(10)],
                ticktext=[f'{i+1}위' for i in range(10)],  # x축의 틱 레이블을 1위에서 10위로 표시
                tickfont=dict(size=15)
            ),
            # legend=dict(
            #     x=0.5,
            #     y=1.1,
            #     orientation='h'
            # ),
        )
        st.plotly_chart(fig)
    with tab6:
        value_2021 = data_2021['관객수'].sum()
        value_2022 = data_2022['관객수'].sum()
        total = value_2021 + value_2022  # 값의 합계 계산
        values = [value_2021, value_2022]
        labels = [f'2021년\n{value_2021:,}명', f'2022년\n{value_2022:,}명']
        colors = ['#FFD0D0', '#3AA6B9']
        plt.figure(figsize=(3.5,3.5),dpi= 300)
        plt.pie(values, labels=labels, autopct='%0.1f%%', colors=colors, startangle=90, textprops = {"fontproperties" : font_prop})
        plt.title('2021/2022 TOP10 관객수 비교' , fontproperties = font_prop)
        plt.axis('equal')
        plt.show()
        st.pyplot(plt.gcf())
# value_2021 = data_2021['관객수'].sum()
# value_2022 = data_2022['관객수'].sum()
# total = value_2021 + value_2022  # 값의 합계 계산
# values = [value_2021, value_2022]
# labels = [f'2021년\n{value_2021:,}', f'2022년\n{value_2022:,}']
# colors = ['#FFD0D0', '#3AA6B9']
# fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='percent', marker=dict(colors=colors))])
# fig.update_layout(title='2021년 vs 2022년 TOP10 관객수 비교\n총 관객수: {:,}'.format(total))
# # Display the pie chart using Streamlit
# st.plotly_chart(fig)