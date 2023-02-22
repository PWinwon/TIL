import sys

# sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline


def find(x):
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y
    return


N, M = map(int, input().split())
knows = list(map(int, input().split()))
knows_lst = [0 for _ in range(N+1)]
for i in range(1, knows[0]+1):
    knows_lst[knows[i]] = 1

parties = [list(map(int, input().split())) for _ in range(M)]

parents = [i for i in range(N+1)]

if knows[0] == 0:
    print(M)
else:
    result = 0
    for party in parties:
        for i in range(1, party[0]):
            union(party[i], party[i + 1])
    for i in range(1, N+1):
        if knows_lst[i]:
            knows_lst[find(i)] = 1
    for party in parties:
        flag = True
        for i in range(1, party[0]+1):
            if knows_lst[find(party[i])]:
                flag = False
                break
        if flag:
            result += 1
    print(result)

