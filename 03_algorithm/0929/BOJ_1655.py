import sys
import heapq

N = int(sys.stdin.readline())
max_h = []
min_h = []
result = []
for n in range(N):
    val = int(sys.stdin.readline())
    if len(max_h) == len(min_h):
        heapq.heappush(max_h, (-val, val))
    else:
        heapq.heappush(min_h, (val, val))

    if min_h and max_h[0][1] > min_h[0][1]:
        temp1 = heapq.heappop(max_h)[1]
        temp2 = heapq.heappop(min_h)[1]
        heapq.heappush(min_h, (temp1, temp1))
        heapq.heappush(max_h, (-temp2, temp2))
    result.append(max_h[0][1])

for res in result:
    print(res)
    
    
# import sys
# import heapq
# 
# N = int(sys.stdin.readline())
# max_h = []
# min_h = []
# for n in range(N):
#     val = int(sys.stdin.readline())
#     if min_h:
#         if min_h[0] > val:
#             heapq.heappush(max_h, (-val, val))
#         else:
#             heapq.heappush(min_h, val)
#     else:
#         heapq.heappush(min_h, val)
#     while len(max_h) <= len(min_h):
#         temp = heapq.heappop(min_h)
#         heapq.heappush(max_h, (-temp, temp))
#     while len(max_h) > len(min_h):
#         temp = heapq.heappop(max_h)
#         heapq.heappush(min_h, temp[1])
#     if len(max_h) < len(min_h):
#         print(min_h[0])
#     else:
#         print(max_h[0][1])