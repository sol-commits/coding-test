import sys

def solution(N, k):
    """
    N x N 배열 A를 일차원 배열 B에 넣고 오름차순으로 정렬 -> B[k] 출력
    """
    
    start, end = 1, N * N
    answer = 0
    
    while start <= end:
        mid = (start + end) // 2
        
        total = sum(min(mid//i, N) for i in range(1, N + 1))
        
        if total < k:
            start = mid + 1
        elif total >= k:
            end = mid - 1
            answer = mid
    
    print(answer)
                    
if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    k = int(input())

    solution(N, k)