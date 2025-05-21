import sys
from collections import deque

def in_cave(cave_row, cave_col, row, col):
    if (0 <= row < cave_row) and (0 <= col < cave_col):
        return True
    return False

def solution(cave_row, cave_col, cave, throw_num, throws):
    """
    모든 막대를 던지고 난 후 미네랄 모양을 구하는 프로그램
    
    1 <= cave_row, cave_col <= 100
    1 <= throw_num <= 100
    왼오오왼
    
    총 시간 복잡도: 
    핵심 아이디어: 중력 구현, bfs로 바닥에 붙어있는 클러스터들을 찾기
    """  
    adj = ((0, 1), (1, 0), (0, -1), (-1, 0))
    throw_vector = ((0, cave_col, 1), (cave_col-1, -1, -1)) # 왼오, 오왼
    vector_idx = 0
    
    for stick_height in throws:
        stick_row = cave_row - stick_height
        vector = throw_vector[vector_idx]
        for stick_col in range(vector[0], vector[1], vector[2]):
            if cave[stick_row][stick_col] == 'x': # 미네랄을 만나면
                cave[stick_row][stick_col] = '.' # 미네랄 제거
            
                visited = [[False] * cave_col for _ in range(cave_row)]
                for c in range(cave_col): # cave의 마지막행에서부터 시작해서 클러스터를 찾음
                    if visited[cave_row-1][c]: continue 
                    if cave[cave_row-1][c] == 'x':
                        q = deque([(cave_row-1, c)])
                        visited[cave_row-1][c] = True
                        while q:
                            loc = q.popleft()

                            for dr, dc in adj:
                                nr, nc = loc[0] + dr, loc[1] + dc
                                if in_cave(cave_row, cave_col, nr, nc):
                                    if visited[nr][nc]: continue
                                    if cave[nr][nc] == 'x':
                                        q.append((nr, nc))
                                        visited[nr][nc] = True
                targets = [] # 위에서 찾은 바닥과 연결된 클러스터가 아닌 공중에 떠있는 클러스터들을 찾음
                for i in range(cave_row):
                    for j in range(cave_col):
                        if (cave[i][j] == 'x') and not visited[i][j]:
                            targets.append((i, j))
                if targets:
                    # 열마다 가장 아래에 있는 미네랄만 추림
                    bottom_by_col = dict()
                    for r, c in targets:
                        if c not in bottom_by_col or r > bottom_by_col[c]:
                            bottom_by_col[c] = r

                    # 그 미네랄들만 기준으로 move_cnt 계산
                    move_cnt = cave_row
                    for c, r in bottom_by_col.items():
                        nr = r + 1
                        while nr < cave_row:
                            if cave[nr][c] == 'x':
                                break
                            nr += 1
                        move_cnt = min(move_cnt, nr - r - 1)
                    
                    for tr, tc in targets: # 공중에 떠있는 클러스터들 . 로 초기화
                        cave[tr][tc] = '.'
                    for tr, tc in targets:
                        cave[tr+move_cnt][tc] = 'x'
                        
                break
        
        vector_idx = 1 - vector_idx
        
    return cave
                        
                
if __name__ == "__main__":
    input = sys.stdin.readline
    R, C = map(int, input().split())
    cave = [list(input().rstrip('\n')) for _ in range(R)]
    N = int(input())
    throws = list(map(int, input().split()))
        
    result = solution(R, C, cave, N, throws)
    
    for r in result:
        print("".join(r))
