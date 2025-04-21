def solution(arrows):
    answer = 0
    visited_nodes = set()
    visited_edges = set()
    
    dir = {
        0: (-1, 0), 1: (-1, 1), 2: (0, 1), 3: (1, 1),
        4: (1, 0), 5: (1, -1), 6: (0, -1), 7: (-1, -1)
    }

    # 시작 위치 (중앙에서 시작)
    x, y = 0, 0
    visited_nodes.add((x, y))

    for arrow in arrows:
        for _ in range(2):  # 두 칸으로 나눠야 교차점 처리 가능
            dx, dy = dir[arrow]
            nx, ny = x + dx, y + dy

            # 간선 정보 양방향으로 저장
            edge = ((x, y), (nx, ny))
            reverse_edge = ((nx, ny), (x, y))
            
            # 이미 방문한 노드인데, 새로운 간선을 지나온 경우 → 사이클 발생
            if (nx, ny) in visited_nodes and edge not in visited_edges:
                answer += 1
            
            visited_nodes.add((nx, ny))
            visited_edges.add(edge)
            visited_edges.add(reverse_edge)

            x, y = nx, ny  # 이동

    return answer