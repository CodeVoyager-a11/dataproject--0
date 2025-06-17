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

# 격차 계산
df['성별 격차'] = df['남자'] - df['여자']

# Streamlit UI
st.title("🎓 성별 격차 분석: 대학 졸업자 취업률 (2014~2023)")

# 연도 선택
selected_years = st.slider(
    "분석할 연도 범위 선택",
    min_value=2014, max_value=2023,
    value=(2014, 2023)
)

# 연도 필터링
start, end = str(selected_years[0]), str(selected_years[1])
filtered_df = df[(df['연도'] >= start) & (df['연도'] <= end)]

# Altair 그래프
chart = alt.Chart(filtered_df).mark_bar(color='#ff6961').encode(
    x=alt.X('연도:N', axis=alt.Axis(labelAngle=0)),
    y=alt.Y('성별 격차:Q', title='남자 - 여자 (%)'),
    tooltip=['연도', '성별 격차']
).properties(width=700, height=400)

st.altair_chart(chart)

# 주요 통계
max_gap = filtered_df['성별 격차'].max()
min_gap = filtered_df['성별 격차'].min()
avg_gap = round(filtered_df['성별 격차'].mean(), 2)

st.subheader("📌 성별 격차 요약")
st.markdown(f"""
- **최대 격차**: {max_gap:.1f}%  
- **최소 격차**: {min_gap:.1f}%  
- **평균 격차**: {avg_gap:.1f}%
""")

# 출처
st.caption("출처: 교육통계서비스 (KESS), 대학졸업자 취업통계")
