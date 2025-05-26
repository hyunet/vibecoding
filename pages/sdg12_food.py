import streamlit as st
import pandas as pd


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


def app():
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
    st.subheader("원본 데이터")
    st.dataframe(df_food)

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
