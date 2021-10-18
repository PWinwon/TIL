thr_sqare = [ i ** 3  for i in range(10**6 + 1)]

test_case = int(input())

for tc in range(test_case):
    number = int(input())
    result = -1
    for idx in range(10**6 + 1):
        if thr_sqare[idx] == number:
            result = idx
        if thr_sqare[idx] > number:
            break
    print('#{} {}'.format(tc+1, result))