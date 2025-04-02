from collections import deque
import math

def solution(rectangle, characterX, characterY, itemX, itemY):
    """
    Args:
        rectangle: 직사각형이 담긴 2차원 배열
        characterX, Y: 캐릭터의 x좌표, y좌표
        itemX, Y: 아이템의 x좌표, y좌표
    Returns:
        캐릭터가 아이템을 줍기 위해 이동해야 하는 최소 거리
    """
    map = [[0] * 151 for _ in range(152)]
    moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    points = {}
    
    for x1, y1, x2, y2 in rectangle:
        for x in range(x1*3, x2*3 + 1):
            for y in [y1*3, y2*3]:
                map[x][y] = 1
        for y in range(y1*3, y2*3 + 1):
            for x in [x1*3, x2*3]:
                map[x][y] = 1
        map[x1*3][y1*3] = 1
        map[x2*3][y1*3] = 1
        map[x1*3][y2*3] = 1
        map[x2*3][y2*3] = 1
        points[(x1*3, y1*3)] = 1
        points[(x2*3, y1*3)] = 1
        points[(x1*3, y2*3)] = 1
        points[(x2*3, y2*3)] = 1
    
    for x1, y1, x2, y2 in rectangle:
        for x in range(x1*3+1, x2*3):
            for y in range(y1*3+1, y2*3):
                map[x][y] = 0
    
    characterX, characterY = characterX*3, characterY*3
    itemX, itemY = itemX*3, itemY*3
    
    queue = deque([(characterX, characterY, 1)])
    map[characterX][characterY] = 0
    
    while queue:
        cur_X, cur_Y, dist = queue.popleft()
        if (cur_X, cur_Y) == (itemX, itemY):
            return dist // 3
        
        for move_X, move_Y in moves:
            new_X, new_Y = cur_X + move_X, cur_Y + move_Y
            if 0 < new_X < 151 and 0 < new_Y < 151 and map[new_X][new_Y] == 1:
                map[new_X][new_Y] = 0
                # if (cur_X, cur_Y) in points:
                #     queue.append((new_X, new_Y, dist + 2))
                # else:
                queue.append((new_X, new_Y, dist + 1))