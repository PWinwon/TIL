N = int(input())

lst = []

for n in range(N):
    k, t = map(int, input().split())
    lst.append((k, t))

result = []
for i in range(N):
    i_rnk = 1
    ik = lst[i][0]
    it = lst[i][1]
    for j in range(N):
        if ik < lst[j][0] and it < lst[j][1]:
            i_rnk += 1
    result.append(i_rnk)

print(' '.join(map(str, result)))