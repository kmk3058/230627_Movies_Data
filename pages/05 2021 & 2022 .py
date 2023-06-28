import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import common

common.page_config()

st.title("2021/2022 BoxOffice Comparison Analysis")

df_2021 = common.get_2021()
df_2022 = common.get_2022()

tab1, tab2= st.tabs(["Country", "Genre"])

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


tab3, tab4= st.tabs(["pie1", "pie2"])

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
    layout = go.Layout(title='2021년 국가별 영화 관객수')

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
    layout = go.Layout(title='2022년 국가별 영화 관객수')

    # 그래프 생성
    fig = go.Figure(data=data, layout=layout)

    # Streamlit에서 그래프 출력
    st.plotly_chart(fig)


gc_2021 = df_2021.loc[:,'대표장르'].value_counts()
gc_2022 = df_2022.loc[:,'대표장르'].value_counts()
tab_menus = ["2021", "2022"]
tab5, tab6 = st.tabs(tab_menus)
with tab5:
    from pywaffle import Waffle

    gc_2021_modified = {}

    for key, value in gc_2021.items():
        gc_2021_modified[key] = value // 20
    fig = plt.figure(
        FigureClass=Waffle,
        plots={
            111: {
                'values': gc_2021_modified,
                'labels': ["{0} ({1})".format(n, v) for n, v in gc_2021.items()],
                'legend': {'loc': 'upper left', 'bbox_to_anchor': (1, 1), 'fontsize': 8},
                'title': {'label': '2021 장르 (20개당 별 하나)', 'loc': 'left', 'fontproperties' : fontprop}
            }
        },
        rows=15,
        figsize=(15, 5),
        font_size=15,
        icons ='star'
    )
    plt.show()
    st.pyplot(fig)

with tab6:
    from pywaffle import Waffle

    gc_2022_modified = {}
    for key, value in gc_2022.items():
        gc_2022_modified[key] = value // 20
    fig = plt.figure(
        FigureClass=Waffle,
        plots={
            111: {
                'values': gc_2022_modified,
                'labels': ["{0} ({1})".format(n, v) for n, v in gc_2022.items()],
                'legend': {'loc': 'upper left', 'bbox_to_anchor': (1, 1), 'fontsize': 8},
                'title': {'label': '2022 장르 (20개당 별 하나)', 'loc': 'left', 'fontproperties' : fontprop}
            }
        },
        rows=15,
        figsize=(15, 5),
        font_size=15,
        icons='star'
    )
    plt.show()
    st.pyplot(fig)