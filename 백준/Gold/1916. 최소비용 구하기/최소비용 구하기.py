import sys
from heapq import heappush, heappop
from collections import defaultdict

def solution(nums_city, nums_bus, bus_map, start, end):
    """
    nums_city: 도시의 개수, nums_bus: 버스의 개수
    bus_map: 출발 도시, 도착지 도시, 버스 비용
    start 부터 end 도시까지 가는데 드는 비용의 최소 비용을 반환
    
    1 <= nums_city <= 1,000
    1 <= nums_bus <= 100,000
    0 <= 버스 비용 < 100,000
    
    총 시간 복잡도: 벨만포드 O(10^3 * 10^5) = O(10^8), 다익스트라
    핵심 아이디어: 다익스트라, 벨만-포드 최단 거리 구하기
    """  
    graph = defaultdict(list)
    for u, v, dist in bus_map:
        graph[u].append((v, dist))
    
    
    distance = [float('inf')] * (nums_city + 1)
    distance[start] = 0
    pq = [(0, start)]

    while pq:
        dist, now = heappop(pq)
        if distance[now] < dist:
            continue
        for nxt, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[nxt]:
                distance[nxt] = new_cost
                heappush(pq, (new_cost, nxt))
    
    return distance[end]

if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    M = int(input())
    bus_map = [list(map(int, input().split())) for _ in range(M)]
    start, end = list(map(int, input().split()))
    print(solution(N, M, bus_map, start, end))
    