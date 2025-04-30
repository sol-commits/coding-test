import sys

def solution(parentheses):
    """
    () : 2
    [] : 3
    ( X ) : 2 x 값(X)
    [ X ] : 3 x 값(X)
    XY = 값(X) + 값(Y)
    
    올바르지 못한 괄호열이면 0 출력
    """  
    
    stack = []
    
    paren_map = {
        ')' : '(',
        ']' : '['
    }
    
    paren_value = {
        ')' : 2,
        ']' : 3
    }
    
    for paren in parentheses:
        if not stack:
            stack.append(paren)
            continue
        if paren not in paren_map: # 닫힌 괄호가 아니라면
            stack.append(paren)
        elif paren in paren_map: # 닫힌 괄호라면
            if stack[-1] == paren_map[paren]:
                stack.pop()
                stack.append(paren_value[paren])
            elif type(stack[-1]) == type(1):
                sub_value = 0
                while stack and type(stack[-1]) == type(1):
                    sub_value += stack.pop()
                if stack and stack[-1] == paren_map[paren]:
                    stack.pop()
                    sub_value *= paren_value[paren]
                    stack.append(sub_value)
                else:
                    return 0
    answer = 0
    while stack:
        if type(stack[-1]) != type(1):
            return 0
        answer += stack.pop()
    return answer
        
        
if __name__ == "__main__":
    input = sys.stdin.readline
    parentheses = input().rstrip('\n')
    print(solution(parentheses))