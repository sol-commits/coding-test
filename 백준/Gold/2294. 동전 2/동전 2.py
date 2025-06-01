import sys

def solution(coin_types, target, coins):
    """
    coins 종류의 동전을 이용해서 그 가치의 합이 target원이 되도록 하는 동전 개수의 최솟값
    
    1 <= coin_types <- 100, 1 <= target <= 10,000
    1 <= coin a, b, c... <= 100,000
    
    22 = 15a + 5b + 4c + 3d
    dp[0] = -1, dp[1] = -1, dp[2] = -1, dp[3] = 1, dp[4] =1,
    dp[5] = 1, dp[6] = dp[3] + dp[3] = 2, dp[7] = dp[3] + dp[4] =2
    dp[8] = dp[5] + dp[3] = 2, dp[9] = dp[5] + dp[4] = 2
    dp[10] = dp[5] + dp[5], dp[11] = dp[8] + dp[3] = 3,
    dp[12] = dp[9] + dp[3] = 2 + 1 = 3, dp[13] = dp[10] + dp[3] = 
        
    총 시간 복잡도: O(coin_types * target) = O(10^2 * 10^4) = O(10^6)
    핵심 아이디어: 
    """  
    dp = [float('inf')] * (target + 1)
    dp[0] = 0
    
    for coin in coins:
        for num in range(coin, target + 1):
            dp[num] = min(dp[num], dp[num-coin] + 1)
            
    return -1 if dp[target] == float('inf') else dp[target]

if __name__ == "__main__":
    input = sys.stdin.readline
    n, k = list(map(int, input().split()))
    coins = list(set(int(input()) for _ in range(n)))

    print(solution(n, k, coins))
