lst = []
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i != j and i != k and j != k:
                lst.append(str(i)+str(j)+str(k))


def strk_cnt(num, st):
    result = []
    for n in lst:
        cnt = 0
        if n[0] == num[0]:
            cnt += 1
        if n[1] == num[1]:
            cnt += 1
        if n[2] == num[2]:
            cnt += 1
        if cnt == st:
            result.append(n)
    return result


def ball_cnt(num, bl):
    result = []
    for n in lst:
        cnt = 0
        if n[0] != num[0] and n[0] == num[1] or n[0] == num[2]:
            cnt += 1
        if n[1] != num[1] and n[1] == num[2] or n[1] == num[0]:
            cnt += 1
        if n[2] != num[2] and n[2] == num[0] or n[2] == num[1]:
            cnt += 1
        if cnt == bl:
            result.append(n)
    return result


N = int(input())
for i in range(N):
    number, strk, ball = map(int, input().split())
    lst = strk_cnt(str(number), strk)
    lst = ball_cnt(str(number), ball)
print(len(lst))