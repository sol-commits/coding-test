def solution(arr):
    """
    Args
    - arr: 문자열 형태의 숫자와 더하기 기호, 뺄셈 기호가 들어있는 배열 
    Returns
    - 서로 다른 연산순서의 계산 결과 중 최댓값
    """
    nums = []
    signs = [1]
    for num in arr:
        if num == "+":
            signs.append(1)
        elif num == "-":
            signs.append(-1)
        else:
            nums.append(int(num))
    
    max_dp = [[0] * len(nums) for _ in range(len(nums))]
    min_dp = [[0] * len(nums) for _ in range(len(nums))]
    for i in range(len(nums)):
        max_dp[i][i] = nums[i]
        min_dp[i][i] = nums[i]
                
    # bottom up
    for i in range(len(nums) - 2, -1, -1):
        for j in range(i + 1, len(nums)):
            max_val = float('-inf')  
            min_val = float('inf')
            for k in range(i, j):
                sign = signs[k+1]
                a, b, c, d = max_dp[i][k], min_dp[i][k], max_dp[k+1][j], min_dp[k+1][j]
                candidates = [a + sign*c, a + sign*d, b + sign*c, b + sign*d]
                max_val = max(max_val, *candidates)
                min_val = min(min_val, *candidates)
            max_dp[i][j] = max_val
            min_dp[i][j] = min_val
    return max_dp[0][-1]