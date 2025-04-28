import sys
from collections import defaultdict, deque

def solution(v, e, start_v, edges):
    graph = defaultdict(list)
    for v1, v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    for key in graph.keys():
        graph[key].sort(reverse=True)
        
    visited = [False] * (v + 1)
    stack = [start_v]
    dfs = []
    
    while stack:
        cur_v = stack.pop()
        if visited[cur_v]:
            continue
        dfs.append(cur_v)
        visited[cur_v] = True
        for adjacent in graph[cur_v]:
            if not visited[adjacent]:    
                stack.append(adjacent)
                
    visited = [False] * (v + 1)
    q = deque([start_v])
    visited[start_v] = True
    bfs = [start_v]
    
    for key in graph.keys():
        graph[key].sort()
    
    while q:
        cur_v = q.popleft()
        visited[cur_v] = True
        for adjacent in graph[cur_v]:
            if not visited[adjacent]:
                q.append(adjacent)
                visited[adjacent] = True
                bfs.append(adjacent)
                
    print(" ".join(list(map(str, dfs))))
    print(" ".join(list(map(str, bfs))))
        
if __name__ == "__main__":
    input = sys.stdin.readline
    N, M, V = tuple(map(int, input().split()))
    graph = [list(map(int, input().split())) for _ in range(M)]
    solution(N, M, V, graph)