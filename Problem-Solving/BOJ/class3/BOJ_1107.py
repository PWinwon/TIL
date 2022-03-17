def my_check(num):
    num = str(num)
    for n in num:
        if n in broken_btn:
            return False
    return True


N = int(input())

M = int(input())
broken_btn = []

if M:
    broken_btn = list(input().split())

start = 100

result = abs(N-100)

for n in range(1000001):
    if my_check(n):
        result = min(result, len(str(n))+abs(n-N))

print(result)