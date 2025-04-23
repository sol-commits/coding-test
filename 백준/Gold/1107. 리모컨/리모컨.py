import sys
from itertools import product

sys.set_int_max_str_digits(500000)

def solution(target, broken_btn):
    """
    지금 보고 있는 채널 = 100번
    채널 N으로 이동하기 위해 버튼을 최소 몇 번 눌러야하는지 출력
    """
    work_btn = [num for num in range(10) if num not in broken_btn]
    digit = len(str(target))
    max_count = abs(target - 100)
    
    candidates_num = []
    for i in range(1, 7):
        candidate = list(product(work_btn, repeat=i))
        for product_arr in candidate:
            number = ''
            for n in product_arr:
                number += str(n)
            candidates_num.append(int(number))
            
    count = max_count
    if candidates_num:
        candidates_num.sort(key = lambda key: abs(target - key))
        
        count = abs(target - candidates_num[0])
        count += len(str(candidates_num[0]))
    
    print(min(max_count, count))
        
        
if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input()) # 이동하려고 하는 채널
    M = int(input()) # 고장난 버튼의 개수
    broken_btn = []
    if M > 0:
        broken_btn = list(map(int, input().split()))
        
    solution(N, broken_btn)