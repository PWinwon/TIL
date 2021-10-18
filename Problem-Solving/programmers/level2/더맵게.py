import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    chk = 0
    while len(scoville) > 1:
        for i in range(len(scoville)):
            if scoville[i] < K:
                break
        else:
            chk = 1
            break
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville,a + b*2)
        answer += 1
    if chk == 0 and scoville[0] < K:
        return -1
    return answer