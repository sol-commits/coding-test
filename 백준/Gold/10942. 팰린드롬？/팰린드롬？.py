import sys

def solution(nums_len, nums, questions_len, questions):
    dp = [[0] * nums_len for _ in range(nums_len)]
    
    # 길이 1인 경우 (항상 팰린드롬)
    for i in range(nums_len):
        dp[i][i] = 1
    
    # 길이 2인 경우 (두 수가 같을 때만 팰린드롬)
    for i in range(nums_len-1):
        if nums[i] == nums[i+1]:
            dp[i][i+1] = 1
    
    # 길이 3 이상인 경우 (점화식 적용)
    for length in range(3, nums_len+1):
        for i in range(nums_len - length + 1):
            j = i + length - 1
            if nums[i] == nums[j] and dp[i+1][j-1]:
                dp[i][j] = 1
    
    # 질문 처리
    for s, e in questions:
        print(dp[s-1][e-1])

if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    nums = list(map(int, input().split()))
    M = int(input())
    SE = [list(map(int, input().split())) for _ in range(M)]
    solution(N, nums, M, SE)
