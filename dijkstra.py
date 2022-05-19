#!/usr/bin/env python
# -*- coding: utf-8 -*-
import heapq
import sys

def dijkstra(start):
    # 초기 배열 설정, 최소 가중치(거리)들의 리스트이다.
    distances = {node: sys.maxsize for node in graph}
    # 시작 노드의 거리는 0으로 설정
    distances[start] = 0
    # priority queue
    queue = []
    # 시작 노드부터 탐색 시작 하기 위함. heapq 모듈은 첫번째 데이터를 기준으로 정렬하기 때문에 
    # 거리 값을 기준으로 정렬하기 위해 (거리, 노드) 순으로 queue에 저장한다.
    heapq.heappush(queue, (distances[start], start))

    # priority queue에 데이터가 하나도 없을 때까지 반복
    while queue:
        # 가장 낮은 거리를 가진 노드와 그 거리를 추출
        current_distance, node = heapq.heappop(queue)
        # 이미 계산되어 저장한 거리와 추출된 거리와 비교하여 저장된 거리가 더 작다면 비교하지 않고 
        # 큐의 다음 데이터로 넘어간다.
        if distances[node] < current_distance:
            continue

        # 대상인 노드에서 인접한 노드와 그 거리를 탐색한다.
        for adjacency_node, distance in graph[node].items():
            # 현재 노드에서 인접한 노드를 지나갈 때까지의 거리를 더하여 가중치로 저장한다.
            weighted_distance = current_distance + distance
            # 배열에 저장된 거리보다 위의 가중치가 더 작을 경우
            if weighted_distance < distances[adjacency_node]:
                # 배열에 저장된 거리를 더 작은 가중치의 값으로 변경
                distances[adjacency_node] = weighted_distance
                # 다음 인접 거리를 계산 하기 위해 해당 거리와 노드를 priority queue에 삽입 
                heapq.heappush(queue, (weighted_distance, adjacency_node))

    return distances

graph = {
    'A': {'B': 5, 'D':2, 'E':4},
    'B': {'C':3,'D':3},
    'C': {'E':4},
    'D': {'C':3 },
    'E': {'D':1},
}

result = dijkstra('A')
print(result)

# {'A': 0, 'B': 7, 'C': 3, 'D': 9, 'E': 5}