N = int(input())
lst = []
for n in range(N):
    lst.append(input())
lst = list(set(lst))
lst.sort(key=lambda x: (len(x), x))
for l in lst:
    print(l)