import sys
from collections import defaultdict, deque

def solution(nodes_num, edges_num, edges):
    """
    edges: [[A, B], ...] -> A 에서 B로 물이 흐른다는 뜻 
    노드로 들어오는 강의 순서 중 가장 큰 값을 i라면, 
    들어오는 모든 강 중에서 순서 i인 값이 하나면 i, 두 개 이상이면 i+1
    이 하천계의 순서를 구하라
    
    2 <= nodes_num <= 1000
    1 <= A, B <= M 
    - M 은 항상 바다와 만나는 노드
    
    총 시간 복잡도: while True 루프 횟수 x O(h^2 x w) = O(h^3 x w^2) = 62,000
    핵심 아이디어: 위상 정렬
    """  
    
    order = [0] * (nodes_num + 1)
    indegrees = [0] * (nodes_num + 1)
    
    candidates = defaultdict(list)
    graph = defaultdict(list)
    for from_node, to_node in edges:
        graph[from_node].append(to_node)
        indegrees[to_node] += 1 
        
    q = deque([(node, 1) for node in range(1, nodes_num) if indegrees[node] == 0])
    
    while q:
        node, node_order = q.popleft()
        order[node] = node_order
        
        for adj in graph[node]:
            indegrees[adj] -= 1
            candidates[adj].append(node_order)
            if indegrees[adj] == 0:
                candidates[adj].sort(key = lambda key: -key)
                temp = (adj, candidates[adj][0])
                if len(candidates[adj]) >= 2:
                    if candidates[adj][0] == candidates[adj][1]:
                        temp = (adj, candidates[adj][0] + 1)
                q.append(temp)

    return order[nodes_num]
        
if __name__ == "__main__":
    input = sys.stdin.readline
    T = int(input())
    solutions = []
    for _ in range(T):
        K, M, P = list(map(int, input().split()))
        nodes = [list(map(int, input().split())) for _ in range(P)]
        solutions.append((K, solution(M, P, nodes)))
        
    for sol in solutions:
        print(sol[0], sol[1])
