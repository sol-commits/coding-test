import sys
from heapq import heappop, heappush

""" 
    num == 자연수 -> 배열에 num 추가 연산
    num == 0 -> 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거
""" 
def solution(op_cnt, nums):
    pq = []
    
    for num in nums:
        if num == 0:
            if not pq:
                print(0)
            else:
                print(heappop(pq))
        else:
            heappush(pq, num)

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    x_list = [int(input()) for _ in range(n)]
    
    solution(n, x_list)