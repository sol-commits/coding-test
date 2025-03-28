def solution(money):
    """
    인접한 두 집을 털면 경보가 울림
    마을의 모든 집들은 동그랗게 배치되어 있음
    Args:
    - money: 각 집에 있는 돈이 담긴 배열
    Returns:
    - 훔칠 수 있는 돈의 최댓값
    """
    include_first, include_last = money[:-1], money[1:]
    
    for i in range(2, len(include_first)):
        if i == 2:
            include_first[i] = include_first[0] + include_first[2]
            include_last[i] = include_last[0] + include_last[2]
            continue
        include_first[i] = max(include_first[i-3], include_first[i-2]) + include_first[i]
        include_last[i] = max(include_last[i-3], include_last[i-2]) + include_last[i]
    
    return max(max(include_first), max(include_last))