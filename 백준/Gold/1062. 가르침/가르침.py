import sys
from itertools import combinations

def solution(teach_cnt, words):
    """
    teach_cnt: 가르칠 알파벳의 개수
    words: anta ** tica 인 남극언어
    """  
    teach_cnt -= 5
    if teach_cnt < 0:
        return 0
    
    always_valid = 0
    antatica = set('antatica')
    required_letters = set()
    word_masks = []
    for word in words:
        filtered = set(word) - antatica
        if not filtered:
            always_valid += 1
        elif len(filtered) <= teach_cnt:
            required_letters.update(filtered)
            mask = sum(1 << (ord(c) - ord('a')) for c in filtered)
            word_masks.append(mask)
            
    if len(required_letters) <= teach_cnt:
        return always_valid + len(word_masks)
    
    max_count = 0
    for comb in combinations(required_letters, teach_cnt):
        mask = sum(1 << (ord(c) - ord('a')) for c in comb)
        count = 0
        for word_mask in word_masks:
            if (word_mask & mask) == word_mask:
                count += 1
        max_count = max(max_count, count)
        
    return always_valid + max_count
    
if __name__ == "__main__":
    input = sys.stdin.readline
    N, K = list(map(int, input().split()))
    words = list(input().strip() for _ in range(N))
    print(solution(K, words))
    