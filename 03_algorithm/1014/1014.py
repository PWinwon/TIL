# 1500 번째 ugly number 까지 구하기 - 교수님 풀이

import heapq

ugly = [0] * 1501
th = 1
minheap =[]
heapq.heappush(minheap, 1) # 시작

prev = - 1
while th < 1501:
    now = heapq.heappop(minheap)
    if now == prev : continue

    ugly[th] = now
    th += 1
    # x2 x3 x5 -> minheap
    heapq.heappush(minheap, 2*now)
    heapq.heappush(minheap, 3*now)
    heapq.heappush(minheap, 5*now)
    prev = now
de = -1