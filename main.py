# main.py
import streamlit as st
from pages import sdg7_energy, sdg11_traffic, sdg12_food
 
st.set_page_config(page_title="SDGs 기반 정보과학 프로젝트", layout="wide")

PAGES = {
    "1. 에너지 효율 분석 (SDG 7)": sdg7_energy,
    "2. 교통 혼잡도 예측 (SDG 11)": sdg11_traffic,
    "3. 식량 재고 관리 (SDG 12)": sdg12_food
}

st.sidebar.title("🌱 SDGs 주제 선택")
selection = st.sidebar.radio("페이지를 선택하세요", list(PAGES.keys()))

# 선택된 페이지 실행
page_function = PAGES[selection]
page_function.app()
