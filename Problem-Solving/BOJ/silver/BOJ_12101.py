import sys

input = sys.stdin.readline


def my_func(s, ans):
    global cnt, N, K, result
    if result != -1:
        return
    if s > N:
        return
    if s == N:
        cnt += 1
        if cnt == K:
            result = '+'.join(map(str, ans))
            return
    for i in range(1, 4):
        ans.append(i)
        my_func(s + i, ans)
        ans.pop()
    return


N, K = map(int, input().split())
cnt = 0
result = -1
my_func(0, [])
print(result)