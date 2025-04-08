def solution(distance, rocks, n):
    rocks.append(distance)
    rocks.sort()
    
    left, right = 0, distance
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2
        current = 0
        removed_rocks = 0
        
        for rock in rocks:
            if rock - current < mid:
                removed_rocks += 1
            else:
                current = rock
        
        if removed_rocks <= n:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return answer