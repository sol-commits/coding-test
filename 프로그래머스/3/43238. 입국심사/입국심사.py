def binary_search_recursive(times, target, start, end, min):
    # 탐색 범위가 비어있다면 종료
    if start > end:
        return min
    
    mid = (start + end) // 2
    
    total = sum([mid // time for time in times])
    
    # print(start, mid, end, total)

    # 목푯값이 중간값보다 작다면 왼쪽으로 재귀 호출
    if total >= target:
        if total == target:
            min = mid
        return binary_search_recursive(times, target, start, mid - 1, mid)
    # 목푯값이 중간값보다 크다면 오른쪽으로 재귀 호출
    else:
        return binary_search_recursive(times, target, mid + 1, end, min)

def solution(n, times):
    """
    Args
        n: 입국심사를 기다리는 사람 수
        times: 각 심사관이 한 명을 심사하는데 걸리는 시간
    Returnss
        모든 사람이 심사를 받는데 걸리는 시간의 최솟값
    """
    times.sort()
    
    low = times[0]
    high = times[-1] * n
    
    return binary_search_recursive(times, n, low, high, low)


if __name__ == "__main__":
    n = 6
    times = [1, 6]
    print(solution(n, times)) # 6