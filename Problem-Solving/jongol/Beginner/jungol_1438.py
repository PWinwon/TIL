paper = [[ 0 for _ in range(100)] for _ in range(100)]

result = 0
N = int(input())
for i in range(N):
    x, y = map(int, input().split())
    for r in range(y, y+10):
        for c in range(x, x+10):
            if paper[r][c] == 0:
                paper[r][c] = 1
                result += 1

print(result)