import sys
from collections import defaultdict
from heapq import heappop, heappush

""" 
    팀의 순위를 반환
    최고 점수가 최종 점수, 
    
    3 <= region_cnt <= 10^4
    1 <= budget <= 10^5
    region_cnt <= budgets_sum <= 10^9
        
    총 시간 복잡도: O(region_cnt log(budget))
    핵심 아이디어: 최소힙
""" 
def solution(team_cnt, prob_cnt, my_team, log_cnt, logs):
    pq = []
    team_scores = defaultdict(list)
    
    for submission, log in enumerate(logs):
        team_id, prob_id, score = log
        if team_id not in team_scores:
            team_scores[team_id] = [0, 0, 0] # 최종 점수, 제출 횟수, 마지막 제출 시간
        heappush(pq, (-score, prob_id, team_id, submission))
    
    counted = set()
    
    while pq:
        score, prob, team, submission = heappop(pq)
        score = -score
        
        if (team, prob) not in counted:
            counted.add((team, prob))
            team_scores[team][0] += score
        
        team_scores[team][1] += 1
        team_scores[team][2] = max(team_scores[team][2], submission)
    
    teams_sorted = sorted(team_scores, key=lambda key: (-team_scores[key][0], team_scores[key][1], team_scores[key][2]))
    
    rank = 1
    for team in teams_sorted:
        if team == my_team:
            return rank
        rank += 1

if __name__ == "__main__":
    input = sys.stdin.readline
    t = int(input())
    n_list, k_list, id_list, m_list = [], [], [], []
    solves_list = []
    for i in range(t):
        n, k, id, m = list(map(int, input().split()))
        n_list.append(n)
        k_list.append(k)
        id_list.append(id)
        m_list.append(m)
    
        solves = []
        for _ in range(m):
            solves.append(list(map(int, input().split())))
        solves_list.append(solves)
    
    for i in range(t):
        print(solution(n_list[i], k_list[i], id_list[i], m_list[i], solves_list[i]))