import sys

""" 
    특정한 정수 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정
    
    3 <= region_cnt <= 10^4
    1 <= budget <= 10^5
    region_cnt <= budgets_sum <= 10^9
        
    총 시간 복잡도: 
    핵심 아이디어: 이진분류
""" 
def solution(region_cnt, budgets, budgets_sum):
    budgets.sort()
    
    if sum(budgets) <= budgets_sum: return budgets[-1]
    
    left = 0
    right = budgets[-1]
    mid = (left + right) // 2
    answer = 0
    
    while left < right - 1:
        temp = sum(b if b <= mid else mid for b in budgets)
        if temp <= budgets_sum:
            answer = max(answer, mid)
            left = mid
        else:
            right = mid
            
        mid = (left + right) // 2

    return answer

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    budgets = list(map(int, input().split()))
    m = int(input())
    print(solution(n, budgets, m))
