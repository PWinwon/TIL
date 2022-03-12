import heapq


def solution(n, start, end, roads, traps):
    answer = 0
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

    h = []
    # 현재위치, 걸린시간, trap -1 or 1 -1: 발동중 1: 중지 0: 상관 x
    heapq.heappush(h, [0, start, tMAP])
    de = -1
    while h:
        time, loca, chk = heapq.heappop(h)
        if loca == end:
            answer = time
            break

        for i in range(1, n+1):
            # 발동중
            xchk = chk

            if xchk[loca] ^ xchk[i] < 0:
                if MAP[i][loca]:
                    xtime = time + MAP[i][loca]
                else:
                    continue

            else:
                if MAP[loca][i]:
                    xtime = time + MAP[loca][i]
                else:
                    continue

            if xchk[i] == 0:
                heapq.heappush(h, [xtime, i, xchk])
            else:
                xchk[i] *= -1
                heapq.heappush(h, [xtime, i, xchk])
    return answer