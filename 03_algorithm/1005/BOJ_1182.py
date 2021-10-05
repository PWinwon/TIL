def my_func(level, total):
    global result
    if level == N:
        if total == S:
            result += 1
        return
    my_func(level+1, total+lst[level])
    my_func(level+1, total)
    return


N, S = map(int, input().split())
lst = list(map(int, input().split()))
if S:
    result = 0
else:
    result = -1
my_func(0, 0)
print(result)