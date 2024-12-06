# pattern1 = [1, 2, 3, 4, 5]
# pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
# pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
# answers : 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열
# return : 가장 많은 문제를 맞힌 사람이 누구인지 배열
# 가장 높은 점수를 받은 사람이 여럿일 경우, 오름차순으로 정렬
def solution(answers):
    result = []
    
    pattern1 = [1, 2, 3, 4, 5] * 2000
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    count = [0] * 3;
    
    for answer, a, b, c in zip(answers, pattern1, pattern2, pattern3):
        if a == answer: 
            count[0] += 1
        if b == answer:
            count[1] += 1
        if c == answer:
            count[2] += 1
            
    max_count = max(count)
    
    for idx, value in enumerate(count):
        if value == max_count:
            result.append(idx + 1)
        
    return result