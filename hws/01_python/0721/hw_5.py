def my_avg(*args):
    total = 0
    cnt = 0
    for i in args:
        total += i
        cnt += 1
    return total/cnt

result = my_avg(77, 83, 95, 80, 70)
print(result)