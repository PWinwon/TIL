import sys

input = sys.stdin.readline


def b_f(n):
    for i in range(n):
        for a, b, c in edges:
            if dist[b] > dist[a] + c:
                if i == n-1:
                    return True
                dist[b] = dist[a] + c
    return False


T = int(input().strip())

for tc in range(T):
    N, M, W = map(int, input().split())

    edges = []
    dist = [0] * (N+1)

    for m in range(M):
        s, e, t = map(int, input().split())
        edges.append([s, e, t])
        edges.append([e, s, t])

    for w in range(W):
        s, e, t = map(int, input().split())
        edges.append([s, e, -t])

    ret = b_f(N)
    if ret:
        print("YES")
    else:
        print("NO")