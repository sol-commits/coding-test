import sys
from collections import defaultdict

def solution(num_plugs, items_order):
    """
    count: 멀티탭 구멍의 개수
    items_order: 충전을 해야하는 용품의 사용 순서
    items_order로 item을 충전하면서 플러그를 빼는 최소 횟수
    
    1 <= count <= 100, 1 <= len(items_order) <= 100
    
    - 필요한 자료구조: 딕셔너리
    - 엣지 케이스: 
    3 12 -> 3번
    1 2 3 2 4 6 2 3 1 3 1 2
    - 1
    - 1, 2
    - 1, 2, 3
    - 1, 2, 3
    - 6, 2, 3 -> 1번
    - 6, 2, 3
    - 6, 2, 3
    - 6, 1, 3 -> 2번
    - 6, 1, 3
    - 6, 1, 3
    - 6, 1, 2 -> 3번
    
    총 시간 복잡도: O(10000log(100))
    핵심 아이디어: 지금 위치에서 가장 늦게 등장하는 아이템부터 제거
    """  
    
    # count 를 min_heap
    plugged_in = []
    plugged_in_items = {}
    
    # items의 딕셔너리로 items 가 쓰이는 횟수를 저장
    item_charge_order = defaultdict(list)
    for order, item in enumerate(items_order): # O(100)
        if len(item_charge_order[item]) == 0:
            item_charge_order[item].append(101)
        item_charge_order[item].append(order)
    
    for item in item_charge_order.keys():
        item_charge_order[item].sort(key=lambda value: -value) # 내림차순으로 정렬
    unplug_count = 0
    
    for item in items_order: # O(100)
        item_charge_order[item].pop()
        if item not in plugged_in_items or not plugged_in_items[item]:
            if len(plugged_in) >= num_plugs:
                # O(100log(100))
                plugged_in.sort(key=lambda key: item_charge_order[key][-1]) # 제일 멀리있는 것을 제외
                plugged_in_items[plugged_in.pop()] = False
                unplug_count += 1
            plugged_in.append(item)
            plugged_in_items[item] = True

    return unplug_count
    
if __name__ == "__main__":
    input = sys.stdin.readline
    N, K = list(map(int, input().split()))
    items_order = list(map(int, input().split()))
    print(solution(N, items_order))
    