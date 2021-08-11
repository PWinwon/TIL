#####################################################################################
# min_max

test_case = int(input())

for t in range(test_case):
    n = int(input())
    list_a = list(map(int, input().split()))
    min_val = 1000000
    max_val = 1

    for a in list_a:
        if max_val < a:
            max_val = a
        if min_val > a:
            min_val = a
    print(f'#{t+1} {max_val - min_val}')


#####################################################################################
#전기버스

test_case = int(input())

for t in range(1, test_case+1):
    k, n, m = map(int, input().split())
    m_num = list(map(int, input().split()))
    n_list = [0] * (n+1)
    for mn in m_num:
        n_list[mn] = 1
    result = 0

    idx = n
    while idx - k > 0:
        chk = 0
        for idx_2 in range(idx-k, idx):
            if n_list[idx_2] == 1:
                idx = idx_2
                result += 1
                break
            else :
                chk += 1
        if chk == k:
            result = 0
            break
    print('#{} {}'.format(t, result))

#####################################################################################
# 구간합
test_list = [3, 2, 7, 5, 9, 11]
chk = 0
for tl in test_list:
    if tl == 7:
        chk = 1
        break
if chk == 1:
    print('존재')
else:
    print('존재 x')

#####################################################################################
# 구간합

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(8):
    for j in range(i, i+3):
        print(lst[j], end=' ')
    print('')

#####################################################################################
# 구간합

test_case = int(input())

for t in range(1, test_case+1):
    n, m = map(int, input().split())
    n_lst = list(map(int, input().split()))
    max_val = 0
    min_val = 10000 * m
    for i in range(n-m+1):
        total_part = 0
        for j in range(i, i+m):
            total_part += n_lst[j]
        if total_part > max_val:
            max_val = total_part
        if total_part < min_val:
            min_val = total_part

    print('#{} {}'.format(t, max_val - min_val))

#####################################################################################
# 구간합 완전탐색 x prefix

test_case = int(input())

for t in range(1, test_case+1):
    n, m = map(int, input().split())
    n_lst = list(map(int, input().split()))
    sum_lst = [0]
    for x in range(n):
        sum_lst.append(sum_lst[x] + n_lst[x])
    max_val = 0
    min_val = 10000 * m
    for idx in range(m, n+1):
        sum_val = sum_lst[idx] - sum_lst[idx-m]
        if sum_val > max_val:
            max_val = sum_val
        if sum_val < min_val:
            min_val = sum_val
    print('#{} {}'.format(t, max_val-min_val))

#####################################################################################
# 구간합 슬라이딩 윈도우

lst = [5, 3, 2, 1, 7, 9, 10, 19, 20, 30]
sum = 10 # 첫 구간 합
print(sum)
for idx in range(3, len(lst)):
    sum -= lst[idx-3]
    sum += lst[idx]
    print(sum)

#####################################################################################
# 구간합 슬라이딩 윈도우

test_case = int(input())

for t in range(test_case):
    n, m = map(int, input().split())
    num_lst = list(map(int, input().split()))

    total = 0
    max_val = 0
    min_val = 10000 * m
    for idx in range(m-1, n):
        if idx == m-1:
            for i in range(m):
                total += num_lst[i]
        else:
            total -= num_lst[idx-m]
            total += num_lst[idx]
        if max_val < total:
            max_val = total
        if min_val > total:
            min_val = total
    print('#{} {}'.format(t+1, max_val - min_val))

#####################################################################################
# 숫자카드
test_case = int(input())

for t in range(test_case):
    idx_list = [0] * 10
    n = int(input())
    cards = int(input())
    for i in range(n):
        idx_list[cards % 10] += 1
        cards = cards // 10
    max_val = 0
    max_cardnum = 0
    for j in range(10):
        if idx_list[j] >= max_val:
            max_val = idx_list[j]
            max_cardnum = j
    print('#{} {} {}'.format(t+1, max_cardnum, max_val))

