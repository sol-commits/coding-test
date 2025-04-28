import sys

def rotate(shape):
    """90도 회전"""
    return [list(row) for row in zip(*shape[::-1])]

def reflect(shape):
    """좌우 대칭"""
    return [row[::-1] for row in shape]

def get_all_shapes(shape):
    shapes = []
    for _ in range(4):
        shape = rotate(shape)
        shapes.append(shape)
        shapes.append(reflect(shape))
    # 중복 제거
    unique = []
    for s in shapes:
        if s not in unique:
            unique.append(s)
    return unique

def solution(n, m, grid):
    """
    세로 n, 가로 m 
    테트로미노가 놓인 칸에 쓰여 있는 수들의 최댓값 반환
    """  
    tet = [
        [[1, 1, 1, 1]], 
        [[1, 1], [1, 1]],
        [[1, 0], [1, 0], [1, 1]],
        [[1, 0], [1, 1], [0, 1]],
        [[1, 1, 1], [0, 1, 0]]
        ]
    
    answer = 0
    for te in tet:
        for t in get_all_shapes(te):
            w, h = len(t[0]), len(t)
            for i in range(m):
                if i + w > m:
                    break
                for j in range(n):
                    if j + h > n:
                        break
                    answer = max(
                        sum(sum(grid[l][k] for l in range(j, j+h, 1) if t[l-j][k-i]) for k in range(i, i+w, 1)), 
                        answer)
    return answer
        
if __name__ == "__main__":
    input = sys.stdin.readline
    N, M = tuple(map(int, input().split()))
    grid = [list(map(int, input().split())) for _ in range(N)]
    print(solution(N, M, grid))