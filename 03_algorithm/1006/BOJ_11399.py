N = int(input())
lst = list(map(int, input().split()))
lst.sort()
result = 0
for i in range(N):
    result += sum(lst[:i+1])
print(result)
