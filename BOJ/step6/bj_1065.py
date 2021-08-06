import sys

number = int(sys.stdin.readline())
result = 0
for i in range(0,number):
    num = i+1
    gap = 0
    check = 1
    gap = ((num//10) % 10 - num % 10)
    while num >= 10:
        if ((num//10) % 10 - num % 10) != gap:
            check = 0
            break
        num = num//10
    if check == 1:
        result += 1
print(result)