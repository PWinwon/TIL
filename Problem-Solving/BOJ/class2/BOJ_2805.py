N, M = map(int, input().split())

trees = list(map(int, input().split()))

l, r = 0, max(trees)
check = 0

while l <= r:
    h = (l+r) // 2
    total = 0
    for n in range(N):
        if trees[n] > h:
            total += trees[n] - h
    if total >= M:
        check = max(check, h)
        l = h + 1
    else:
        r = h - 1

print(check)