import sys

input = sys.stdin.readline


def my_func(n, s):
    global V, result, result_node
    if s > result:
        result = s
        result_node = n
    for x, y in MAP[n]:
        if used[x] == 0:
            used[x] = 1
            my_func(x, s + y)
            used[x] = 0

    return


V = int(input().strip())

MAP = [[] for _ in range(V)]

for v in range(V):
    temp = list(map(int, input().split()))
    x = temp[0] - 1
    idx = 1
    while True:
        if temp[idx] == -1:
            break
        MAP[x].append([temp[idx]-1, temp[idx+1]])
        idx += 2

result = 0
result_node = -1
used = [0] * (V)
used[0] = 1
my_func(0, 0)
used[0] = 0

used[result_node] = 1
my_func(result_node, 0)
print(result)