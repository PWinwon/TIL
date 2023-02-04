import sys

input = sys.stdin.readline

W, N = map(int, input().split())

VVS = [list(map(int, input().split())) for _ in range(N)]

VVS.sort(key=lambda x: x[1], reverse=True)

result = 0

for vvs, cost in VVS:
    if W <= 0:
        break
    elif W > vvs:
        W -= vvs
        result += vvs * cost
    else:
        result += W * cost
        W = 0

print(result)