def my_func(level, s, c):
    global cnt, result, sl, max_val, chk
    total = int(''.join(map(str, s)))
    if chk:
        return
    if total == max_val and level != 0:
        if (cnt-c) % 2:
            s[-1], s[-2] = s[-2], s[-1]
        c = cnt
        total = int(''.join(map(str, s)))
        chk = True
    if c == cnt:
        if result < total:
            result = total
        return
    for i in range(level+1, sl):
        if s[level] <= s[i]:
            s[level], s[i] = s[i], s[level]
            my_func(level+1, s, c+1)
            s[level], s[i] = s[i], s[level]
        my_func(level+1, s, c)
    return


T = int(input())

for tc in range(1, T+1):
    temp = input().split()
    score = list(map(int, list(temp[0])))
    sl = len(score)
    cnt = int(temp[1])
    max_val = int(''.join(map(str, sorted(list(map(int, temp[0])), reverse=True))))
    chk = False
    result = 0
    my_func(0, score, 0)
    print('#{} {}'.format(tc, result))