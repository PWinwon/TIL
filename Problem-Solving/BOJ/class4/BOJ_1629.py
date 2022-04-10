import sys

def my_func(num, cnt, md):
    if cnt == 1:
        return num % md
    else:
        temp = my_func(num, cnt//2, md)
        if cnt % 2:
            return temp * temp * num % md
        return temp * temp % md


A, B, C = map(int, sys.stdin.readline().split())
result = my_func(A, B, C)
print(result)