import sys

def solution(nums_len, nums):
    """
    nums 에서 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합
    
    1 <= nums_len <= 10^5
    -10^3 <= nums <= 10^3
    
    총 시간 복잡도: O(coin_types * target) = O(10^2 * 10^4) = O(10^6)
    핵심 아이디어: 완전 탐색인데, 중복 계산을 피한다. 
    """  
    dp = nums.copy()
    cur_max = nums[0]
    cur_max_idx = 0
    
    for idx in range(1, nums_len):
        dp[idx] += dp[idx - 1]
        
        while dp[idx] < nums[idx]:
            dp[idx] -= nums[cur_max_idx]
            cur_max_idx += 1
            
        cur_max = max(dp[idx], cur_max)
        
    return cur_max

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    nums = list(map(int, input().split()))

    print(solution(n, nums))
