import sys

def solution(N, cables):
    """
    cables를 이용하여 똑같은 길이의 랜선 N개를 만드는 문제
    N개를 만들 수 있는 랜선의 최대 길이를 출력
    """
    cables.sort()
    start, end = 1, cables[-1]
    answer = 0
    
    while start <= end:
        mid = (start + end) // 2
    
        total = sum(cable // mid for cable in cables)
        
        if total >= N:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    
    print(answer)
        
    
if __name__ == "__main__":
    input = sys.stdin.readline
    K, N = map(int, input().split())
    cables = [int(input()) for _ in range(K)]

    solution(N, cables)