import sys
from collections import defaultdict, deque

def solution(test_case):
    """
    test_case[target_building] 건설 완료하는데 드는 최소시간 출력
    """
    
    indegree = [0] * (test_case['building_num'] + 1)
    graph = defaultdict(list)
    
    for before_building, after_building in test_case['orders']:
        graph[before_building].append(after_building)
        indegree[after_building] += 1
    
    dp = [0] * (N + 1)
    q = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = test_case['cost'][i]
    
    while q:
        cur  = q.popleft()
        for next in graph[cur]:
            indegree[next] -= 1
            dp[next] = max(dp[next], dp[cur] + test_case['cost'][next])
            if indegree[next] == 0:
                q.append(next)
                
    return dp[test_case['target_building']]
                    
if __name__ == "__main__":
    input = sys.stdin.readline
    test_case_num = int(input())
    answer = []
    for i in range(test_case_num):
        test_case = {}
        N, K = map(int, input().split())
        test_case['building_num'] = N
        test_case['order_num'] = K
        test_case['cost'] = [0] + list(map(int, input().split()))
        test_case['orders'] = [list(map(int, input().split())) for _ in range(K)] # X -> Y
        test_case['target_building'] = int(input())
        answer.append(solution(test_case))
        
    print(*answer, sep='\n')