#############################################################
# 교수님 풀이

from collections import deque

for _ in range(1,10+1) :
    tc = int(input())
    queue = deque()
    for val in map(int, input().split()):
        queue.append(val)

    t = 1
    while queue[-1] > 0 :
        a= queue.popleft()
        queue.append(a - t)
        t = t % 5 + 1

    # 결과
    queue[-1] = 0
    print("#{}".format(tc),end= ' ')
    while queue :
        print(queue.popleft(),end = ' ')
    print()