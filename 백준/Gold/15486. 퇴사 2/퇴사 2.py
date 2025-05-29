import sys

def solution(day_len, day_price):
    """
    day_price: [[time1, price1], ...]
    - time: 상담을 완료하는데 걸리는 기간
    - price: 상담을 했을 때 받을 수 있는 금액
    
    얻을 수 있는 최대 수익을 반환
    
    1 <= day_price_len <= 1,500,000 = 10^6
    1 <= time <= 50, 1 <= price <= 1,000
    
    총 시간 복잡도: 
    핵심 아이디어: 현재 단계의 가능한 점프 수를 이전 단계의 결과에 의존
    """  
    prices = [0] * (day_len + 1)
    max_price_by_day = 0
    for day in range(day_len):
        next_day = day + day_price[day][0] - 1
        if next_day < day_len:
            prices[next_day] = max(prices[next_day], max_price_by_day + day_price[day][1])
        max_price_by_day = max(max_price_by_day, prices[day])
    return max_price_by_day
                
if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    TP = [list(map(int, input().split())) for _ in range(N)]
    
    print(solution(N, TP))
