from collections import deque

def move_cnt(location, target):
    total_cnt = 1
    if location > target:
        total_cnt += location - target
    else:
        total_cnt += target - location
    return total_cnt


def move_loc(move, tr, loc):
    if move != 0 and tr > loc:
        loc += move
        if loc > tr:
            loc = tr
    elif move != 0 and loc > tr:
        loc -= move
        if loc < tar:
            loc = tar
    return loc


test_case = int(input())
for tc in range(test_case):
    lst = list(input().split())
    loop = int(lst[0])
    lst_btn = deque()
    for i in range(1, loop+1):
        lst_btn.append([lst[i*2-1], lst[i*2]])
    b = 1
    o = 1
    result = 0
    b_move = 0
    o_move = 0
    while lst_btn:
        temp = lst_btn.popleft()
        tar = int(temp[1])
        if temp[0] == 'B':
            b = move_loc(b_move, tar, b)
            res = move_cnt(b, tar)
            o_move += res
            result += res
            b = tar
            b_move = 0
        elif temp[0] == 'O':
            o = move_loc(o_move, tar, o)
            res = move_cnt(o, tar)
            b_move += res
            result += res
            o = tar
            o_move = 0
    print('#{} {}'.format(tc+1, result))