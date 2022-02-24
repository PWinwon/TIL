import sys
import heapq

N = int(input())

heap = []
for n in range(N):
    num = int(sys.stdin.readline().strip())
    if num:
        heapq.heappush(heap, (-num, num))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)