import heapq


def solution(jobs):
    answer = 0
    for i in jobs:
        answer -= i[0]
    start = -1
    now = 0
    cnt = 0
    h = []
    while cnt < len(jobs) or h:
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(h, j[1])
                cnt += 1
        if h:
            temp = heapq.heappop(h)
            start = now
            answer += temp + now
            now += temp
        else:
            now += 1

    return answer//len(jobs)