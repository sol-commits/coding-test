import sys
import math

def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def solution(digits):
    """
    digits 자리 수 주에서 신기한 소수를 오름차순으로 정렬해서 반환
    신기한 소수: 7331
    - 733도 소수, 73도 소수, 7도 소수
    - 왼쪽부터 1자리, 2자리, 3자리, 4자리 수 모두 소수
    
    1 <= digits <= 8
    
    총 시간 복잡도: O(10^5)
    핵심 아이디어: dp
    """  
    min_num = int('2' + '0' * (digits-1))
    max_num = int('9' * digits)
    visited = set()
    stack = ['2', '3', '5', '7'] 
    answer = []

    while stack:
        num_str = stack.pop()
        if num_str in visited:
            continue
        visited.add(num_str)
        if is_prime(int(num_str)):
            if len(num_str) == digits:
                answer.append(int(num_str))
            else:
                for next in ['1', '3', '7', '9']:
                    if num_str + next not in visited:
                        stack.append(num_str + next)
            
    answer.sort()
    return answer
            
if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    for num in solution(N):
        print(num)
    