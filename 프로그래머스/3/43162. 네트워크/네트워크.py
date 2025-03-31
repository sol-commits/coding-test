# DFS, union-find로도 풀 수 있을 듯

def solution(n, computers):
    """
    Args:
        - n: 컴퓨터의 개수
        - computers: 연결에 대한 정보가 담긴 2차원 배열
    Returns:
        - 네트워크의 개수
    """
    visited = [0] * n
    answer = 0
    stack = [] 
    
    for computer in range(n):
        if not stack:
            if not visited[computer]:
                stack.append(computer)
                answer += 1    
        while stack:
            computer = stack.pop()
            visited[computer] = 1
            for neighbor in range(n):
                if neighbor != computer and computers[computer][neighbor] and not visited[neighbor]:
                    stack.append(neighbor)
            
    return answer