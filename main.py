import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium


# 연도를 문자열로 지정
data = {
    '연도': ['2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023'],
    '남자': [69.0, 69.0, 69.0, 67.8, 69.6, 69.0, 67.1, 69.5, 71.2, 72.4],
    '여자': [65.0, 66.0, 66.5, 64.8, 66.2, 65.3, 63.2, 65.8, 67.9, 68.5]
}
df = pd.DataFrame(data)
df['남녀 평균'] = df[['남자', '여자']].mean(axis=1)
df.set_index('연도', inplace=True)

# 제목
st.title("대학졸업자 취업률 추이 (2014-2023)")

# 항목 선택
options = st.multiselect(
    "표시할 항목을 선택하세요:",
    options=['남자', '여자', '남녀 평균'],
    default=['남자', '여자', '남녀 평균']
)

# 연도 슬라이더를 문자열에 맞게 변환
years = df.index.tolist()
start_year, end_year = st.select_slider(
    "연도 범위를 선택하세요:",
    options=years,
    value=(years[0], years[-1])
)

# 데이터 필터링
filtered_df = df.loc[start_year:end_year, options]

# 그래프 출력
if filtered_df.empty:
    st.warning("하나 이상의 항목을 선택해주세요.")
else:
    st.line_chart(filtered_df)

    # 출처
    st.caption("출처: 교육통계서비스 (KESS), 대학졸업자 취업통계")
