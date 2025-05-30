import sys
from collections import defaultdict

def solution(num):
    """
    1, 2, 3의 합으로 num을 나타내는 방법의 수를 반환
    
    1 <= num <- 10,000
    
    총 시간 복잡도: 
    핵심 아이디어: 
    """  
    dp = [0] * (num + 1)
    dp[0] = 1
    
    for n in [1, 2, 3]:             # 사용할 수 있는 숫자
        for i in range(n, num + 1):   # 만들 수 있는 수 i
            dp[i] += dp[i - n]
    
    return dp[num]

if __name__ == "__main__":
    input = sys.stdin.readline
    T = int(input())
    nums = [int(input()) for _ in range(T)]

    answers = []
    for num in nums:
        answers.append(solution(num))
    
    for a in answers:
        print(a)
