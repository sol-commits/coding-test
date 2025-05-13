import sys
from collections import defaultdict, deque

def solution(declares):
    """
    i# : 기본 변수형, 배열[], 참조&, 포인터* 
    int& a*[]&, b, c*;
    -> a의 타입: int&&[]*
    
    declares: ['int&', 'a*[]&,', 'b,', 'c*';
    - declares[0] = 기본 변수형 + 추가적인 변수형
    - declares[1:] = 변수 선언
    
    총 시간 복잡도: O(10^5)
    핵심 아이디어: 위상 정렬 -> 진입 차수가 0인 것만 큐에 넣어서 줄을 세운다. 
    """  
    
    answer = []
    
    base_type = declares[0]
    for i in range(1, len(declares)):
        temp = base_type
        var = ''
        stack = []
        for c in declares[i][:-1]: # , or ; 제외
            if c.isalpha():
                var += c
            elif c == '[':
                stack.append(']')
            elif c == ']':
                stack.append('[')
            else:
                stack.append(c)
        while stack:
            temp += stack.pop()
        temp += ' ' + var + ';'
        answer.append(temp)
        
    return answer
    
if __name__ == "__main__":
    input = sys.stdin.readline
    declares = input().split()
    for sol in solution(declares):
        print(sol)
    