import sys

T = int(sys.stdin.readline())

for t in range(T):
    list_t = list(map(int, sys.stdin.readline().split()))
    students = list_t[0]
    scores = list_t[1:]
    avg_scores = sum(scores) / students
    result = 0
    for score in scores:
        if score > avg_scores:
            result += 1

    print(f'{result/students * 100:.3f}%')

