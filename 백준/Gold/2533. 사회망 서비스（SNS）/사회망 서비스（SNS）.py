import sys
from collections import defaultdict
import sys

sys.setrecursionlimit(10**6) 

def solution(nodes, edges):
    """
    얼리어답터가 아닌 node들은 자신의 모든 이웃들이 얼리어답터일 때만 아이디어를 받아드림
    모든 node가 새로운 아이디어를 받아들이기 위해 필요한 최소 얼리어답터의 수를 반환
    
    2 <= nodes <= 1,000,000
    
    총 시간 복잡도: O(10^6)
    핵심 아이디어: dfs, 
    """  
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # 각 노드마다 두 가지 상태를 저장 
    # status[node][0]: 노드가 얼리어답터인지 여부
    # status[node][1]: 노드의 자식 중 얼리어답터가 있는지 여부
    status = {i: [False, False] for i in range(1, nodes+1)}
    
    visited = [False] * (nodes + 1)
    
    def dfs(node):
        visited[node] = True
        
        # 현재 노드의 모든 인접 노드에 대해
        is_leaf = True
        for adj_node in graph[node]:
            is_leaf = False
            if not visited[adj_node]:
                dfs(adj_node)
                
            # 자식이 얼리어답터가 아니면, status[node][1] 업데이트
            if status[adj_node][0]:
                status[node][1] = True
        
        # 현재 노드의 자식 중 얼리어답터가 없다면, 현재 노드는 얼리어답터여야 함
        if not status[node][1]:
            status[node][0] = True
        
        # 리프 노드는 얼리어답터가 아니어도 됨
        if is_leaf:
            status[node][0] = False
            status[node][1] = False

    # 임의의 노드에서 시작
    dfs(1)
    
    return sum(status[i][1] for i in range(1, nodes + 1)) 
                
if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    edges = [list(map(int, input().split())) for _ in range(N - 1)]
    
    print(solution(N, edges))
