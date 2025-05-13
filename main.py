import streamlit as st
import random 
import time
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR&display=swap');

        html, body, [class*="css"]  {
            font-family: 'Noto Sans KR', sans-serif;
        }
    </style>
""", unsafe_allow_html=True)

# MBTI와 추천 직업, 과목, 학과, 학습 팁 매핑
career_data = {
    "INTJ": {
        "jobs": ["데이터 과학자 🚀", "전략 컨설턴트 🌎", "UX 디자이너 🖼️"],
        "subjects": ["수학Ⅰ/Ⅱ", "확률과 통계", "정보", "융합과학"],
        "majors": ["컴퓨터공학과", "산업공학과", "디자인학과"],
        "tips": "계획을 세우고 혼자 깊이 있게 탐구하는 학습 방식이 잘 맞아요. 구조화된 개념 정리 노트를 만들어보세요."
    },
    "INFP": {
        "jobs": ["작가 🌟", "심리상담사 🩵", "사회운동가 🌍"],
        "subjects": ["문학", "심리학", "윤리와 사상", "언어와 매체"],
        "majors": ["심리학과", "문예창작과", "사회복지학과"],
        "tips": "감정과 직관에 의존하는 편이라 글쓰기나 토론을 통한 표현 학습이 좋아요. 목표를 시각화해보는 것도 도움이 됩니다."
    },
    "ENTP": {
        "jobs": ["기획자 📋", "창업가 🚀", "광고 크리에이터 🎬"],
        "subjects": ["경제", "정치와 법", "미디어와 표현", "창의적 체험활동"],
        "majors": ["경영학과", "광고홍보학과", "창업학과"],
        "tips": "새로운 아이디어를 실현하는 데 강하므로 프로젝트 기반 학습과 발표활동이 매우 효과적입니다."
    },
    # 다른 MBTI도 동일하게 확장 가능
}

# 페이지 제목 꾸미기
st.markdown("""
    <h1 style='text-align: center; color: #ff69b4;'>
        🌟 MBTI 기반 진로·과목 추천 시스템 🌟
    </h1>
    <h4 style='text-align: center; color: #f08080;'>
        당신의 MBTI에 맞는 직업, 선택과목, 관련 학과, 공부법을 알려드려요! 🎓
    </h4>
""", unsafe_allow_html=True)

# 사용자 입력
mbti = st.selectbox("💡 MBTI를 선택해주세요:", list(career_data.keys()))

# 결과 출력
if mbti:
    with st.spinner("✨ 당신에게 딱 맞는 진로 정보를 불러오고 있어요..."):
        time.sleep(1.5)

    st.success("🔍 추천 정보 도착!")
    st.markdown("---")
    st.subheader(f"🎉 \"{mbti}\" 유형에 맞는 진로 정보입니다!")

    data = career_data.get(mbti)
    if data:
        st.markdown("#### 💼 추천 직업")
        for job in data["jobs"]:
            st.markdown(f"- {job}")

        st.markdown("#### 📚 추천 선택 과목")
        st.markdown(", ".join(data["subjects"]))

        st.markdown("#### 🎓 관련 대학 학과")
        st.markdown(", ".join(data["majors"]))

        st.markdown("#### 🧠 학습 팁")
        st.info(data["tips"])

        st.balloons()
        st.toast("모든 추천 정보를 확인했어요! 🌟")

# 하단 정보
st.markdown("""
    <hr>
    <p style='text-align: center; color: #aaa;'>
        🌺 제작: <strong>MBTI Career Recommender+</strong> | 고등학생을 위한 맞춤 진로 탐색 도우미 💡
    </p>
""", unsafe_allow_html=True)
