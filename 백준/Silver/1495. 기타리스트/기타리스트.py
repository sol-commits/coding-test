import sys
from collections import defaultdict

def is_valid(vol, max_vol):
    return 0 <= vol <= max_vol

def solution(song_num, start_vol, max_vol, vol_diffs):
    """
    vol_diffs: 곡을 연주하기 전에 바꿀 수 있는 볼륨
    
    1 <= song_nums <= 50, 1 <= max_vol <= 1,000, 1 <= start_vol <= max_vol
    
    총 시간 복잡도: 
    핵심 아이디어: 
    """  
    candidates = defaultdict(set)
    candidates[-1].add(start_vol)
    
    for idx, vol_diff in enumerate(vol_diffs): # O(50)
        if not candidates[idx-1]: return -1
        for vol in candidates[idx-1]: # O(2^50) = O(10^10)
            if is_valid(vol + vol_diff, max_vol): 
                candidates[idx].add(vol + vol_diff)
            if is_valid(vol - vol_diff, max_vol):
                candidates[idx].add(vol - vol_diff)

    return max(candidates[song_num-1]) if candidates[song_num-1] else -1
                
if __name__ == "__main__":
    input = sys.stdin.readline
    N, S, M = list(map(int, input().split()))
    volumes = list(map(int, input().split()))
    
    print(solution(N, S, M, volumes))
