from collections import deque

def is_one_char_diff(word1, word2):
    diff_count = 0
    
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            diff_count += 1
        if diff_count > 1:
            return False
    
    return True

def solution(begin, target, words):
    """
    - 한 번에 한 개의 알파벳만 바꿀 수 있음
    Args:
        - 단어 begin -> target
        - words: 단어 집합 
    Returns:
        - 가장 짧은 변환 단계
    """
    visited = {word: 0 for word in words}
    queue = deque([(begin, 0)])
    n = len(begin)
    
    while queue:
        cur_word, steps = queue.popleft()
        if cur_word == target:
            return steps
        for word in words:
            if is_one_char_diff(word, cur_word) and not visited[word]:
                queue.append((word, steps + 1))
                visited[word] = 1
    return 0
