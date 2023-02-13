import sys
# sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N = int(input().strip())

lst = [list(map(int, input().split())) for _ in range(N)]
lst.append(lst[0])

result = 0
A = 0
B = 0

for i in range(N):
    A += lst[i][0] * lst[i+1][1]
    B += lst[i+1][0] * lst[i][1]

result = round(abs(A - B) / 2, 1)
print(result)