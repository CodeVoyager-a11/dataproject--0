import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium



# 연도 문자열로 처리
data = {
    '연도': ['2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023'],
    '남자': [69.0, 69.0, 69.0, 67.8, 69.6, 69.0, 67.1, 69.5, 71.2, 72.4],
    '여자': [65.0, 66.0, 66.5, 64.8, 66.2, 65.3, 63.2, 65.8, 67.9, 68.5]
}
df = pd.DataFrame(data)
df['남녀 평균'] = df[['남자', '여자']].mean(axis=1)
df = df.melt(id_vars='연도', var_name='성별', value_name='취업률')

# Streamlit UI
st.title("대학졸업자 취업률 추이 (2014-2023)")

selected_items = st.multiselect(
    "표시할 항목을 선택하세요:",
    options=df['성별'].unique().tolist(),
    default=['남자', '여자', '남녀 평균']
)

min_year, max_year = st.select_slider(
    "연도 범위를 선택하세요:",
    options=sorted(df['연도'].unique()),
    value=('2014', '2023')
)

# 필터링
filtered_df = df[
    (df['성별'].isin(selected_items)) &
    (df['연도'] >= min_year) & (df['연도'] <= max_year)
]

# Altair 차트
chart = alt.Chart(filtered_df).mark_line(point=True).encode(
    x=alt.X('연도:N', axis=alt.Axis(labelAngle=0)),  # 레이블을 0도로 회전 → 가로
    y='취업률:Q',
    color='성별:N'
).properties(width=700, height=400)

st.altair_chart(chart)

# 출처
st.caption("출처: 교육통계서비스 (KESS), 대학졸업자 취업통계")
