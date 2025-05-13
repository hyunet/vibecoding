import streamlit as st
import random

# MBTI와 추천 직업 매핑
mbti_jobs = {
    "INTJ": ["데이터 과학자 🚀", "전략 컨설턴트 🌎", "UX 디자이너 🖼️"],
    "INFP": ["작가 🌟", "심리상담사 🩵", "사회운동가 🌍"],
    "ENTP": ["기획자 📋", "창업가 🚀", "광고 크리에이터 🎬"],
    "ISFJ": ["교사 🏫", "간호사 🩽", "사회복지사 🚑"],
    "ESFP": ["이벤트 플래너 🎉", "방송인 🎥", "스타일리스트 💄"],
    "ISTP": ["엔지니어 🛠️", "파일럿 ✈️", "탐험가 🌍"],
    # 추가 MBTI
    "INFJ": ["상담가 🩵", "작가 📚", "기획자 📊"],
    "ESTJ": ["경영자 💼", "군인 💪", "프로젝트 매니저 📅"],
    "ENFP": ["마케터 📢", "강연가 🏛️", "콘텐츠 제작자 🎤"],
    "ISTJ": ["공무원 🏛️", "회계사 💳", "품질관리자 📈"],
    # 나머지도 추가 가능
}

# 페이지 제목 꾸미기
st.markdown("""
    <h1 style='text-align: center; color: #ff69b4;'>
        🌟 MBTI 지보 참조 사이트 🌟
    </h1>
    <h3 style='text-align: center; color: #f08080;'>
        당신의 계획에 참고가 되는 지보를 규칙없이 제시해요! 💬
    </h3>
""", unsafe_allow_html=True)

# 사용자 입력
mbti = st.selectbox("\ud83d\udca1 MBTI\ub97c \uc120\ud0dd\ud574\uc8fc세요:", list(mbti_jobs.keys()))

# 추천 직업 출력
if mbti:
    st.markdown("---")
    st.subheader(f"\ud83c\udf89 \"{mbti}\" 멤\ud2f0\ub514에 \uc815\ud574진 \ucc38고 \uc9c0보가 \uc774것이에요! \ud83c\udf1f")

    jobs = mbti_jobs.get(mbti, ["추천 지보가 없어요. ❌"])
    for job in jobs:
        st.markdown(f"- {job}")

    st.balloons()
    st.snow()

# 하단 장식
st.markdown("""
    <hr>
    <p style='text-align: center; color: #aaa;'>
        🌺 제작: <strong>MBTI Career Recommender</strong> | 🌼 프리 버전 프로필 사이트입니다. 
    </p>
""", unsafe_allow_html=True)
