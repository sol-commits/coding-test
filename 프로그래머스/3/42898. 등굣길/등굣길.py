def temp(cur_row, cur_col, map, moves):
    if map[cur_row][cur_col] != 0:
        return map[cur_row][cur_col]
    for move_row, move_col in moves:
        next_row, next_col = cur_row + move_row, cur_col + move_col
        if 1 <= next_row < len(map) and 1 <= next_col < len(map[0]):
            if map[next_row][next_col] == -1:
                continue
            map[cur_row][cur_col] += temp(next_row, next_col, map, moves)
    
    return map[cur_row][cur_col]

def solution(m, n, puddles):
    """
    Args:
        - m: 가로길이, n: 세로길이
        - puddles: 물에 잠긴 지역의 좌표
    Returns:
        - 오른쪽과 아래쪽으로만 움직여 집에서 학교까지 갈 수 있는 최단경로의 개수 % 1000000007
    """
    map = [[0] * (m+1) for _ in range(n+1)]
    school_row, school_col = n, m
    home_row, home_col = 1, 1
    map[home_row][home_col] = 1
    
    for puddle_col, puddle_row in puddles:
        map[puddle_row][puddle_col] = -1
        
    moves = [(-1, 0), (0, -1)]
    temp(school_row, school_col, map, moves)

    # top down                
    return map[school_row][school_col]   % 1000000007