# PyPy 통과

import sys
# sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline


def find(x):
    if x == parents[x]:
        return parents[x]
    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y
    return


def my_ccw(p1, p2, p3):
    A = p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1]
    B = p1[1] * p2[0] + p2[1] * p3[0] + p3[1] * p1[0]
    ret = A-B

    if ret > 0:
        return 1
    elif ret == 0:
        return 0
    else:
        return -1


def my_check(p1, p2, p3, p4):
    res1 = my_ccw([p1[0], p1[1]], [p2[0], p2[1]], [p3[0], p3[1]])
    res2 = my_ccw([p1[0], p1[1]], [p2[0], p2[1]], [p4[0], p4[1]])
    res3 = my_ccw([p3[0], p3[1]], [p4[0], p4[1]], [p1[0], p1[1]])
    res4 = my_ccw([p3[0], p3[1]], [p4[0], p4[1]], [p2[0], p2[1]])

    if res1 == res2 == res3 == res4 == 0:
        if (max(p1[0], p2[0]) < min(p3[0], p4[0])) or (max(p3[0], p4[0]) < min(p1[0], p2[0])) or (max(p1[1], p2[1]) < min(p3[1], p4[1])) or (
                max(p3[1], p4[1]) < min(p1[1], p2[1])):
            return False
        else:
            return True

    elif (res1 * res2 <= 0) and (res3 * res4 <= 0):
        return True
    else:
        return False


N = int(input().strip())
parents = [i for i in range(N)]

lines = []
for n in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    lines.append([x1, y1, x2, y2])

for i in range(N):
    for j in range(i, N):
        if my_check([lines[i][0], lines[i][1]], [lines[i][2], lines[i][3]], [lines[j][0], lines[j][1]], [lines[j][2], lines[j][3]]):
            if find(i) != find(j):
                union(i, j)

parents = [find(x) for x in parents]

cnt_dict = dict()
result = 0
for p in parents:
    if p in cnt_dict.keys():
        cnt_dict[p] += 1
    else:
        result += 1
        cnt_dict[p] = 1


print(result)
print(max(cnt_dict.values()))
