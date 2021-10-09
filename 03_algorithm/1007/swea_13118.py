# def my_func(s, e):
#     if s == e:
#         return s
#     mid = (s+e)//2
#     left = my_func(s, mid)
#     right = my_func(mid+1, e)
#     if left + lst[left] > right + lst[right]:
#         return left
#     else:
#         return right
#
#
# T = int(input())
#
# for tc in range(1, T+1):
#     lst = list(map(int, input().split()))
#     N = lst[0]
#     lst = lst[1:]
#     result = 0
#     start = 1
#     end = lst[0]
#     while end < N-1:
#         start = my_func(start, end)
#         end = start + lst[start]
#         result += 1
#     print('#{} {}'.format(tc, result))

###################################################################
# 교수님 풀이

def dfs(now, cnt) :
    if now > N : # 고려 x
        return
    if visited[now] <= cnt : return # 백트래킹
    visited[now] = cnt
    if now == N :
        return
    # next = now + (1~lst[now])
    for dist in range(1,lst[now] + 1):
        dfs(now + dist , cnt + 1)
    return

T = int(input())
for tc in range(1, T + 1)  :
    lst = list(map(int ,input().split()))
    N = lst[0] # 종점
    visited = [999] * (N+1) # 탐색을 했을때 지금까지의 최소 교환횟수가 저장이 되어있다.
    dfs(1,0)
    print("#{} {}".format(tc, visited[N] - 1))