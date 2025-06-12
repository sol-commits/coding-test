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
    # dp[i][remain] = 최소 제곱합 (i번째 사람까지 배치, 줄에 remain 칸 남음)
    dp = list([float('inf')] * col for _ in range(people_cnt))
    
    for idx, name_len in enumerate(name_lens):
        if idx == 0: # 첫번째 사람은 무조건 새 줄 시작
            remain = col - name_len
            dp[idx][remain] = remain ** 2
            continue
        
        for prev_remain, prev_calc in enumerate(dp[idx-1]):
            if dp[idx-1][prev_remain] == float('inf'): continue
            
            # 경우 1: 새 줄에 시작
            new_remain = col - name_len
            dp[idx][new_remain] = min(dp[idx][new_remain], prev_calc + new_remain ** 2)
            
            # 경우 2: 같은 줄에 이어서 배치 (공백 1칸 포함)
            if prev_remain > name_len:
                new_remain = prev_remain - name_len - 1
                dp[idx][new_remain] = min(dp[idx][new_remain], prev_calc - prev_remain**2 + new_remain**2)
                
    # 마지막 줄은 남는 칸을 계산하지 않으므로 마지막 사람까지 넣은 상태에서 remain 제곱값은 빼줌
    answer = float('inf')
    for remain, calc in enumerate(dp[people_cnt - 1]):
        answer = min(answer, calc - remain**2)

    return answer

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = tuple(map(int, input().split()))
    name_lens = [int(input()) for _ in range(n)]

    print(solution(n, m, name_lens))
