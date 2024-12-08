def solution(common):
    is_arithmetic = False
    if common[2] - common[1] == common[1] - common[0]:
        is_arithmetic = True
        d = common[2] - common[1]
    else:
        r = common[2]//common[1]
        
    return common[len(common) - 1] + d if is_arithmetic else common[len(common) - 1] * r