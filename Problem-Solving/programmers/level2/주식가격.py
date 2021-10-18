from collections import deque

def solution(prices):
    answer = []
    que = deque(prices)
    while que:
        cnt = 0
        temp = que.popleft()
        for q in que:
            cnt += 1
            if q < temp:
                break
        answer.append(cnt)

    return answer