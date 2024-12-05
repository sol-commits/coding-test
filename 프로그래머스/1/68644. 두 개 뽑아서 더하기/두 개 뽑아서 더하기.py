# 정수 배열 numbers
# return : 서로 다른 인덱스에 있는 두개의 수를 뽑아 더해 만들 수 있는 모든 수를 배열에 오름차순으로
def solution(numbers):
    answer = []
    dict = {}
    
    for i in range(0, len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            dict[numbers[i] + numbers[j]] = 1
    
    for key in dict:
        answer.append(key)
        
    answer.sort()
    return answer