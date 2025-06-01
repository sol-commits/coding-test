import sys

def solution(nums_len, nums):
    """
    nums 에서 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합
    
    1 <= nums_len <= 10^5
    -10^3 <= nums <= 10^3
    
    총 시간 복잡도: O(10^5)
    핵심 아이디어: 이전까지의 최대 연속합에 현재 값을 더하는 것이 이득이 되는지?
    아니면 새로 시작하는 것이 더 나은지?
    """  
    dp = [0] * nums_len
    dp[0] = nums[0]
    max_sum = dp[0]
    
    for idx in range(1, nums_len):
        dp[idx] = max(dp[idx - 1] + nums[idx], nums[idx])
        max_sum = max(max_sum, dp[idx])
        
    return max_sum

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    nums = list(map(int, input().split()))

    print(solution(n, nums))
