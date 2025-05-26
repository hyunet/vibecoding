import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import heapq


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


def app():
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

    st.subheader("다익스트라 최단 거리")
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
