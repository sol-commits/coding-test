import sys
from collections import defaultdict

def solution(block_num, block):
    """
    B, O, J 순서로 블록을 밟으면서 점프
    한 번 k칸 만큼 점프를 하는데 필요한 에너지의 양은 k * k
    스타트가 링크를 만나는데 필요한 에너지 양의 최솟값을 반환
    만날 수 없는 경우에는 -1
    
    1 <= block_num <= 9
    
    총 시간 복잡도: O(50 x 1,001) = O(50,050)
    핵심 아이디어: 현재 단계의 가능한 볼륨을 이전 단계의 결과에만 의존
    """  
    
    record = defaultdict(list) 
    record['B'] = [(0, 0)] # idx, jump_cnt 
    order = {'B':'J', 'O':'B', 'J':'O'}  
    for idx in range(1, block_num):
        prev = order[block[idx]] 
        if prev not in record: continue 
        candidate_jumps = []
        for prev_idx, jump_cnt in record[prev]:
            jump_cnt += (idx - prev_idx) * (idx - prev_idx) 
            candidate_jumps.append((idx, jump_cnt))
        candidate_jumps.sort(key = lambda key: key[1])
        record[block[idx]].append(candidate_jumps[0])
        if idx == block_num - 1:
            return candidate_jumps[0][1]
    return -1
                
if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    block = input().rstrip("\n")
    
    print(solution(N, block))
