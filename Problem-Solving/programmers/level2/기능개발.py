from collections import deque

def solution(progresses, speeds):
    answer = []
    q_pro = deque(progresses)
    q_spd = deque(speeds)
    cnt = 0
    while q_pro:
        if q_pro[0] >= 100:
            q_pro.popleft()
            q_spd.popleft()
            cnt += 1
            continue
        if cnt > 0:
            answer.append(cnt)
            cnt = 0
        for i in range(len(q_pro)):
            q_pro[i] += q_spd[i]
    answer.append(cnt)
    return answer