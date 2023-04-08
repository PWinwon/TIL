import sys
from collections import deque

sys.stdin = open('input.txt', 'r')


def myDFS(chk, newC, r, c, ret):
    global N
    for i in range(4):
        yr, xr = r+dr[i], c+dc[i]
        if yr < 0 or yr >= N or xr < 0 or xr >= N:
            continue
        if MAP[yr][xr] != chk:
            continue
        if artMAP[yr][xr] >= 0:
            continue
        artMAP[yr][xr] = newC
        ret = myDFS(chk, newC, yr, xr, ret+1)
    return ret


def oper_art():
    global N
    ans = 0
    # artMAP과 used 초기화
    for r in range(N):
        for c in range(N):
            artMAP[r][c] = -1
            used[r][c] = False

    # artMAP 재구성
    # artMAP 재구성에 사용될 color idx 변수 초기화
    # 총 구역 개수 저장
    # 각 그룹의 원소 개수 저장도 해야되네..?
    newColor = 0
    groupCnt = 0
    colors = []
    groupEleCnt = []
    for r in range(N):
        for c in range(N):
            if artMAP[r][c] < 0:
                artMAP[r][c] = newColor
                cnt = myDFS(MAP[r][c], newColor, r, c, 1)
                newColor += 1
                groupCnt += 1
                colors.append(MAP[r][c])
                groupEleCnt.append(cnt)

    # 예술성 검사 및 계산
    # artMAP 기준으로 각 구역을 돌면서 접하는 친구 확인하기
    # 접하는 친구와 접하는 면


    for r in range(N):
        for c in range(N):
            # used[r][c] 가 False라면 탐색안한 구역
            if not used[r][c]:
                idx = artMAP[r][c]

                que = deque()
                # 접하는 면 계산해서 넣을 temp
                temp = [0] * groupCnt

                que.append([r, c])
                used[r][c] = True

                while que:
                    y, x = que.popleft()
                    for i in range(4):
                        yr, xr = y+dr[i], x+dc[i]
                        if yr < 0 or yr >= N or xr < 0 or xr >= N:
                            continue
                        if used[yr][xr]:
                            continue
                        # 다르면 temp에 저장 >> 접하는 면이기 때문
                        if artMAP[r][c] != artMAP[yr][xr]:
                            temp[artMAP[yr][xr]] += 1
                            continue
                        que.append([yr, xr])
                        used[yr][xr] = True

                de = -1
                for i in range(groupCnt):
                    if idx == i:
                        continue
                    # 접하는 면이 있고, 해당 원소의 개수가 남아있는경우 ( 이전 탐색에서 접하는 면과 중복 계산되지 않도록 하기 위함 )
                    if temp[i] and groupEleCnt[i]:
                        ans += (groupEleCnt[idx] + groupEleCnt[i]) * colors[idx] * colors[i] * temp[i]
                groupEleCnt[idx] = 0
    return ans


def cross_lotation():
    global N, tempMAP
    r, c = N//2, N//2
    tempMAP[r][c] = MAP[r][c]
    i = 1
    while i <= N//2:
        rU, rL, rD, rR = r+dr[0]*i, r+dr[1]*i, r+dr[2]*i, r+dr[3]*i
        cU, cL, cD, cR = c+dc[0]*i, c+dc[1]*i, c+dc[2]*i, c+dc[3]*i
        tempMAP[rU][cU], tempMAP[rL][cL], tempMAP[rD][cD], tempMAP[rR][cR] = MAP[rR][cR], MAP[rU][cU], MAP[rL][cL], MAP[rD][cD]
        i += 1
    return


def square_loation():
    global N, tempMAP
    # 1, 2, 3, 4 분면 범위를 나눠서 궈궈 해야함
    mid = N // 2
    sub_square_lotaion(0, 0, mid)
    sub_square_lotaion(mid+1, 0, mid)
    sub_square_lotaion(0, mid+1, mid)
    sub_square_lotaion(mid+1, mid+1, mid)

    for r in range(N):
        for c in range(N):
            MAP[r][c] = tempMAP[r][c]
    return


def sub_square_lotaion(sr, sc, n):
    global tempMAP
    for r in range(n):
        for c in range(n):
            tempMAP[c+sr][n-r-1+sc] = MAP[r+sr][c+sc]
    return

input = sys.stdin.readline
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

N = int(input().strip())

MAP = [list(map(int, input().split())) for _ in range(N)]
artMAP = [[-1 for _ in range(N)] for _ in range(N)]
used = [[False for _ in range(N)] for _ in range(N)]
colors = []
groupEleCnt = []

answer = 0
for i in range(4):
    # 예술성 점수 구하기
    answer += oper_art()
    # i 가 3이면 즉, 4회전 이후 점수는 구할 필요가 없음
    if i == 3:
        continue
    tempMAP = [[0 for _ in range(N)] for _ in range(N)]
    # 십자 회전
    cross_lotation()
    # 각 사각형 회전
    square_loation()
    de = -1

print(answer)