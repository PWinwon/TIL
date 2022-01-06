# 1 == 1
# 2 ~ 7 == 2
# 8 ~ 19 == 3
# 20 ~ 37 == 4

N = int(input())

sum = 2
cnt = 0
while sum <= N:
    sum += 6 * cnt
    cnt += 1
if N == 1:
    print(1)
else:
    print(cnt)