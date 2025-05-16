import sys

def fill_character(board, char_arr, row, col):
    for c in char_arr:
        board[row][col] = c
        row += 1
    return (0, col + 1)
def solution(s, num):
    """
    각 숫자의 가로: s+2, 세로: 2s+3
    num: 모니터에 나타내야하는 수(string)
    '-'와 '|'를 이용해서 출력
    - 각 숫자 사이에는 공백이 한 칸 있어야 함
    
    1 <= s <= 10
    0 <= num <= 9,999,999,999
    
    총 시간 복잡도: O(20 * 20)
    핵심 아이디어: 구현
    """  
    a = list(' ' + ('|' * s) + ' ' + ('|' * s) + ' ')
    b = list(' ' + (' ' * s) + ' ' + ('|' * s) + ' ')
    c = list('-' + (' ' * s) + '-' + (' ' * s) + '-')
    d = list(' ' + ('|' * s) + ' ' + (' ' * s) + ' ')
    e = list(' ' + (' ' * s) + '-' + (' ' * s) + ' ')
    f = list('-' + (' ' * s) + ' ' + (' ' * s) + ' ')
    g = list('-' + (' ' * s) + ' ' + (' ' * s) + '-')
    blank = list(' ' * (2*s+1))
    dict = {
        '1': [blank, blank, a], '2': [b, c, d],
        '3': [blank, c, a], '4': [d, e, a], '5': [d, c, b],
        '6': [a, c, b], '7': [blank, f, a], '8': [a, c, a],
        '9': [d, c, a], '0': [a, g, a]
    }
    
    display_w = (s+2) * len(num) + (len(num) - 1)
    display_h = 2*s + 3
    display = list([' '] * display_w for _ in range(display_h))
    cur_row, cur_col = 0, 0
    for n in num:
        num_display = dict[n]
        cur_row, cur_col = fill_character(display, num_display[0], cur_row, cur_col)
        for _ in range(s):
            cur_row, cur_col = fill_character(display, num_display[1], cur_row, cur_col)
        cur_row, cur_col = fill_character(display, num_display[2], cur_row, cur_col)
        cur_col += 1
        
    return display
            
if __name__ == "__main__":
    input = sys.stdin.readline
    s, num = input().split()
    s = int(s)
    for str in solution(s, num):
        print("".join(str))
