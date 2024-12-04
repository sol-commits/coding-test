# mode : 0 또는 1
# 
def solution(code):
    ret = ''
    mode = 0 # 시작할 때 mode는 0
    idx = 0
    
    while idx < len(code):
        if mode == 0:
            if code[idx] != '1' and idx % 2 == 0:
                ret += code[idx]
            elif code[idx] == '1':
                mode = 1
        else:
            if code[idx] != '1' and idx % 2 == 1:
                ret += code[idx]
            elif code[idx] == '1':
                mode = 0
        idx += 1
        
    return ret if ret != '' else 'EMPTY'