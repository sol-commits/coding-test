import sys
from collections import defaultdict

def solution(item_count, max_weight, items):
    """
    items = [[물건의 무게, 물건의 가치], ...]
    배낭에 넣을 수 있는 물건들의 가치의 최댓값

    1 <= item_count <= 10^2, 1 <= max_weight <= 10^5
    1 <= 물건 무게 <= 10^5, 0 <= 물건 가치 <= 10^3
    
    총 시간 복잡도: 
    핵심 아이디어: 
    """ 
    # dp[i][w]는 i번째 물건까지 고려했을 때, 무게 w로 담을 수 있는 최대 가치
    dp = [[0] * (max_weight + 1) for _ in range(item_count + 1)]

    for i in range(1, item_count + 1):
        weight, value = items[i - 1] # 현재 물건의 무게와 가치
        for w in range(max_weight + 1):
            if w < weight:
                # 현재 물건을 담지 못하는 경우 -> 이전 결과 그대로 사용
                dp[i][w] = dp[i - 1][w]
            else:
                # 담지 않는 경우 vs 담는 경우 중 최대 가치 선택
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
                
    # 마지막 물건까지 고려했을 때, 무게 max_weight로 담을 수 있는 최대 가치 반환
    return dp[item_count][max_weight]

if __name__ == "__main__":
    input = sys.stdin.readline
    N, K = list(map(int, input().split()))
    info = [list(map(int, input().split())) for _ in range(N)]
    
    print(solution(N, K, info))
