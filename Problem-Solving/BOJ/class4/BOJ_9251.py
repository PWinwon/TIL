import sys

input = sys.stdin.readline

F_string = ' ' + input().strip()
S_string = ' ' + input().strip()

F_len = len(F_string)
S_len = len(S_string)

memo = [[0 for _ in range(S_len)] for _ in range(F_len)]

for i in range(1, F_len):
    F_temp = F_string[i]
    for j in range(1, S_len):
        S_temp = S_string[j]
        if F_temp == S_temp:
            memo[i][j] = memo[i-1][j-1] + 1
        else:
            memo[i][j] = max(memo[i][j-1], memo[i-1][j])

print(memo[F_len-1][S_len-1])