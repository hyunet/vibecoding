import streamlit as st
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import heapq

st.set_page_config(page_title="SDGs 기반 정보과학 프로젝트", layout="wide")

PAGES = ["1. 에너지 효율 분석", "2. 교통 혼잡도 예측", "3. 식량 재고 관리"]
st.sidebar.title("🌱 SDGs 주제 선택")
page = st.sidebar.radio("페이지를 선택하세요", PAGES)

# 공통 함수: 다익스트라

def dijkstra_nx(graph: nx.Graph, start):
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0
    pq = [(0, start)]
    visited = set()
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if current_node in visited:
            continue
        visited.add(current_node)
        for neighbor in graph.neighbors(current_node):
            weight = graph.edges[current_node, neighbor].get('weight', 1)
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances

if page == PAGES[0]:
    st.title("🔌 SDG 7: 에너지 효율 분석")
    st.markdown("[데이터 출처: e-나라지표](https://www.index.go.kr/potal/main/EachDtlPageDetail.do?idx_cd=1428)")

    st.header("[데이터로 말하기] 트리 구조로 에너지 소비 시각화")
    energy_tree = {
        "국가": ["서울", "부산"],
        "서울": ["강남구", "마포구"],
        "부산": ["해운대구", "사하구"],
        "강남구": [],
        "마포구": [],
        "해운대구": [],
        "사하구": []
    }
    def display_tree(node, level=0):
        st.text("  " * level + "- " + node)
        for child in energy_tree.get(node, []):
            display_tree(child, level + 1)
    display_tree("국가")

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

elif page == PAGES[1]:
    st.title("🚦 SDG 11: 교통 혼잡도 예측")
    st.markdown("[데이터 출처: 공공데이터포털](https://www.data.go.kr/data/15070252/fileData.do)")

    st.header("[데이터로 말하기] 그래프 구조 시각화 및 다익스트라")
    G = nx.Graph()
    edges = [
        ("A", "B", 3),
        ("B", "C", 2),
        ("A", "D", 1),
        ("D", "C", 4),
        ("C", "E", 1),
    ]
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=2000)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    st.pyplot(plt.gcf())
    st.json(dijkstra_nx(G, 'A'))

    st.header("[데이터로 읽기] 인사이트 3가지")
    st.markdown("""
    1. C 지점은 최단 경로의 교차점으로 혼잡도가 집중됨
    2. A에서 E까지 가장 빠른 경로는 B와 C를 거침
    3. 다익스트라 알고리즘을 통해 교통 병목 예측 가능
    """)

    st.header("[데이터로 쓰기] 문제 해결 구조화")
    st.markdown("""
    - 교통 노드를 그래프로 설계
    - BFS로 전체 흐름 탐색 후 혼잡 지점 사전 파악
    - 다익스트라 알고리즘 기반 시간대별 우회 경로 제공 시스템 구현
    """)

elif page == PAGES[2]:
    st.title("🍽️ SDG 12: 식량 재고 관리")
    st.markdown("[데이터 출처: 기상자료개방포털](https://data.kma.go.kr/climate/RankState/selectRankStatisticsDivision.do?pgmNo=70)")

    st.header("[데이터로 말하기] 정렬 알고리즘 시각화")
    food_data = [
        {"식품": "쌀", "유통기한": 10},
        {"식품": "라면", "유통기한": 3},
        {"식품": "통조림", "유통기한": 24},
        {"식품": "계란", "유통기한": 1}
    ]
    df_food = pd.DataFrame(food_data)
    st.dataframe(df_food)

    def merge_sort(data):
        if len(data) <= 1:
            return data
        mid = len(data) // 2
        left = merge_sort(data[:mid])
        right = merge_sort(data[mid:])
        return merge(left, right)

    def merge(left, right):
        result = []
        while left and right:
            if left[0]['유통기한'] < right[0]['유통기한']:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        result += left + right
        return result

    sorted_food = merge_sort(food_data.copy())
    st.subheader("정렬 결과 (머지 정렬)")
    st.dataframe(pd.DataFrame(sorted_food))

    st.header("[데이터로 읽기] 인사이트 3가지")
    st.markdown("""
    1. 유통기한이 짧은 식품이 재고 순환의 핵심
    2. 빠른 정렬로 식품 유실 방지 가능
    3. 재난 상황 시 긴급 식량 분배 우선순위 지정 가능
    """)

    st.header("[데이터로 쓰기] 문제 해결 구조화")
    st.markdown("""
    - 정렬 알고리즘으로 유통기한순 정리
    - 스택 구조로 폐기 전 품목 추적
    - 이진 탐색으로 필요한 품목 빠르게 조회 가능
    """)
