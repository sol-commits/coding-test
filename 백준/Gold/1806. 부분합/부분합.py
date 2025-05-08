import sys
from collections import deque

def solution(nums_length, target_sum, nums):
    """
    nums_length: 수열의 길이
    nums 에서 연속된 수들의 부분합 중에 
    그 합이 target_sum 이상이 되는 것 중 가장 짧은 것의 길이를 반환
    -> 합을 반환하는 게 불가능하다면 0 반환
    
    1 <= nums_length <= 100,000
    0 <= target_sum <= 100,000,000
    
    총 시간 복잡도: O(10000log(100))
    핵심 아이디어: 지금 위치에서 가장 늦게 등장하는 아이템부터 제거 -> 그리디
    """  
    
    q = deque()
    
    total = 0
    answer = 100001
    
    for num in nums: # O(N) : 10,000
        q.append(num)
        total += num
        
        # O(N) : 1 ~ 10,000
        while q and total - q[0] >= target_sum:
            total -= q.popleft()
        
        if not q:
            answer = 1
        elif total >= target_sum:
            answer = min(answer, len(q))
    

    return answer if answer != 100001 else 0
    
if __name__ == "__main__":
    input = sys.stdin.readline
    N, S = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    print(solution(N, S, nums))
    