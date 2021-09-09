import heapq

def solution(operations):
    answer = [0, 0]
    h = []
    for oper in operations:
        temp, num = oper.split()
        num = int(num)
        if temp == 'I':
            heapq.heappush(h, num)
        elif num < 0 and h:
            heapq.heappop(h)
        elif num > 0 and h:
            h.pop()
    if h:
        answer[0] = max(h)
        answer[1] = min(h)
    return answer