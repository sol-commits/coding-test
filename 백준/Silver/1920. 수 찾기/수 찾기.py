import sys

def solution(N, A_list, M, numbers):
    """
    numbers 에 있는 숫자들이 A_list에 있는지 출력
    """
    number_dict = {}
    for number in numbers:
        number_dict[number] = 0
    
    for A in A_list:
        if A in number_dict:
            number_dict[A] = 1
    
    for number in numbers:
        if number in number_dict:
            print(number_dict[number])
        
    
if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    A_list = list(map(int, input().split()))
    M = int(input())
    numbers = list(map(int, input().split()))

    solution(N, A_list, M, numbers)