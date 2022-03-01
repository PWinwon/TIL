import sys
import heapq

N = int(input())

h = []

for n in range(N):
    x = int(sys.stdin.readline().strip())
    if x:
        heapq.heappush(h, (abs(x), x))
    else:
        if h:
            print(heapq.heappop(h)[1])
        else:
            print(0)
