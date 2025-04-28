import sys

def recursive(n, nums, idx, add_cnt, sub_cnt, mult_cnt, div_cnt, total, candidates):
    if idx == n:
        candidates.append(total)
    if add_cnt > 0:
        recursive(n, nums, idx+1, add_cnt-1, sub_cnt, mult_cnt, div_cnt, total + nums[idx], candidates)
    if sub_cnt > 0:
        recursive(n, nums, idx+1, add_cnt, sub_cnt-1, mult_cnt, div_cnt, total - nums[idx], candidates)
    if mult_cnt > 0:
        recursive(n, nums, idx+1, add_cnt, sub_cnt, mult_cnt-1, div_cnt, total * nums[idx], candidates)
    if div_cnt > 0:
        recursive(n, nums, idx+1, add_cnt, sub_cnt, mult_cnt, div_cnt-1, total // nums[idx] if total > 0 else -(abs(total) // nums[idx]), candidates)

def solution(n, nums, op_count):
    """
    n: 수의 개수, 
    n-1개의 연산자,
    만들 수 있는 식의 결과가 최대인 것과 최소인 것을 반환
    """  
    
    candidates = []
    recursive(n, nums, 1, op_count[0], op_count[1], op_count[2], op_count[3], nums[0], candidates)
    
    
    
    # a b c d
    #  4 ^ (n-1 = 4^10 = 2^20 = 1024 * 1024 = 10 * 6 -> 완전 탐색 가능
    
    
    print(max(candidates))
    print(min(candidates))
        
if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    A = tuple(map(int, input().split()))
    operation_count = tuple(map(int, input().split()))
    solution(N, A, operation_count)