import sys
from bisect import bisect_left

def solution(A):
    """
    수열 A에서, 가장 긴 증가하는 부분 수열을 구하는 문제
    """
    lis = []
    
    for num in A:
        if not lis or lis[-1] < num:
            lis.append(num)    
        else:
            lis[bisect_left(lis, num)] = num
    
    print(len(lis))
        
if __name__ == "__main__":
    input = sys.stdin.readline
    N = input()
    A = list(map(int, input().split()))

    solution(A)