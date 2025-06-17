import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import altair as alt

# 데이터 준비
data = {
    '연도': ['2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023'],
    '남자': [69.0, 69.0, 69.0, 67.8, 69.6, 69.0, 67.1, 69.5, 71.2, 72.4],
    '여자': [65.0, 66.0, 66.5, 64.8, 66.2, 65.3, 63.2, 65.8, 67.9, 68.5]
}
df = pd.DataFrame(data)
df['성별 격차'] = df['남자'] - df['여자']

# 격차 감소 여부 계산
df['격차 변화'] = df['성별 격차'].diff().fillna(0)
df['감소 여부'] = df['격차 변화'] < 0

# 최고/최저점 찾기
max_gap = df['성별 격차'].max()
min_gap = df['성별 격차'].min()

# 연도 필터링 슬라이더
st.title("📉 성별 격차 분석 (선그래프 + 주요 포인트 강조)")
selected_years = st.slider("분석할 연도 범위 선택", 2014, 2023, (2014, 2023))
start, end = str(selected_years[0]), str(selected_years[1])
filtered_df = df[(df['연도'] >= start) & (df['연도'] <= end)].copy()

# 기본 선그래프
line = alt.Chart(filtered_df).mark_line(point=True, color='gray').encode(
    x=alt.X('연도:N', axis=alt.Axis(labelAngle=0)),
    y=alt.Y('성별 격차:Q', title='남자 - 여자 (%)'),
    tooltip=['연도', '성별 격차']
)

# 격차 감소 연도에 ▼ 마커 추가
drops = filtered_df[filtered_df['감소 여부'] == True]
drop_points = alt.Chart(drops).mark_text(
    text='▼', color='green', dy=-15, size=18
).encode(
    x='연도:N',
    y='성별 격차:Q'
)

# 최고점 강조 (빨간 원)
max_point = alt.Chart(filtered_df[filtered_df['성별 격차'] == max_gap]).mark_point(
    color='red', size=100, shape='circle'
).encode(x='연도:N', y='성별 격차:Q')

# 최저점 강조 (파란 원)
min_point = alt.Chart(filtered_df[filtered_df['성별 격차'] == min_gap]).mark_point(
    color='blue', size=100, shape='circle'
).encode(x='연도:N', y='성별 격차:Q')

# 차트 결합
chart = (line + drop_points + max_point + min_point).properties(
    width=700,
    height=400,
    title="연도별 성별 취업률 격차 추이 (감소 연도 및 최고/최저점 강조)"
)

st.altair_chart(chart)

# 요약 통계
st.subheader("📌 격차 통계 요약")
st.markdown(f"""
- **최대 격차**: {max_gap:.1f}%  
- **최소 격차**: {min_gap:.1f}%  
- **격차가 감소한 연도 수**: {filtered_df['감소 여부'].sum()}회
""")

# 출처
st.caption("출처: 교육통계서비스 (KESS), 대학졸업자 취업통계")

