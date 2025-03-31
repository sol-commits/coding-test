from collections import deque

def solution(maps):
    """
    - 동, 서, 남, 북 방향으로 한 칸씩 이동하며, 게임 맵을 벗어난 길은 갈 수 없음
    Args
        - maps: 2차원 배열
            - 1: 이동할 수 있는 칸
            - 0: 이동할 수 없는 칸
        - 시작점 (0, 0)에서 상대 팀 진영 (m-1, n-1)까지 최단 거리로 도착할 수 있는 칸의 개수
    Returns
        - 상대 팀 진영에 최단 거리로 도착할 수 있는 칸의 개수
        - 상대 팀 진영에 도착할 수 없는 경우 -1
    """
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    target = (len(maps) - 1, len(maps[0]) - 1)
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    queue = deque([(0, 0, 1)]) # (행, 열, 거리)
    visited[0][0] = True
    
    while queue:
        row, col, dist = queue.popleft()
        if (row, col) == target:
            return dist
        
        for move_row, move_col in moves:
            new_row, new_col = row + move_row, col + move_col
            if 0 <= new_row < len(maps) and 0 <= new_col < len(maps[0]) and not visited[new_row][new_col] and maps[new_row][new_col] == 1:
                visited[new_row][new_col] = True
                queue.append((new_row, new_col, dist + 1))
    
    return -1