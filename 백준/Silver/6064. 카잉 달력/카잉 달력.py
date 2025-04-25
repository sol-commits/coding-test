import sys
from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

def solution(M, N, x, y):
    """
    <M:N> = 마지막 해, <x:y> = ?
    """  
    L = lcm(M, N) # 최소공배수
    
    k = x
    while k <= L:
        cur_y = k % N if k % N != 0 else N
        if cur_y == y:
            return k
        
        k += M
        
    return -1  
        
if __name__ == "__main__":
    input = sys.stdin.readline
    T = int(input()) 
    cases = [list(map(int, input().split())) for _ in range(T)]
        
    for case in cases:
        print(solution(case[0], case[1], case[2], case[3]))