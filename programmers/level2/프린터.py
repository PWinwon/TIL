from collections import deque

def solution(priorities, location):
    answer = 0
    que = deque(priorities)
    que_l = deque([i for i in range(len(priorities))])
    while que:
        temp = que.popleft()
        ll = que_l.popleft()
        for i in range(len(que)):
            if que[i] > temp:
                que.append(temp)
                que_l.append(ll)
                break
        else:
            answer += 1
            if location == ll:
                return answer

    return answer