import sys
from collections import defaultdict

def solution(num_count, nums):
    """
    만들 수 있는 등식의 수를 반환

    3 <= num_count <= 100
    0 <= num <= 9
    
    총 시간 복잡도: 
    핵심 아이디어: 
    """ 
    dp = list([0] * 21 for _ in range(num_count))
    dp[0][nums[0]] = 1
    
    for idx in range(1, num_count - 1):
        
        for num, count in enumerate(dp[idx-1]):
            if num + nums[idx] <= 20:
                dp[idx][num + nums[idx]] += count
            if num - nums[idx] >= 0:
                dp[idx][num - nums[idx]] += count
            
    return dp[num_count-2][nums[-1]]

if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    nums = list(map(int, input().split()))
    
    print(solution(N, nums))
