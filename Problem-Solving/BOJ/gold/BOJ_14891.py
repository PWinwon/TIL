import sys
from collections import deque

input = sys.stdin.readline


def rotate_wheel(n, chk):
    if chk == 1:
        temp = que[n].pop()
        que[n].appendleft(temp)
    else:
        temp = que[n].popleft()
        que[n].append(temp)
    return


que = [deque(list(input().strip())) for _ in range(4)]

K = int(input().strip())

for k in range(K):
    a, b = map(int, input().split())
    a -= 1
    lst = [[a, b]]
    if a == 0:
        # 1번이 돌아가는지 체크
        if que[0][2] != que[1][6]:
            lst.append([1, -b])
            # 2번이 돌아가나?
            if que[1][2] != que[2][6]:
                lst.append([2, b])
                # 3번이 돌아가나?
                if que[2][2] != que[3][6]:
                    lst.append([3, -b])
    elif a == 1:
        # 0번이 돌아가나?
        if que[1][6] != que[0][2]:
            lst.append([0, -b])
        if que[1][2] != que[2][6]:
            lst.append([2, -b])
            if que[2][2] != que[3][6]:
                lst.append([3, b])
    elif a == 2:
        if que[2][2] != que[3][6]:
            lst.append([3, -b])
        if que[2][6] != que[1][2]:
            lst.append([1, -b])
            if que[1][6] != que[0][2]:
                lst.append([0, b])
    else:
        if que[3][6] != que[2][2]:
            lst.append([2, -b])
            if que[2][6] != que[1][2]:
                lst.append([1, b])
                if que[1][6] != que[0][2]:
                    lst.append([0, -b])

    for x, y in lst:
        rotate_wheel(x, y)

result = 0
score = 1
for q in que:
    if q[0] == '1':
        result += score
    score *= 2
print(result)


