import sys

def solution(T, paren_lens):
    """
    길이가 paren_len인 서로 다른 올바른 괄호 문자열의 개수를 반환
    
    1 <= T <= 100
    1 <= paren_len <= 5,000
    
    총 시간 복잡도: O(10^4)
    핵심 아이디어: 단순 A 입력 vs 복사 - 붙여넣기 중 더 큰 값을 선택
    """  
    dp = [0 for i in range(5000 + 1)]
    MOD = 1000000007
    dp[0] = 1
    
    for num in range(2, 5001, 2):
        for prev in range(2, num, 2):
            dp[num] = (dp[num] + dp[prev]*dp[num-prev-2]) % MOD
        dp[num] = (dp[num] + dp[num-2]) % MOD
    
    for paren_len in paren_lens:
        print(dp[paren_len])
        
if __name__ == "__main__":
    input = sys.stdin.readline
    T = int(input())
    paren_lens = [int(input()) for _ in range(T)]
    
    solution(T, paren_lens)
