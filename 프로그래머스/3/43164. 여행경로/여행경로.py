from collections import defaultdict

def solution(tickets):
    """
    항공권 모두 이용, 항상 ICN에서 출발
    가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return
    Args
        tickets: 항공권 정보가 담긴 2차원 배열
    Returnss
        방문하는 공항 경로 배열
    """
    
    from_to_map = defaultdict(list)
    tickets_count = defaultdict(int)
    
    for from_port, to_port in tickets:
        from_to_map[from_port].append(to_port)
        tickets_count[(from_port, to_port)] += 1
        
    for from_port in from_to_map.keys():
        from_to_map[from_port].sort(reverse=True)
    
    stack = []
    
    for next_port in from_to_map['ICN']:
        stack.append(("ICN", next_port, [])) # 현재 공항, 다음 공항, 지금까지의 경로
    
    while stack:
        prev_port, cur_port, routes = stack.pop()
        routes.append((prev_port, cur_port))
        
        if len(routes) == len(tickets):
            answer = [routes[0][0]]
            for _, to_port in routes:
                answer.append(to_port)
            return answer
        
        for next_port in from_to_map[cur_port]:
            if routes.count((cur_port, next_port)) < tickets_count[(cur_port, next_port)]:
                stack.append((cur_port, next_port, routes.copy()))