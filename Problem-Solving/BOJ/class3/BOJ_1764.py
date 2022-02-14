import sys

N, M = map(int, input().split())

my_hash = dict()
result = []

for n in range(N):
    name = sys.stdin.readline().strip()
    my_hash[name] = 1

for m in range(M):
    name = sys.stdin.readline().strip()
    if name in my_hash.keys():
        result.append(name)

result.sort()

print(len(result))
for i in range(len(result)):
    print(result[i])