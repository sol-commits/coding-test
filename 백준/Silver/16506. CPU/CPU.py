import sys

opcode_map = {
    "ADD": '0000', "ADDC": '0000',
    "SUB": '0001', "SUBC": '0001',
    'MOV': '0010', 'MOVC': '0010',
    'AND': '0011', 'ANDC': '0011',
    'OR': '0100', 'ORC': '0100',
    'NOT': '0101',
    'MULT': '0110', 'MULTC': '0110',
    'LSFTL': '0111', 'LSFTLC': '0111',
    'LSFTR': '1000', 'LSFTRC': '1000',
    'ASFTR': '1001', 'ASFTRC': '1001',
    'RL': '1010', 'RLC': '1010',
    'RR': '1011', 'RRC': '1011',
}

def solution(command_num, commands):
    """
    command_num: 명령어의 수
    commands: 명령어
    - opcode rD rA rB 또는 opcode rD rA #C
    
    어셈블리어 코드를 기계어 코드로 번역하여 반환
    
    1 <= command_num <= 500
    0 <= rD, rA, rB <= 7 -> 레지스터 번호
        - 사용하지 않을 경우에만 0이 주어짐
    0 <= #C <= 15  -> 상수
    
    총 시간 복잡도: 
    핵심 아이디어: 구현
    """  
    answer = []
    for command in commands:
        assembly  = opcode_map[command[0]]
    
        is_rb = False
        if command[0][-1] == 'C':
            assembly += '10' # #C 사용
        else:
            assembly += '00' # rB 사용
            is_rb = True
        
        assembly += str(bin(int(command[1]))).replace("b", "0")[-3:].zfill(3) # rD
        
        if ('MOV' in command[0]) or ('NOT' == command[0]):
            assembly += '000' # rA
        else:
            assembly += str(bin(int(command[2]))).replace("b", "0")[-3:].zfill(3) # rA
        
        if is_rb:
            assembly += str(bin(int(command[3]))).replace("b", "0")[-3:].zfill(3) # rB
            assembly += '0'
        else:
            assembly += str(bin(int(command[3]))).replace("b", "0")[-4:].zfill(4) # #C
            
        answer.append(assembly)
    return answer
            
if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    commands = [input().split() for _ in range(N)]
    for sol in solution(N, commands):
        print(sol)
