import sys

def dfs(n, c):
    global lst_len, M
    if n == M:
        print(' '.join(map(str, result)))
        return

    for i in range(c, lst_len):
        result.append(sorted_lst[i])
        dfs(n+1, i)
        result.pop()
    return


N, M = map(int, input().split())

lst = list(map(int, input().split()))
sorted_lst = list(set(lst))
sorted_lst.sort()
lst_len = len(sorted_lst)

result = []
dfs(0, 0)

