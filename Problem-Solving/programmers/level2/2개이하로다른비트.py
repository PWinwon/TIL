def solution(numbers):
    answer = []
    for num in numbers:
        if num % 2:
            lst = []
            num = bin(num)[2:]
            num = '0' + num
            lst.extend(num)
            idx = len(lst) - 1
            while idx >= 0:
                if lst[idx] == '0':
                    lst[idx] = '1'
                    idx += 1
                    break
                idx -= 1
            while idx >= 0:
                if lst[idx] == '1':
                    lst[idx] = '0'
                    break
                idx += 1
            answer.append(int(''.join(lst),2))

        else:
            answer.append(num + 1)
    return answer