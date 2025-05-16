import sys
from collections import deque       

def in_board(w, h, row, col):
    return (0 <= row < h) & (0 <= col < w)

def solution(board_h, board_w, board):
    """
    board_h: 보드의 세로 크기
    board_w: 보드의 가로 크기
    board: 보드 상태
        - o: 동전, .: 빈칸, #: 벽
        - o의 개수는 항상 2개
    첫째 줄에 두 동전 중 하나만 보드에 떨어뜨기 위해 눌러야 하는 버튼의 최소 횟수
    - 두 동전을 떨어뜨릴 수 없거나, 버튼을 10번보다 많이 눌러야 한다면 -1 출력
    
    1 <= board_h, board_w <= 20
    
    총 시간 복잡도: 
    핵심 아이디어: bfs(최소 몇번)
    """  
    move = [[1, 0], [0, 1], [-1, 0], [0, -1]] # 버튼
    coin_loc = []
    for row in range(board_h):
        for col in range(board_w):
            if board[row][col] == 'o':
                coin_loc.append((row, col))
    coin_loc = tuple([(coin_loc[0][0], coin_loc[0][1], 
                        coin_loc[1][0], coin_loc[1][1], 0)])
    q = deque(coin_loc)
    visited = set()
    
    while q:
        coins_pop = q.popleft()
        coins_loc = coins_pop[:4]
        count = coins_pop[4]
        
        if count == 10:
            return -1
        
        for drow, dcol in move:
            coin1_nrow, coin1_ncol = coins_loc[0] + drow, coins_loc[1] + dcol
            coin2_nrow, coin2_ncol = coins_loc[2] + drow, coins_loc[3] + dcol
            
            out_board = 0 # 코인 몇 개가 board를 벗어나는지
            
            if in_board(board_w, board_h, coin1_nrow, coin1_ncol):
                if board[coin1_nrow][coin1_ncol] == '#':
                    coin1_nrow, coin1_ncol = coins_loc[0], coins_loc[1]
            else:
                out_board  += 1
            if in_board(board_w, board_h, coin2_nrow, coin2_ncol):
                if board[coin2_nrow][coin2_ncol] == '#': 
                    coin2_nrow, coin2_ncol = coins_loc[2], coins_loc[3]
            else:
                out_board  += 1
            
            if out_board == 1:
                return count + 1
            elif out_board != 2: # 둘 다 보드 안에 있다면
                # 예시) coin1 -> coin2 가려고하는데, coin2는 벽에 막혀 못 움직이고 있다면
                if (coin1_nrow, coin1_ncol) == (coin2_nrow, coin2_ncol): 
                    continue
                else: 
                    if (coin1_nrow, coin1_ncol, coin2_nrow, coin2_ncol) not in visited:
                        q.append((coin1_nrow, coin1_ncol, coin2_nrow, coin2_ncol, count + 1))
                        visited.add((coin1_nrow, coin1_ncol, coin2_nrow, coin2_ncol))
    return -1
            
if __name__ == "__main__":
    input = sys.stdin.readline
    board_h, board_w = list(map(int, input().split()))
    board = list(list(input().rstrip('\n')) for _ in range(board_h))
    print(solution(board_h, board_w, board))
