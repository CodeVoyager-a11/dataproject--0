
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 정의
data = {
    '연도': [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    '전체': [67.0, 67.5, 67.7, 66.2, 67.7, 67.1, 65.1, 67.7, 69.6, 70.3],
    '남자': [69.0, 69.0, 69.0, 67.8, 69.6, 69.0, 67.1, 69.5, 71.2, 72.4],
    '여자': [None]*10  # 여학생 데이터가 남학생과 바뀐 것으로 보여 보완 가능
}
df = pd.DataFrame(data)

# 제목
st.title("대학졸업자 취업률 추이 (2014-2023)")

# 라인 그래프
st.subheader("취업률 선그래프")
fig, ax = plt.subplots()
ax.plot(df['연도'], df['전체'], marker='o', label='전체')
ax.plot(df['연도'], df['남자'], marker='s', label='남자')
ax.plot(df['연도'], df['여자'], marker='^', label='여자')
ax.set_xlabel("연도")
ax.set_ylabel("취업률 (%)")
ax.set_title("대학졸업자 취업률")
ax.legend()
st.pyplot(fig)
