import heapq
from collections import defaultdict

def dijkstra(start, graph, n):
    distance = [float('inf')] * (n + 1)
    distance[start] = 0
    pq = [(0, start)]

    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue
        for next in graph[now]:
            new_cost = dist + 1
            if new_cost < distance[next]:
                distance[next] = new_cost
                heapq.heappush(pq, (new_cost, next))
                
    return distance

def solution(n, edge):
    """
    노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex
    1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지 반환
    """
    graph = defaultdict(list)
    for u, v in edge:
        graph[u].append((v))
        graph[v].append((u))
    
    distance = dijkstra(1, graph, n)
    max_distance = max(distance[1:])
    
    return sum(1 for d in distance if d == max_distance)