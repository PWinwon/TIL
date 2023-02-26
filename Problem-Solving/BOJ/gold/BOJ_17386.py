import sys

input = sys.stdin.readline


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


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

res1 = my_ccw([x1, y1], [x2, y2], [x3, y3]) * my_ccw([x1, y1], [x2, y2], [x4, y4])
res2 = my_ccw([x3, y3], [x4, y4], [x1, y1]) * my_ccw([x3, y3], [x4, y4], [x2, y2])

if res1 == -1 and res2 == -1:
    print(1)
else:
    print(0)