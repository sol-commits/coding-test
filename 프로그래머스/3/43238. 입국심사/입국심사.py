def binary_search_recursive(times, target, start, end, min_time):
    # 탐색 범위가 비어있다면 최소 시간 반환
    if start > end:
        return min_time
    
    mid = (start + end) // 2
    # 중간값에서 처리 가능한 총 인원 계산
    total_people = sum(mid // time for time in times)

    # 처리 가능한 총 인원 >= 사람수
    # 더 작은 시간으로 탐색하며 최소 시간을 업데이트
    if total_people >= target:
        return binary_search_recursive(times, target, start, mid - 1, mid)
    # 처리 가능한 총 인원 < 사람수
    # 더 큰 시간으로 탐색
    else:
        return binary_search_recursive(times, target, mid + 1, end, min_time)

def solution(n, times):
    """
    Args
        n: 입국심사를 기다리는 사람 수
        times: 각 심사관이 한 명을 심사하는데 걸리는 시간
    Returnss
        모든 사람이 심사를 받는데 걸리는 시간의 최솟값
    """
    times.sort()
    
    # 이분 탐색의 시작 범위: 가장 짧은 심사 시간
    start = times[0]
    # 이분 탐색의 끝 범위: 가장 긴 심사 시간이 모든 사람을 처리하는 경우
    end = times[0] * n
    
    return binary_search_recursive(times, n, start, end, start)