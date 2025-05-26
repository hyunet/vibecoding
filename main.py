import streamlit as st
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import heapq

st.set_page_config(page_title="지속가능발전목표 기반 데이터 구조 프로젝트", layout="wide")

st.title("🌍 지속가능발전목표(SDG) 기반 데이터 구조 프로젝트")
st.markdown("---")

st.header("📌 프로젝트 개요")
st.write("""
이 프로젝트는 지속가능발전목표(SDG)를 달성하기 위한 데이터 기반 분석과 자료구조/알고리즘을 접목하여, 다양한 사회 문제의 해결 방안을 제시합니다. 아래의 사례들을 통해 데이터를 수집, 시각화하고, 효율적인 알고리즘 설계를 수행합니다.
""")

st.markdown("---")

# 사례 1: 트리 구조 기반 에너지 모니터링
st.subheader("1️⃣ 트리 구조 기반 에너지 모니터링")
st.write("""
에너지 소비 데이터를 트리 구조로 표현하여 지역별 사용 흐름을 분석하고, 불필요한 낭비를 줄이기 위한 구조를 설계합니다.
""")

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

st.text("에너지 소비 트리 구조")
display_tree("국가")

st.markdown("---")

# 사례 2: 그래프 구조 및 BFS + 다익스트라 알고리즘
st.subheader("2️⃣ 교통 흐름 분석: 그래프 + BFS + 다익스트라")
st.write("""
시간대별 교통량 데이터를 그래프 구조로 모델링하고, 너비 우선 탐색(BFS) 및 다익스트라 알고리즘으로 최적 경로 및 혼잡도 예측을 수행합니다.
""")

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
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=15)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
st.pyplot(plt.gcf())

st.write("#### 🔍 다익스트라 최단 거리 예시")
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if current_distance > distances[current_node]:
            continue
        for neighbor in graph[current_node]:
            weight = graph[current_node][neighbor].get('weight', 1)
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances

st.json(dijkstra(dict(G), 'A'))

st.markdown("---")

# 사례 3: 식량 소비 패턴 및 정렬
st.subheader("3️⃣ 식량 소비 패턴 분석: 정렬 알고리즘")
st.write("""
식량 소비 패턴 데이터를 기반으로 유통기한순으로 식품을 정렬하고, 빠른 검색을 위한 탐색 알고리즘을 적용합니다.
""")

food_data = [
    {"식품": "쌀", "유통기한": 10},
    {"식품": "라면", "유통기한": 3},
    {"식품": "통조림", "유통기한": 24},
    {"식품": "계란", "유통기한": 1}
]

st.write("#### 🗂 원본 데이터")
st.dataframe(pd.DataFrame(food_data))

st.write("#### ⏳ 유통기한 기준 정렬 결과 (머지 정렬)")
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
st.dataframe(pd.DataFrame(sorted_food))

st.markdown("---")

# 사례 4: 재난 피해 지역 지원 최적화
st.subheader("4️⃣ 재난 피해 최소화: 피해 규모 정렬 및 자원 분배")
st.write("""
피해 규모가 큰 지역을 우선 지원하기 위해 정렬 알고리즘을 활용하고, 자원 분배 알고리즘을 설계합니다.
""")

disaster_data = [
    {"지역": "X", "피해 규모": 80},
    {"지역": "Y", "피해 규모": 45},
    {"지역": "Z", "피해 규모": 95},
    {"지역": "W", "피해 규모": 30},
]
sorted_disaster = sorted(disaster_data, key=lambda x: -x["피해 규모"])
st.dataframe(pd.DataFrame(sorted_disaster))

st.markdown("---")

st.success("이 프로젝트는 다양한 문제 해결에 있어 자료구조 및 알고리즘의 실제적 활용 사례를 보여줍니다. 지속가능한 사회를 위한 데이터 과학 기반 접근 방식의 중요성을 강조합니다.")
