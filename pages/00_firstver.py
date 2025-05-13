import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests

# 페이지 기본 설정
st.set_page_config(page_title="데이터로 말하기", layout="wide")

# 스타일 적용
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR&display=swap');
        html, body, [class*="css"]  {
            font-family: 'Noto Sans KR', sans-serif;
        }
        h1, h2, h3 {
            color: #2C3E50;
        }
    </style>
""", unsafe_allow_html=True)

# 제목 출력
st.title("📊 데이터로 말하기")
st.markdown("""
### 공공데이터를 통해 세상을 읽는 시각을 기릅시다.
이 페이지는 공공 데이터를 수집하고, 정리하고, 시각화하여 정보를 직관적으로 이해할 수 있도록 도와줍니다.
""")

# 데이터 선택 옵션
st.sidebar.header("🔎 데이터 선택")
data_source = st.sidebar.selectbox("공공 데이터 예시 선택:", (
    "코로나19 확진자 현황 (질병청 API)",
    "서울시 미세먼지 데이터 (CSV 예시)",
))

# 데이터 불러오기 및 처리
if data_source == "코로나19 확진자 현황 (질병청 API)":
    st.subheader("🦠 코로나19 확진자 수 (예시 데이터)")

    # 예시 JSON 형태로 가정
    sample_data = {
        'date': pd.date_range(start='2024-01-01', periods=7),
        'cases': [1523, 1892, 1734, 1420, 1587, 1990, 2104]
    }
    df = pd.DataFrame(sample_data)
    
    st.line_chart(df.set_index('date'))
    st.dataframe(df)

elif data_source == "서울시 미세먼지 데이터 (CSV 예시)":
    st.subheader("🌫️ 서울시 미세먼지 농도 (예시 데이터)")

    # 샘플 데이터프레임
    df = pd.DataFrame({
        '구': ['강남구', '종로구', '송파구', '영등포구', '마포구'],
        'PM10': [55, 40, 70, 60, 65],
        'PM2.5': [28, 21, 33, 30, 27]
    })

    fig, ax = plt.subplots()
    df.plot(kind='bar', x='구', y=['PM10', 'PM2.5'], ax=ax)
    ax.set_ylabel('농도 (㎍/㎥)')
    st.pyplot(fig)
    st.dataframe(df)

# 하단 정보
st.markdown("""
    <hr>
    <p style='text-align: center; color: gray;'>
        📘 본 앱은 교육용 목적으로 제작되었으며, 실제 공공 API 연결 및 확장은 자유롭게 추가 개발 가능합니다.
    </p>
""", unsafe_allow_html=True)
