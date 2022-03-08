from collections import deque


def solution(n, start, end, roads, traps):
    answer = 999999999999999999999999999999
    tMAP = [0] * (n + 1)
    MAP = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for trap in traps:
        tMAP[trap] = 1

    for road in roads:
        road_s, road_e, time = road
        if MAP[road_s][road_e] == 0:
            MAP[road_s][road_e] = time
        if MAP[road_s][road_e] and MAP[road_s][road_e] > time:
            MAP[road_s][road_e] = time

    que = deque()
    # 현재위치, 걸린시간, trap -1 or 1 -1: 발동중 1: 중지 0: 상관 x
    que.append([start, 0, tMAP])
    de = -1
    while que:
        location, time, chk = que.popleft()
        if location == end and answer > time:
            answer = time
            break

        if tMAP[location] < 0:
            for i in range(1, n+1):
                if MAP[i][location]:
                    xtime = time + MAP[i][location]
                else:
                    continue
                xchk = chk
                xchk[i] *= -1
                que.append([i, xtime, xchk])
        else:
            for i in range(1, n+1):
                if MAP[location][i]:
                    xtime = time + MAP[location][i]
                else:
                    continue
                xchk = chk
                xchk[i] *= -1
                que.append([i, xtime, xchk])

    return answer