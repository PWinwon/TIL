from collections import deque


def my_oper(n, o):
    if o == 0:
        return n + 1
    elif o == 1:
        return n - 1
    elif o == 2:
        return n * 2
    elif o == 3:
        return n - 10


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    used = [0] * 1000001
    que = deque()
    que.append(N)
    used[N] = 1
    result = 0
    while que:
        num = que.popleft()
        if num == M:
            result = used[num]
            break
        for i in range(4):
            n = my_oper(num, i)
            if n > 1000000:
                continue
            if used[n] != 0:
                continue
            used[n] = used[num] + 1
            que.append(n)
    print('#{} {}'.format(tc, result-1))


# 교수님 풀이

# from collections import deque
#
#
# def bfs(n,m) :
#     # 큐 / visited 큐에 재등록 방지
#     qu = deque()
#     visited = [0] * 1000001
#
#     # 시작 노드 큐에 등록하기(방문 예약)
#     visited[n] = 1 # 재등록 방지
#     qu.append((n, 0)) # (숫자, level) level : 연산 횟수
#
#     # BFS
#     while qu :
#         num , level = qu.popleft()
#         if num == m : # BFS 중에 m 나옴
#             return level # m 이 처음 탐색되었을때 연산횟수를 리턴 ----> 최소 연산횟수를 구할수 있다.
#
#         # next 노드 큐에 등록 (방문예약) -> for 문으로 묶기
#         if 1 <= num+1 <= 1000000 and visited[num+1] == 0:
#             visited[num+1] = 1
#             qu.append((num+1, level + 1))
#         if 1 <= num - 1 <= 1000000 and visited[num-1] == 0:
#             visited[num-1] = 1
#             qu.append((num-1, level + 1))
#         if 1 <= num * 2 <= 1000000 and visited[num * 2] == 0:
#             visited[num*2] =1
#             qu.append((num*2, level + 1))
#         if 1 <= num - 10 <= 1000000 and visited[num - 10] == 0 :
#             visited[num-10] = 1
#             qu.append((num-10, level + 1))
#
#     return - 1
#
# T = int(input())
# for tc in range(1,T+1) :
#     N,M = map(int, input().split())
#     ret = bfs(N,M)
#     print("#{} {}".format(tc, ret))
