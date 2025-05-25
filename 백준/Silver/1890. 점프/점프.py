import sys

def is_in_bounds(row, col, size):
    return (0 <= row < size) and (0 <= col < size)
        
def get_path_counts(row, col, dp, board, board_size):
    if not is_in_bounds(row, col, board_size):
        return 0
    if dp[row][col] != 0:
        return dp[row][col]
    
    # 위 쪽에서 점프 가능할 때
    for r in range(row): 
        if board[r][col] == row - r:
            dp[row][col] += get_path_counts(r, col, dp, board, board_size)
    # 왼쪽에서 점프 가능할 때
    for c in range(col):
        if board[row][c] == col - c:
            dp[row][col] += get_path_counts(row, c, dp, board, board_size)
            
    return dp[row][col]

def solution(board_size, board):
    """
    board[i][j] -> 현재 칸에서 갈 수 있는 거리
    반드시 오른쪽이나 아래쪽으로만 이동
    가장 왼쪽 위 칸에서 가장 오른쪽 아래 칸으로 규칙에 맞게 이동할 수 있는 경로의 개수를 반환
    
    4 <= board_size <= 100
    0 <= board[i][j] <= 9
    
    총 시간 복잡도: 
    핵심 아이디어: dp, top-down
    """  
    dp = [[0] * board_size for _ in range(board_size)]
    dp[0][0] = 1 # 시작점
                
    return get_path_counts(board_size-1, board_size-1, dp, board, board_size)
                
if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    print(solution(N, board))
