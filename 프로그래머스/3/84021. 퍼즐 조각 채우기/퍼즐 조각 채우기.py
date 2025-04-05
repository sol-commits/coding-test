from collections import defaultdict

def dfs(map, moves, n, cur_row, cur_col, routes):
    routes.append((cur_row, cur_col))
    for move_row, move_col in moves:
        new_row, new_col = cur_row + move_row, cur_col + move_col
        if 0 <= new_row < n and 0 <= new_col < n:
            if map[new_row][new_col] == 1 and (new_row, new_col) not in routes:
                dfs(map, moves, n, new_row, new_col, routes)    

def get_puzzle(map, routes, is_game_board=False):
    # 행과 열의 범위 계산
    row1, row2 = min(r[0] for r in routes), max(r[0] for r in routes)
    col1, col2 = min(r[1] for r in routes), max(r[1] for r in routes)
    
    # 퍼즐 조각 추출 
    origin_puzzle = [[0]*(col2 - col1 + 1) for _ in range(row2 - row1 + 1)]
    for row, col in routes:
        origin_puzzle[row - row1][col - col1] = 1
        map[row][col] = 0

    if not is_game_board:
        puzzle_rotations = [origin_puzzle]
        for _ in range(1, 4):  # 90도씩 총 3번 회전
            rotated = [list(x) for x in zip(*puzzle_rotations[-1])][::-1]
            puzzle_rotations.append(rotated)
        # 문자열로 변환
        puzzle_rotations_str = [str(p) for p in puzzle_rotations]
        return puzzle_rotations_str

    return str(origin_puzzle)
    
def solution(game_board, table):
    """
    규칙: 한번에 하나씩, 조각 회전 O, 새로 채워 넣은 퍼즐 조각과 인접한 칸이 비어있으면 안됨
    Args
        game_board: 현재 게임 보드의 상태
        table: 테이블 위에 놓인 퍼즐 조각의 상태
    Returns
        규칙에 맞게 최대한 많은 퍼즐 조각을 채워 넣을 경우, 총 몇 칸을 채울 수 있는지
    """
    answer = 0
    n = len(table)
    moves = ((-1, 0), (1, 0), (0, 1), (0, -1))
    table_puzzles, board_puzzles = [], []
    
    for i in range(n): # game_board 0, 1 반전
        for j in range(n):
            game_board[i][j] = 1 - game_board[i][j]
    
    for row in range(n):
        for col in range(n):
            if table[row][col] == 1:
                routes = []
                dfs(table, moves, n, row, col, routes)
                table_puzzles.append(get_puzzle(table, routes))
            if game_board[row][col] == 1:
                routes = []
                dfs(game_board, moves, n, row, col, routes)
                board_puzzles.append(get_puzzle(game_board, routes, is_game_board=True))
    
    board_puzzles_count = defaultdict(int)
    for board_puzzle in board_puzzles:
        board_puzzles_count[board_puzzle] += 1
    
    for puzzle in table_puzzles:
        for rotation in puzzle:
            if board_puzzles_count.get(rotation, 0) > 0:
                answer += rotation.count('1')
                board_puzzles_count[rotation] -= 1
                break

    return answer