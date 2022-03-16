N = int(input())

lst = list(map(int, input().split()))
lst_s = sorted(lst)

result = dict()
cnt = 0

for l in lst_s:
    if l in result.keys():
        continue
    result[l] = cnt
    cnt += 1

res = []
for l in lst:
    res.append(result[l])

print(' '.join(map(str, res)))