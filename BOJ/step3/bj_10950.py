t = int(input())
result = [0] * t

for i in range(0,t):
    a, b = map(int,input().split())
    result[i] = a + b

for i in range(0,t):
    print(result[i])