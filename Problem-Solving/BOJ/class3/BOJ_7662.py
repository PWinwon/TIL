import sys
import heapq


def my_func(arr):
    while arr and used[arr[0][1]] == 0:
        heapq.heappop(arr)


T = int(input())

for t in range(T):
    K = int(input())
    min_heap = []
    max_heap = []
    used = [0] * 1000000
    for k in range(K):
        oper, num = sys.stdin.readline().split()
        num = int(num)
        if oper == "I":
            heapq.heappush(min_heap, (num, k))
            heapq.heappush(max_heap, (num*(-1), k))
            used[k] = 1
        elif oper == "D":
            if num > 0:
                my_func(max_heap)
                if max_heap:
                    used[max_heap[0][1]] = 0
                    heapq.heappop(max_heap)

            elif num < 0:
                my_func(min_heap)
                if min_heap:
                    used[min_heap[0][1]] = 0
                    heapq.heappop(min_heap)

    my_func(max_heap)
    my_func(min_heap)


    if max_heap:
        print('{} {}'.format((max_heap[0][0])*(-1), min_heap[0][0]))
    else:
        print("EMPTY")