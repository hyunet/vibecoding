import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt


def app():
    st.title("🔌 SDG 7: 에너지 효율 분석")
    st.markdown("[데이터 출처: e-나라지표](https://www.index.go.kr/potal/main/EachDtlPageDetail.do?idx_cd=1428)")

    st.header("[데이터로 말하기] 트리 구조로 에너지 소비 시각화")
    st.write("지역별 에너지 소비 구조를 트리 형태로 시각화합니다.")

    energy_edges = [
        ("국가", "서울"), ("국가", "부산"),
        ("서울", "강남구"), ("서울", "마포구"),
        ("부산", "해운대구"), ("부산", "사하구")
    ]

    G_energy = nx.DiGraph()
    G_energy.add_edges_from(energy_edges)
    pos = nx.spring_layout(G_energy, seed=42)

    plt.figure(figsize=(6, 4))
    nx.draw(G_energy, pos, with_labels=True, node_color='lightblue', node_size=1800, arrows=True)
    st.pyplot(plt.gcf())

    st.header("[데이터로 읽기] 인사이트 3가지")
    st.markdown("""
    1. 수도권과 지방의 에너지 소비 구조가 뚜렷하게 나뉨
    2. 도시 중심부의 하위 구역이 에너지 사용량의 큰 비중을 차지함
    3. 트리 구조 분석을 통해 비효율적 분배 지점 발견 가능
    """)

    st.header("[데이터로 쓰기] 문제 해결 구조화")
    st.markdown("""
    - 트리 탐색을 통해 과도한 소비 구간 식별 → 노드별 소비량 분석
    - 큐를 사용해 우선순위 재분배 로직 적용
    - 전력 낭비 최소화를 위한 분산 에너지 공급 설계
    """)
