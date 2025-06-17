import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import altair as alt

# 데이터 설정
data = {
    '연도': ['2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023'],
    '남자': [69.0, 69.0, 69.0, 67.8, 69.6, 69.0, 67.1, 69.5, 71.2, 72.4],
    '여자': [65.0, 66.0, 66.5, 64.8, 66.2, 65.3, 63.2, 65.8, 67.9, 68.5]
}
df = pd.DataFrame(data)
df['성별 격차'] = df['남자'] - df['여자']

# 변화량 계산
df['작년 대비 변화'] = df['성별 격차'].diff().round(2)
df['다음해 대비 변화'] = df['성별 격차'].shift(-1) - df['성별 격차']
df['다음해 대비 변화'] = df['다음해 대비 변화'].round(2)

# 최대 증가/감소 포인트 계산
max_increase = df['작년 대비 변화'].max()
max_decrease = df['작년 대비 변화'].min()

# Streamlit UI
st.title("📊 성별 격차 변화 분석 (증가/감소 포인트 강조)")
selected_years = st.slider("연도 범위 선택", 2014, 2023, (2014, 2023))
start, end = str(selected_years[0]), str(selected_years[1])
filtered_df = df[(df['연도'] >= start) & (df['연도'] <= end)].copy()

# 기본 선 그래프
line = alt.Chart(filtered_df).mark_line(point=True, color='gray').encode(
    x=alt.X('연도:N', axis=alt.Axis(labelAngle=0)),
    y=alt.Y('성별 격차:Q', title='남자 - 여자 (%)'),
    tooltip=[
        alt.Tooltip('연도:N'),
        alt.Tooltip('성별 격차:Q', title='격차(%)'),
        alt.Tooltip('작년 대비 변화:Q', title='작년 대비 변화'),
        alt.Tooltip('다음해 대비 변화:Q', title='다음해 대비 변화')
    ]
)

# 최대 증가점 (빨간 점)
increase_point = alt.Chart(filtered_df[filtered_df['작년 대비 변화'] == max_increase]).mark_point(
    size=100, color='red'
).encode(x='연도:N', y='성별 격차:Q')

# 최대 감소점 (파란 점)
decrease_point = alt.Chart(filtered_df[filtered_df['작년 대비 변화'] == max_decrease]).mark_point(
    size=100, color='blue'
).encode(x='연도:N', y='성별 격차:Q')

# 결합
chart = (line + increase_point + decrease_point).properties(
    width=700,
    height=400,
    title="연도별 성별 격차 추이 (가장 많이 증가/감소한 해 강조)"
)

st.altair_chart(chart)

# 요약 정보
st.subheader("📌 격차 통계 요약")
st.markdown(f"""
- **가장 많이 증가한 해**: {df[df['작년 대비 변화'] == max_increase]['연도'].values[0]} (+{max_increase:.1f}%)  
- **가장 많이 감소한 해**: {df[df['작년 대비 변화'] == max_decrease]['연도'].values[0]} ({max_decrease:.1f}%)
""")

# 출처
st.caption("출처: 교육통계서비스 (KESS), 대학졸업자 취업통계")
