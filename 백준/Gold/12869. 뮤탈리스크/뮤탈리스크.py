import sys
from collections import defaultdict
from itertools import permutations

def solution(svc_count, svcs):
    """
    모든 svc를 파괴하기 위해 공격해야 하는 횟수의 최솟값

    1 <= svc_count <= 3,
    1 <= svc <= 60
    
    총 시간 복잡도: 
    핵심 아이디어: 
    """ 
    dp = defaultdict(set)
    
    dp[0].add(tuple(svcs))
    adds = set(permutations([-(3**(2-i)) for i in range(svc_count)], svc_count))
    answer = 0

    while True:
        for cand in dp[answer]:
            for idx in range(svc_count):
                if cand[idx] > 0:
                    break
                if idx == svc_count - 1:
                    return answer
            for add in adds:
                dp[answer + 1].add(tuple([cand[i] + add[i] for i in range(svc_count)]))
        answer += 1

if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    SVC = list(map(int, input().split()))
    
    print(solution(N, SVC))
