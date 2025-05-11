import sys
from collections import defaultdict, deque

def solution(num_students, num_compares, compares):
    """
    compares: 일부 학생들의 키를 비교한 결과
    compares 예시 [[A,B]]: A가 B의 앞에 서야한다는 의미
    학생들을 앞에서부터 줄을 세운 결과를 반환
    
    1 <= num_students <= 32,000
    1 <= num_compares <= 100,000
    
    총 시간 복잡도: O(1,000,000)
    핵심 아이디어: 위상 정렬
    """  
    
    degrees = [0] * (num_students + 1)
    
    higher = defaultdict(list)
    for short, high in compares:
        if high in higher[short]:
            continue
        degrees[high] += 1
        higher[short].append(high)
    
    q = deque()
    for i in range(1, num_students + 1):
        if degrees[i] == 0:
            q.append(i)
    
    result = []
    while q:
        student = q.popleft()
        result.append(student)
        for high in higher[student]:
            degrees[high] -= 1
            if degrees[high] == 0:
                q.append(high)
    
    return result
    
if __name__ == "__main__":
    input = sys.stdin.readline
    N, M = list(map(int, input().split()))
    compares = [list(map(int, input().split())) for _ in range(M)]
    print(" ".join(list(map(str, solution(N, M, compares)))))
    