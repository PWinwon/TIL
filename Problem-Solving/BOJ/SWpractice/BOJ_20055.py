import sys
from collections import deque

# sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N, K = map(int, input().split())

belt = deque(map(int, input().split()))

que = deque()

used = [0 for _ in range(N * 2)]

cnt = 0
for i in range(2*N):
    if belt[i] == 0:
        cnt += 1

answer = 1

while cnt < K:
    next_que = deque()
    # 1. 벨트 한바퀴 돌리기 (벨트 한바퀴 돌리고, 로봇의 인덱스 += 1)
    belt.appendleft(belt.pop())
    for i in range(len(que)):
        used[que[i]] = 0
        que[i] += 1
        used[que[i]] = 1
    while que:
        x = que.popleft()
        if x >= N-1:
            used[x] = 0
            continue
        if used[x+1] == 0 and belt[x+1] != 0:
            belt[x+1] -= 1
            used[x+1] = 1
            used[x] = 0
            next_que.append(x+1)

            if belt[x+1] == 0:
                cnt += 1
        else:
            next_que.append(x)
    if belt[0] != 0:
        next_que.append(0)
        belt[0] -= 1
        used[0] = 1
        if belt[0] == 0:
            cnt += 1
    que = next_que
    if cnt >= K:
        break
    answer += 1

print(answer)