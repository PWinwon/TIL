R = 31
M = 1234567891

N = int(input())
temp = input()

result = 0

for n in range(N):
    num = ord(temp[n]) - ord('a') + 1
    result += num * (R ** n)
    result %= M

print(result)