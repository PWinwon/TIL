import sys

input = sys.stdin.readline


def my_shuffle(l, r, i):
    global N
    new_lst = []
    l_idx, r_idx = 0, 0

    while l_idx < N//2:
        new_lst.append(l[l_idx])
        if l_idx >= i:
            new_lst.append(r[r_idx])
            r_idx += 1
        l_idx += 1

    while r_idx < N//2:
        new_lst.append(r[r_idx])
        r_idx += 1

    new_l, new_r = new_lst[0:N//2], new_lst[N//2:]
    return new_l, new_r


def sort_chk(le, ri, c):
    global result, sol1, sol2
    temp = le + ri
    if temp == sol1 or temp == sol2:
        if result > c:
            result = c
        return True

    return False


def my_dfs(left, right, cnt):
    global result, N
    if cnt >= result:
        return

    flag = sort_chk(left, right, cnt)
    if flag:
        return

    for i in range(N//2):
        new_left, new_right = my_shuffle(left, right, i)
        my_dfs(new_left, new_right, cnt+1)
        new_left, new_right = my_shuffle(right, left, i)
        my_dfs(new_left, new_right, cnt + 1)
    return


T = int(input().strip())

for tc in range(1, T+1):
    N = int(input().strip())
    lst = list(map(int, input().split()))
    card1, card2 = lst[0:N//2], lst[N//2:]

    sol1 = sorted(lst)
    sol2 = sorted(lst, reverse=True)

    result = 6
    my_dfs(card1, card2, 0)
    if result >= 6:
        print('#{} {}'.format(tc, -1))
    else:
        print('#{} {}'.format(tc, result))