#####################################################################################
# 현주의 상자
test_case = int(input())

for t in range(test_case):
    n, q = map(int, input().split())
    boxes = [0] * n
    for i in range(q):
        l, r = map(int, input().split())
        for j in range(l-1, r):
            boxes[j] = i+1
    print('#{}'.format(t+1), end='')
    for box in boxes:
        print(' {}'.format(box), end='')
    print('')

#####################################################################################
# 간단한 소인수 분해
prime_nums = [2, 3, 5, 7, 11]
test_case = int(input())

for t in range(test_case):
    number = int(input())
    prime_cnt = [0] * 5
    idx = 0
    while idx < 5:
        if number % prime_nums[idx] > 0:
            idx += 1
        else:
            prime_cnt[idx] += 1
            number = number // prime_nums[idx]

    print('#{}'.format(t+1), end='')
    for cnt in prime_cnt:
        print(' {}'.format(cnt), end='')
    print('')

#####################################################################################
# flatten
for t in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))
    gap = 0
    while True:
        max_val = 0
        max_idx = 0
        min_val = 100
        min_idx = 0
        for box_idx in range(100):
            if max_val < boxes[box_idx]:
                max_val = boxes[box_idx]
                max_idx = box_idx
            if min_val > boxes[box_idx]:
                min_val = boxes[box_idx]
                min_idx = box_idx
        if dump == 0:
            gap = boxes[max_idx] - boxes[min_idx]
            break
        dump -= 1
        boxes[max_idx] -= 1
        boxes[min_idx] += 1
    print('#{} {}'.format(t, gap))

#####################################################################################
# 오목(모의 코테)

five_board = []
test_list = [0] * 21
five_board.append(test_list)
for i in range(19):
    five_board.append([0] + list(map(int, input().split())) + [0])
five_board.append(test_list)


who_win = 0
for x in range(1, 20):
    for y in range(1, 20):
        if five_board[x][y] > 0 and five_board[x][y] != five_board[x][y-1]:     #가로
            chk = five_board[x][y]
            cnt = 0
            idx_x = x
            idx_y = y
            while True:
                if five_board[idx_x][idx_y] == chk:
                    cnt += 1
                elif cnt == 5:
                    who_win = chk
                    result_x = x
                    result_y = y
                    break
                else:
                    cnt = 0
                    break
                idx_y += 1
        
        if five_board[x][y] > 0 and five_board[x][y] != five_board[x-1][y]:     #세로
            chk = five_board[x][y]
            cnt = 0
            idx_x = x
            idx_y = y
            while True:
                if five_board[idx_x][idx_y] == chk:
                    cnt += 1
                elif cnt == 5:
                    who_win = chk
                    result_x = x
                    result_y = y
                    break
                else:
                    cnt = 0
                    break
                idx_x += 1
        
        if five_board[x][y] > 0 and five_board[x][y] != five_board[x+1][y-1]:     #우상단
            chk = five_board[x][y]
            cnt = 0
            idx_x = x
            idx_y = y
            while True:
                if five_board[idx_x][idx_y] == chk:
                    cnt += 1
                elif cnt == 5:
                    who_win = chk
                    result_x = x
                    result_y = y
                    break
                else:
                    cnt = 0
                    break
                idx_x -= 1
                idx_y += 1
        
        if five_board[x][y] > 0 and five_board[x][y] != five_board[x-1][y-1]:     #우하단
            chk = five_board[x][y]
            cnt = 0
            idx_x = x
            idx_y = y
            while True:
                if five_board[idx_x][idx_y] == chk:
                    cnt += 1
                elif cnt == 5:
                    who_win = chk
                    result_x = x
                    result_y = y
                    break
                else:
                    cnt = 0
                    break
                idx_x += 1
                idx_y += 1
    


print('{}'.format(who_win))
if who_win > 0:
    print('{} {}'.format(result_x, result_y))

