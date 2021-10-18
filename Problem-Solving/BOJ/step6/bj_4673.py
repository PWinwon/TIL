numbers = [1] * 10000

for idx in range(10000):
    num = idx + 1
    self_num = num
    if numbers[idx] == 1:
        print(num)
    while num:
        self_num += num % 10
        num = num // 10
    if self_num <= 10000:
        numbers[self_num-1] = 0

