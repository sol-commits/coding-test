import sys
from collections import defaultdict

""" 
    1. 두 개의 단어가 같은 종류의 문자로 이루어져 있음
    2. 같은 문자는 같은 개수만큼 있음
    한 문자를 더하거나, 빼거나, 하나의 문자를 다른 문자로 바꾸어 같은 구성을 갖게 되는 경우 
    -> 비슷한 단어
    첫 번째 단어와 비슷한 단어가 모두 몇 개인지 출력
    
    words_cnt <= 100, word_len <= 10
        
    총 시간 복잡도: O(region_cnt log(budget))
    핵심 아이디어: 이진분류
""" 
def solution(words_cnt, words):
    if words_cnt == 0:
        return 0

    target_dict = defaultdict(int)
    for c in words[0]:
        target_dict[c] += 1

    answer = 0

    for word in words[1:]:
        word_dict = defaultdict(int)
        for c in word:
            word_dict[c] += 1

        # 알파벳별 개수 차이 계산
        diff = 0
        for char in set(target_dict.keys()) | set(word_dict.keys()):
            diff += abs(target_dict[char] - word_dict[char])

        # 비슷한 단어 조건: (1) 같거나 (2) 한 글자 차이거나 (3) 하나만 바뀐 경우
        if diff == 0 or diff == 1 or (diff == 2 and len(words[0]) == len(word)):
            answer += 1

    return answer

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    words = [input().rstrip("\n") for _ in range(n)]
    print(solution(n, words))
