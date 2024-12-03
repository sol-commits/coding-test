def solution(num_list):
    n = len(num_list)
    diff = num_list[n-1] - num_list[n-2]
    if diff <= 0:
        num_list.append(2 * num_list[n-1])
    else:
        num_list.append(diff)
    return num_list