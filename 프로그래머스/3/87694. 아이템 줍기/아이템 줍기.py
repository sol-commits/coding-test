from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    """
    Args:
        rectangle: 직사각형이 담긴 2차원 배열
        characterX, Y: 캐릭터의 x좌표, y좌표
        itemX, Y: 아이템의 x좌표, y좌표
    Returns:
        캐릭터가 아이템을 줍기 위해 이동해야 하는 최소 거리
    """
    scale = 2
    map_limit = 50*scale+1
    map = [[0] * (map_limit) for _ in range(map_limit + 1)]
    moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    
    for x1, y1, x2, y2 in rectangle:
        for x in range(x1*scale, x2*scale + 1):
            for y in [y1*scale, y2*scale]:
                map[x][y] = 1
        for y in range(y1*scale, y2*scale + 1):
            for x in [x1*scale, x2*scale]:
                map[x][y] = 1
    
    for x1, y1, x2, y2 in rectangle:
        for x in range(x1*scale+1, x2*scale):
            for y in range(y1*scale+1, y2*scale):
                map[x][y] = 0
    
    characterX, characterY = characterX*scale, characterY*scale
    itemX, itemY = itemX*scale, itemY*scale
    
    queue = deque([(characterX, characterY, 0)])
    map[characterX][characterY] = 0
    
    while queue:
        cur_X, cur_Y, dist = queue.popleft()
        if (cur_X, cur_Y) == (itemX, itemY):
            return dist // scale
        
        for move_X, move_Y in moves:
            new_X, new_Y = cur_X + move_X, cur_Y + move_Y
            if 0 < new_X < map_limit and 0 < new_Y < map_limit and map[new_X][new_Y] == 1:
                map[new_X][new_Y] = 0
                queue.append((new_X, new_Y, dist + 1))