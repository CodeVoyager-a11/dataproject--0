import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# 데이터 정의
data = {
    '연도': [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    '전체': [67.0, 67.5, 67.7, 66.2, 67.7, 67.1, 65.1, 67.7, 69.6, 70.3],
    '남자': [69.0, 69.0, 69.0, 67.8, 69.6, 69.0, 67.1, 69.5, 71.2, 72.4],
    '여자': [65.0, 66.0, 66.5, 64.8, 66.2, 65.3, 63.2, 65.8, 67.9, 68.5]
}

df = pd.DataFrame(data)
df.set_index('연도', inplace=True)

# 제목
st.title("대학졸업자 취업률 추이 (2014-2023)")

# Streamlit 기본 선그래프 사용
st.line_chart(df)
