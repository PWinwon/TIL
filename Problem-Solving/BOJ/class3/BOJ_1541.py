temp = input().split('-')
result = []
for t in temp:
    x = t.split('+')
    x_sum = 0
    for s in x:
        x_sum += int(s)
    result.append(x_sum)


chk = False
for r in result:
    if chk:
        res -= r
    else:
        res = r
        chk = True

print(res)