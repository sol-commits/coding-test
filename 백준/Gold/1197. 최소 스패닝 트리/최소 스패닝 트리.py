import sys
from collections import defaultdict
from heapq import heappop, heappush

# 프림의 시간 복잡도: O(E log V)
# 크루스칼의 시간 복잡도: O(E log E)
# 그래프 내에 간선이 많은 경우는 프림 알고리즘, 
# 간선이 적은 경우는 크루스칼 알고리즘이 유리
# 이 문제에서 V는 10,000, E는 100,000이므로 프림이 더 알맞음

def find(parent, vertex):
    while parent[vertex] != vertex:
        parent[vertex] = parent[parent[vertex]]  # 경로 압축
        vertex = parent[vertex]
    return vertex

def union(parent, v1, v2):
    parent_v1 = find(parent, v1)
    parent_v2 = find(parent, v2)
    
    if parent_v1 < parent_v2:
        parent[parent_v2] = parent_v1
    else:
        parent[parent_v1] = parent_v2

def solution(V, E, edges):
    """
    정점의 개수 V, 간선의 개수 E, 간선 정보 edges가 주어질 때,
    최소 스패닝 트리를 출력
    """
    edges.sort(key=lambda x: x[2])  # 비용으로 정렬
    parent = [i for i in range(V + 1)]  # 부모 노드 초기화
    mst = 0
    
    for edge in edges:
        v1, v2, cost = edge
        
        if find(parent, v1) != find(parent, v2):
            union(parent, v1, v2)
            mst += cost
    
    print(mst)
                    
if __name__ == "__main__":
    input = sys.stdin.readline
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]

    solution(V, E, edges)