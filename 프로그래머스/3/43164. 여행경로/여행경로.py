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
    possible_routes = []
    
    from_to_map = defaultdict(list)
    tickets_count = defaultdict(int)
    
    for from_, to_ in tickets:
        from_to_map[from_].append(to_)
        tickets_count[(from_, to_)] += 1
    
    stack = []
    
    for to_ in from_to_map['ICN']:
        stack.append(("ICN", to_, []))
    
    while stack:
        prev_port, cur_port, routes = stack.pop()
        routes.append((prev_port, cur_port))
        if len(routes) == len(tickets):
            possible_route = []
            possible_route.append(routes[0][0])
            for from_, to_ in routes:
                possible_route.append(to_)
            possible_routes.append(possible_route)
            continue
        for next_port in from_to_map[cur_port]:
            if routes.count((cur_port, next_port)) < tickets_count[(cur_port, next_port)]:
                stack.append((cur_port, next_port, routes.copy()))
                
    return  sorted(possible_routes, key=lambda x: (tuple(x)))[0]