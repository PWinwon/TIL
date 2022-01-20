N = int(input())

lst = []
for n in range(N):
    age, name = input().split()
    temp = [age, name]
    lst.append(temp)

lst.sort(key=lambda x: int(x[0]))

for n in range(N):
    print(lst[n][0], lst[n][1])