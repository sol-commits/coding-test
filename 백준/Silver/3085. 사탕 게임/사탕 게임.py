import sys

def count_color(N, candies):
    max_count = 0
    
    for i in range(N):
        color = candies[i][0]
        count = 0
        for j in range(N):
            if candies[i][j] == color:
                count += 1
            else:
                max_count = max(max_count, count)
                color = candies[i][j]
                count = 1
        
        max_count = max(max_count, count)
    
    for j in range(N):
        color = candies[0][j]
        count = 0
        for i in range(N):
            if candies[i][j] == color:
                count += 1
            else:
                max_count = max(max_count, count)
                color = candies[i][j]
                count = 1
        
        max_count = max(max_count, count)
    
    return max_count

def solution(N, candies):
    answer = 0
    
    adj = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    
    for i in range(N):
        for j in range(N):
            for drow, dcol in adj:
                next_row, next_col = i + drow, j + dcol
                
                if 0 <= next_row < N and 0 <= next_col < N:
                    candies[i][j], candies[next_row][next_col] = candies[next_row][next_col], candies[i][j]
                    answer = max(count_color(N, candies), answer)
                    candies[i][j], candies[next_row][next_col] = candies[next_row][next_col], candies[i][j] # 되돌려놓기
                    
                if answer == N:
                    break
                
    
    print(answer)
            
if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input()) # 보드의 크기
    candies = [list(input())[:-1] for _ in range(N)]
        
    solution(N, candies)