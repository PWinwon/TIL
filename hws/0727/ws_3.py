def lonely(numbers):
    i = 0
    while True:
        if i >= len(numbers) -1:
            break
        if numbers[i] == numbers[i+1]:
            numbers.pop(i)
        else :
            i += 1
    return numbers

a = lonely([1, 1, 3, 3, 0, 1, 1])
b = lonely([4, 4, 4, 3, 3])
print(a)
print(b)