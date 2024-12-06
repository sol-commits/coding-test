def solution(answers):
    patterns = [
        [1, 2, 3, 4, 5] * 2000,
        [2, 1, 2, 3, 2, 4, 2, 5] * 1250,
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    ]

    scores = [0] * 3;
    
    for idx, answer in enumerate(answers):
        for i in range(3):
            if patterns[i][idx] == answer:
                scores[i] += 1
            
    max_score = max(scores)
    highest_scores = []
    
    for idx, score in enumerate(scores):
        if score == max_score:
            highest_scores.append(idx + 1)
        
    return highest_scores
