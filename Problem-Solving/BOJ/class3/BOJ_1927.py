import sys
import heapq

heap = []

N = int(sys.stdin.readline().strip())

for n in range(N):
    x = int(sys.stdin.readline().strip())
    if x > 0:
        heapq.heappush(heap, x)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)