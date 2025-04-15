from collections import defaultdict

def solution(n, results):
    """
    선수의 수 n, 경기 결과를 담은 2차원 배열 results
    정확하게 순위를 매길 수 있는 선수의 수를 반환
    """
    win_graph = defaultdict(list) # 선수 간의 이긴 관계를 담은 그래프
    lose_graph = defaultdict(list) # 선수 간의 진 관계를 담은 그래프
    
    records = [[-1, -1] for _ in range(n + 1)] # 총 이긴 횟수, 진 횟수 기록
    
    for win, lose in results:
        win_graph[lose].append(win) 
        lose_graph[win].append(lose)
        
    graphs = [win_graph, lose_graph]
    for i in range(1, n + 1):
        for j in range(len(graphs)):
            stack = [i]
            visited = [False] * (n + 1)
    
            while stack:    
                current = stack.pop()
                if visited[current]:
                    continue
                records[i][j] += 1
                visited[current] = True
                for next in graphs[j][current]:
                    if not visited[next]:
                        stack.append(next)

    # print(records)
    answer = 0
    for i in range(1, n + 1):
        if records[i][0] + records[i][1] == n - 1:
            answer += 1
    
    return answer