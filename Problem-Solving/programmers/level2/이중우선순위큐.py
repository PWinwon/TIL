import heapq


def solution(operations):
    my_func = lambda x: x*(-1)
    answer = [0, 0]
    heap = []
    chk = 0
    for oper in operations:
        o, num = oper.split()
        num = int(num)
        if o == 'I':
            heapq.heappush(heap, num)
        elif num < 0 and heap:
            if chk == 2:
                heap = list(map(my_func, heap))
                heapq.heapify(heap)
                chk = 1
            heapq.heappop(heap)
        elif num > 0 and heap:
            if chk == 0 or chk == 1:
                heap = list(map(my_func, heap))
                heapq.heapify(heap)
                chk = 2
            heapq.heappop(heap)
    if chk == 2:
        heap = list(map(my_func, heap))
    if heap:
        answer[0] = max(heap)
        answer[1] = min(heap)
    return answer