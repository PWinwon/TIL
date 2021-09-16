# 0은 +, 1은 -, 2는 *, 3은 //

def my_func(level, total):
    global max_val, min_val
    if level == N:
        if total > max_val:
            max_val = total
        if total < min_val:
            min_val = total
        return
    for i in range(4):
        if oper[i] == 0:
            continue
        if i == 0:
            temp = total + numbers[level]
        elif i == 1:
            temp = total - numbers[level]
        elif i == 2:
            temp = total * numbers[level]
        else:
            if total < 0 and numbers[level] > 0:
                total *= -1
                temp = total // numbers[level]
                temp *= -1
            else:
                temp = total // numbers[level]
        oper[i] -= 1
        my_func(level+1, temp)
        oper[i] += 1
    return



N = int(input())
numbers = list(map(int, input().split()))
oper = list(map(int, input().split()))
max_val = -1000000000
min_val = 1000000000
my_func(1, numbers[0])
print(max_val)
print(min_val)