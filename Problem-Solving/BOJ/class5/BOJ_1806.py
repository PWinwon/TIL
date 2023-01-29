import sys

input = sys.stdin.readline

N, S = map(int, input().split())
lst = list(map(int, input().split()))

l_idx = 0
r_idx = 0

s = 0
flag = False

while r_idx < N:
    s += lst[r_idx]
    r_idx += 1
    if s >= S:
        flag = True
        break

if flag:
    result = r_idx - l_idx

    while l_idx < N and r_idx < N:
        if s >= S:
            s -= lst[l_idx]
            l_idx += 1
        else:
            s += lst[r_idx]
            r_idx += 1
            if (r_idx - l_idx) >= result:
                s -= lst[l_idx]
                l_idx += 1
        if s >= S and (r_idx - l_idx) < result:
            result = r_idx - l_idx

    while l_idx < N:
        if s >= S:
            s -= lst[l_idx]
            l_idx += 1
            if s >= S and (r_idx - l_idx) < result:
                result = r_idx - l_idx
        else:
            break
    print(result)

else:
    print(0)

