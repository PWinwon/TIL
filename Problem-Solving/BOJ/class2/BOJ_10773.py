K = int(input())

stck = []

for k in range(K):
    num = int(input())
    if num:
        stck.append(num)
    else:
        stck.pop()

print(sum(stck))