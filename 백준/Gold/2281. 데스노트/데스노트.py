import sys
from collections import defaultdict

def solution(people_cnt, col, name_lens):
    """ 
    각 줄의 끝에 사용하지 않고 남게 되는 칸의 수의 제곱의 합이 최소가 되도록
    -> 남게 되는 칸 수의 제곱의 합의 최솟값을 반환
    마지막 줄은 계산하지 않음
    
    1 <= people_cnt <= 10^3
    1 <= col, name_len <= 10^3   
    
    총 시간 복잡도: 
    핵심 아이디어: 
    """ 
    # 1에서 짤렸을 때
    # 2에서 짤렸을 때
    # 3에서 짤렸을 때
    dp = defaultdict(dict)
    
    for idx, name_len in enumerate(name_lens):
        if idx == 0:
            dp[idx][col-name_len] = (col - name_len) ** 2
            continue
        for key, value in dp[idx-1].items():
            dp[idx][col-name_len] = min(dp[idx].get(col-name_len, float('inf')), value + (col - name_len) ** 2)
            if key > name_len:
                temp = key-name_len-1
                dp[idx][temp] = min(dp[idx].get(temp, float('inf')), value - key**2 + temp**2)
                
    answer = float('inf')
    for key, value in dp[people_cnt - 1].items():
        answer = min(answer, value - key**2)

    return answer

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = tuple(map(int, input().split()))
    name_lens = [int(input()) for _ in range(n)]

    print(solution(n, m, name_lens))
