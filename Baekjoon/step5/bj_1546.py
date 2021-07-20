import sys

num = int(input())
score = list(map(int, sys.stdin.readline().split()))
max_score = 0
avg_score = 0

for i in range(num):
    avg_score += score[i]
    if(max_score <= score[i]):
        max_score = score[i]

print(avg_score * 100 / (max_score * num))