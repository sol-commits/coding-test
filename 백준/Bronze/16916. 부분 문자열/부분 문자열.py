import sys

def solution(str, substr):
    """
    substr이 str의 부분문자열이라면 1을 반환, 아니면 0
    
    1 <= len(str), len(substr) <= 1,000,000
    
    총 시간 복잡도: O(1,000,000)
    핵심 아이디어: in 연산
    """  
    return int(substr in str)
    
if __name__ == "__main__":
    input = sys.stdin.readline
    S = input().rstrip('\n')
    P = input().rstrip('\n')
    print(solution(S, P))
    