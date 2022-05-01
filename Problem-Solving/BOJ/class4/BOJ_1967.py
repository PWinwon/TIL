import sys

from collections import deque

input = sys.stdin.readline


def my_bfs(n):
    que = deque()
    used = [-1] * (N)
    que.append(n)
    used[n] = 0

    while que:
        y = que.popleft()

        for x, cnt in MAP[y]:
            if used[x] == -1:
                que.append(x)
                used[x] = used[y] + cnt

    ret_node = -1
    ret_max = -1

    for i in range(N):
        if ret_max < used[i]:
            ret_max = used[i]
            ret_node = i

    return (ret_node, ret_max)


N = int(input().strip())

MAP = [[] for _ in range(N)]

for n in range(N-1):
    a, b, c = map(int, input().split())
    MAP[a-1].append([b-1, c])
    MAP[b-1].append([a-1, c])

result = -1
result_node = -1

result_node, result = my_bfs(0)

result_node, result = my_bfs(result_node)

print(result)