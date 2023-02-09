import sys
# sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

def find(x):
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]


# def union(x, y):
#     x = find(x)
#     y = find(y)
#     if x < y:
#         parents[y] = x
#     else:
#         parents[x] = y
#     return


G = int(input().strip())
P = int(input().strip())

parents = [i for i in range(G+1)]

result = 0
for p in range(P):
    a = int(input().strip())
    b = find(a)
    if b == 0:
        break
    # union(b, b-1)
    # b > b-1
    parents[b] = parents[b-1]
    result += 1

print(result)