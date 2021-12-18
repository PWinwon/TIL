from collections import deque


def que_chk(n):
    global que

    for q, i in que:
        if q > n:
            return False

    return True


T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    que = deque()

    for i in range(N):
        if i == M:
            que.append([lst[i], True])
        else:
            que.append([lst[i], False])
    cnt = 1
    while que:
        num, flag = que.popleft()

        ret = que_chk(num)
        if ret:
            if flag:
                print(cnt)
                break
            else:
                cnt += 1
        else:
            que.append([num, flag])
