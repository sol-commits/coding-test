import sys
from collections import defaultdict

def solution(matrix_cnt, matrix):
    """ 
    모든 행렬을 곱하는데 필요한 곱셉 연산 횟수의 최솟값을 반환
    
    1 <= matrix_cnt <= 500
    1 <= matrix_r, matric_c <= 500
    
    총 시간 복잡도:  
    핵심 아이디어: 
    - 행렬은 결합법칙이 성립 (AB)C = A(BC)
    """ 
    # dp[i][j]: i~j까지 행렬을 곱하는 최소 비용
    dp = [[0] * matrix_cnt for _ in range(matrix_cnt)] 

    # 부분 문제의 길이를 2부터 시작해서 점차 늘려가며 해결
    for length in range(2, matrix_cnt + 1):  # length = 부분 행렬의 길이
        for i in range(matrix_cnt - length + 1):
            j = i + length - 1 # i부터 j까지가 하나의 구간
            dp[i][j] = float("inf")
            
            for k in range(i, j):
                # 비용 계산: 왼쪽 dp + 오른쪽 dp + 두 행렬 곱 비용
                cost = (
                    dp[i][k] +
                    dp[k + 1][j] +
                    matrix[i][0] * matrix[k][1] * matrix[j][1]
                )
                dp[i][j] = min(dp[i][j], cost)

    return dp[0][matrix_cnt - 1]

if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    rc = [list(map(int, input().split())) for _ in range(N)]

    print(solution(N, rc))
