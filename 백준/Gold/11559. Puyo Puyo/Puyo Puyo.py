import sys
from collections import defaultdict

def in_field(cur_row, cur_col, h, w):
    if (0 <= cur_row < h) and (0 <= cur_col < w):
        return True
    return False

def find_puyo(h, w, stack):
    for i in range(h):
        for j in range(w):
            if field[i][j] != '.':
                stack.append(((i, j), (i, j)))

def solution(field):
    """
    field: 뿌요들이 전부 아래로 떨어진 뒤의 상태(12*6 이차원배열)
    R: 빨강, G: 초록, B: 파랑, P: 보라, Y: 노랑, .: 빈공간
    연쇄가 몇 번 연속으로 일어날지 반환
    - 같은 색 뿌요가 4개 이상 상하좌우로 연결되어 있으면 연결된 같은 색 뿌요들이 한꺼번에 없어짐(=1연쇄)
    - 터질 수 있는 뿌요가 여러 그룹이 있다면 동시에 터져야 하고 여러 그룹이 터지더라도 한번의 연쇄가 추가됨
    
    총 시간 복잡도: O(400^2 * 4 = 10^5)
    핵심 아이디어: bfs(최소 몇번)
    """  
    h, w = 12, 6
    moves = ((0, 1), (0, -1), (1, 0), (-1, 0))
    answer = 0
    
    while True:
        visited = set()
        stack = []
        routes = defaultdict(list)
        find_puyo(h, w, stack)
        
        if not stack:
            break

        while stack:
            loc, start_loc = stack.pop()
            
            if loc in visited:
                continue
            
            visited.add(loc)
            routes[start_loc].append(loc)
            
            for drow, dcol in moves:
                nrow, ncol = loc[0] + drow, loc[1] + dcol
                if in_field(nrow, ncol, h, w):
                    if (field[nrow][ncol] == field[loc[0]][loc[1]]) and ((nrow, ncol) not in visited):
                        stack.append(((nrow, ncol), start_loc))

        prev_answer = answer
        bomb = 0
        for route_list in routes.values():
            if len(route_list) >= 4:
                for row, col in route_list:
                    field[row][col] = ' '
                    bomb = 1
        answer += bomb
        if prev_answer == answer:
            return answer
            
        for j in range(w):
            for i in range(h):
                if field[i][j] == ' ': # 비어있다면 땡겨와야함
                    for k in range(i, 0, -1):
                        field[k][j] = field[k-1][j]
                    field[0][j] = '.'                
    return answer
if __name__ == "__main__":
    input = sys.stdin.readline
    field = list(list(input().rstrip('\n')) for _ in range(12))
    print(solution(field))
