N = int(input())
num = 1
for n in range(1, N+1):
    num *= n

check = list(str(num))

result = 0
for c in range(len(check)-1, -1, -1):
    if check[c] != '0':
        break
    else:
        result += 1
print(result)