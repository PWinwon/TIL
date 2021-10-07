import sys

T = int(sys.stdin.readline())

for tc in range(T):
    N = int(sys.stdin.readline())
    scores = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
    scores_A = sorted(scores)
    min_A = scores_A[0][1]
    cnt = 0
    for i in range(1, N):
        if scores_A[i][1] > min_A:
            cnt += 1
        elif scores_A[i][1] < min_A:
            min_A = scores_A[i][1]
    print(N-cnt)