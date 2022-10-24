import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

lst = [0] * 7
ans = -1
ans_idx = -1

for x in [a, b, c]:
    lst[x] += 1

for i in range(7):
    if ans <= lst[i]:
        ans = lst[i]
        ans_idx = i

if ans == 1:
    print(100 * ans_idx)
elif ans == 2:
    print(1000 + ans_idx * 100)
else:
    print(10000 + ans_idx * 1000)