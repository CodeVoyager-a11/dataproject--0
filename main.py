import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

## 데이터 정의
data = {
    '연도': [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    '남자': [69.0, 69.0, 69.0, 67.8, 69.6, 69.0, 67.1, 69.5, 71.2, 72.4],
    '여자': [65.0, 66.0, 66.5, 64.8, 66.2, 65.3, 63.2, 65.8, 67.9, 68.5]
}
df = pd.DataFrame(data)
df['남녀 평균'] = df[['남자', '여자']].mean(axis=1)
df.set_index('연도', inplace=True)

# 제목
st.title("대학졸업자 취업률 추이 (2014-2023)")

# 연도 슬라이더
min_year, max_year = st.slider(
    "연도 범위를 선택하세요:",
    min_value=2014,
    max_value=2023,
    value=(2014, 2023)
)

# 선택 가능한 항목
options = st.multiselect(
    "표시할 항목을 선택하세요:",
    options=['남자', '여자', '남녀 평균'],
    default=['남자', '여자', '남녀 평균']
)

# 데이터 필터링
filtered_df = df.loc[min_year:max_year, options]

# 그래프 출력
if filtered_df.empty:
    st.warning("하나 이상의 항목을 선택해주세요.")
else:
    st.line_chart(filtered_df)
