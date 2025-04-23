import sys

def solution(N):
    """
    1부터 N까지의 수를 이어서 썼을 때, 이 수의 자릿수
    """
    digit = len(str(N))
    count = 0
    
    for i in range(digit - 1):
        count += (i+1) * (9 * (10 ** i))
    count += digit * (N - (10 ** (digit - 1)) + 1)
    
    print(count)
        
        
if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input()) 
        
    solution(N)