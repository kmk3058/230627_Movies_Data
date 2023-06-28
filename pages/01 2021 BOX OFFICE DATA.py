import streamlit as st
import common

common.page_config()
st.title("2021년 박스오피스 Data")
st.dataframe(common.get_2021(),
             use_container_width=True,
             hide_index=True)


# import streamlit as st
# # 탭 구성 요소 설정
# tab_names = ['Tab 1', 'Tab 2']
# active_tab = st.radio('Tabs', tab_names)
# # 첫 번째 탭의 내용
# if active_tab == 'Tab 1':
#     with st.beta_container():
#         st.write('This is Tab 1 content.')
#         # 여기에 탭 1의 내용을 추가하세요
# # 두 번째 탭의 내용
# elif active_tab == 'Tab 2':
#     with st.beta_container():
#         st.write('This is Tab 2 content.')
#         # 여기에 탭 2의 내용을 추가하세요