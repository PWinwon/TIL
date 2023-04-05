import sys

# sys.stdin = open('input.txt', 'r')


def init(lst):
    global N, M

    mIdx = 0
    for n in range(N):
        boxes[lst[n]] = [lst[n+N], mIdx]
        # 꼬리일 때
        if (n + 1) % (N // M) == 0:
            tail[mIdx] = lst[n]
            mIdx += 1
            prv[lst[n]] = lst[n-1]
            nxt[lst[n]] = -1
        # 머리일 때
        elif n % (N // M) == 0:
            head[mIdx] = lst[n]
            prv[lst[n]] = -1
            nxt[lst[n]] = lst[n+1]
        # 나머지
        else:
            prv[lst[n]] = lst[n-1]
            nxt[lst[n]] = lst[n+1]
    return


def delete_box(i):
    ret = -1
    if i in boxes.keys() and boxes[i][0] > 0:
        ret = i
        bNum = boxes[i][1]
        # head 라면?
        if prv[i] == -1:
            prv[nxt[i]] = prv[i]
            head[bNum] = nxt[i]
        # tail 이란면?
        elif nxt[i] == -1:
            nxt[prv[i]] = nxt[i]
            tail[bNum] = prv[i]
        else:
            prv[nxt[i]] = prv[i]
            nxt[prv[i]] = nxt[i]

        boxes[i][0] = -1
        boxes[i][1] = -1
    return ret


def drop_box(w):
    global N, M
    ret = 0
    for m in range(M):
        # 고장난 벨트는 패스
        if isBroken[m]:
            continue
        # head 를 확인 후 무게가 w 이하라면 삭제 및 ret += weight
        i = head[m]
        if boxes[i][0] <= w:
            ret += boxes[i][0]
            delete_box(i)
        else:
            prv[i] = tail[m]
            nxt[tail[m]] = i
            head[m], tail[m] = nxt[i], i
            prv[nxt[i]] = -1
            nxt[i] = -1
    return ret


def check_box(i):
    ret = -1
    if i in boxes.keys() and boxes[i][0] > 0:
        bNum = boxes[i][1]
        # head 라면?
        if prv[i] == -1:
            pass
        # tail 이란면?
        elif nxt[i] == -1:
            nxt[prv[i]] = nxt[i]
            tail[bNum] = prv[i]
        else:
            prv[nxt[i]] = prv[i]
            nxt[prv[i]] = nxt[i]
        nxt[i] = head[bNum]
        prv[i] = -1
        prv[head[bNum]] = i
        ret = bNum+1
    return ret


def break_belt(bNum):
    if isBroken[bNum]:
        return -1

    mIdx = bNum+1
    isBroken[bNum] = True

    while mIdx != bNum:
        if mIdx == M:
            mIdx = 0
        if isBroken[mIdx]:
            mIdx += 1
            continue
        nxt[tail[mIdx]] = head[bNum]
        prv[head[bNum]] = tail[mIdx]
        head[bNum] = -1
        tail[mIdx] = tail[bNum]
        tail[bNum] = -1
        break

    return bNum+1


input = sys.stdin.readline

N, M = -1, -1

boxes = dict()
prv = dict()
nxt = dict()

head = [-1 for _ in range(10)]
tail = [-1 for _ in range(10)]
isBroken = [False] * 10

q = int(input().strip())

for _ in range(q):
    temp = list(map(int, input().split()))
    ret = -2
    c = temp[0]
    if c == 100:
        N = temp[1]
        M = temp[2]
        init(temp[3:])
    elif c == 200:
        ret = drop_box(temp[1])
    elif c == 300:
        ret = delete_box(temp[1])
    elif c == 400:
        ret = check_box(temp[1])
    elif c == 500:
        ret = break_belt(temp[1]-1)

    if ret == -2:
        continue
    print(ret)