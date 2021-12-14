N = int(input())
lst = []

for n in range(N):
    lst.append(int(input()))


num = 1
result = []
stack = []


for n in lst:
    while num <= n:
        stack.append(num)
        result.append('+')
        num += 1
    if stack[-1] == n:
        stack.pop()
        result.append('-')
    else:
        result = []
        break

if result:
    for r in result:
        print(r)
else:
    print('NO')