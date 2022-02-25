import sys

N = int(input())
M = int(input())
S = sys.stdin.readline().strip()

idx = 1
pattern = 0
result = 0

while idx < M-1:
    if S[idx-1] == 'I' and S[idx] == 'O' and S[idx+1] == 'I':
        pattern += 1
        if pattern == N:
            result += 1
            pattern -= 1
        idx += 1
        
    else:
        pattern = 0
    idx += 1

print(result)