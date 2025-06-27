import sys
from heapq import heappop, heappush

""" 
    L : 커서를 왼쪽으로 한 칸 옮김, D : 커서를 오른쪽으로 한 칸 옮김
    B : 커서 왼쪽에 있는 문자 삭제, P $ : $라는 문자를 커서 왼쪽에 추가
    - 모든 명령어를 수행하고 난 후 편집기에 입력되어 있는 문자열을 출력
    - 처음 커서의 위치는 문장의 맨뒤
    
    len(text) <= 10^5, 1 <= commands_cnt <= 5*10^5
    
    핵심아이디어: 그리디 -> 더 높은 주가가 나타날 때 과거의 주식을 모두 파는 것
    과거의 주식을 판 개수만큼, 오늘 산 주식을 다시 삼
""" 
class Node:
    def __init__(self, val="", prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

def solution(text, commands_cnt, commands):
    head_node = Node(text[0]) # head_node
    prev_node = head_node
    
    for idx in range(1, len(text)):
        cur_node = Node(text[idx], prev=prev_node)
        prev_node.next = cur_node
        prev_node = cur_node
        
    cursor = cur_node, None
    
    for command in commands:
        if command[0] == 'L':
            if cursor[0]:
                cursor = cursor[0].prev, cursor[0]
        elif command[0] == 'D':
            if cursor[1]:
                cursor = cursor[1], cursor[1].next
        elif command[0] == 'B':
            if cursor[0]:
                if cursor[1]:
                    cursor[1].prev = cursor[0].prev
                if cursor[0].prev:
                    cursor[0].prev.next = cursor[1]
                cursor = cursor[0].prev, cursor[1]
        else:
            add_node = Node(command[1], prev=cursor[0], next=cursor[1])
            if cursor[0]:
                cursor[0].next = add_node
            if cursor[1]:
                cursor[1].prev = add_node
            cursor = add_node, cursor[1]
    
    cur_node = cursor[1] if cursor[1] else cursor[0]
    while cur_node.prev:
        cur_node = cur_node.prev
    
    answer = ''
    while cur_node.next:
        answer += cur_node.val
        cur_node = cur_node.next
    
    print(answer + cur_node.val)
                
if __name__ == "__main__":
    input = sys.stdin.readline
    input_str = input().rstrip("\n")
    M = int(input())
    commands = [input().rstrip("\n").split() for _ in range(M)]
    
    solution(input_str, M, commands)