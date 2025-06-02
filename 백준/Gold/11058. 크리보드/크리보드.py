import sys

def solution(push_cnt):
    """
    크리보드 버튼을 총 push_cnt 번 눌러서 화면에 출력된 A 개수의 최댓값
    
    1 <= push_cnt <= 100
    
    총 시간 복잡도: 
    핵심 아이디어: 
    """  
    dp = [i for i in range(push_cnt + 1)]
    dp[0] = 0
    
    for i in range(1, push_cnt + 1):
        for j in range(i + 3, push_cnt + 1):
            dp[j] = max(dp[j], dp[i] * (j - i - 3 + 2))

    return dp[push_cnt]

if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())

    print(solution(N))
