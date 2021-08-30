def bfs(level, lst, res, used, temp):
    if level == len(lst):
        a = temp[::]
        res.append(a)
        return res
    for i in range(len(lst)):
        if used[i] == 1:
            continue
        temp[level] = i+1
        used[i] = 1
        res = bfs(level+1, lst, res, used, temp)
        used[i] = 0
    return res


def solution(expression):
    answer = 0
    st = 0
    stack = []
    sign = []
    for i in range(len(expression)):
        if expression[i].isdigit():
            continue
        else:
            stack.append(int(expression[st:i]))
            sign.append(expression[i])
            st = i+1
    stack.append(int(expression[st:]))
    sample = list(set(sign))
    visited = [0] * len(sample)
    result = bfs(0, sample, [], visited, [0]*len(sample))
    for res in result:
        dict1 = dict(zip(sample, res))
        idx = 0
        stack1 = [stack[0]]
        my_sign = []
        while idx < len(sign):
            if my_sign:
                if dict1[sign[idx]] > dict1[my_sign[-1]]:
                    my_sign.append(sign[idx])
                else:
                    while my_sign and dict1[sign[idx]] <= dict1[my_sign[-1]]:
                        s = my_sign.pop()
                        if s == '+':
                            a = stack1.pop()
                            b = stack1.pop()
                            stack1.append(a + b)
                        elif s == '-':
                            a = stack1.pop()
                            b = stack1.pop()
                            stack1.append(b - a)
                        else:
                            a = stack1.pop()
                            b = stack1.pop()
                            stack1.append(a * b)
                    my_sign.append(sign[idx])
            else:
                my_sign.append(sign[idx])
            stack1.append(stack[idx + 1])
            idx += 1
        while my_sign:
            ms = my_sign.pop()
            if ms == '+':
                a = stack1.pop()
                b = stack1.pop()
                stack1.append(a + b)
            elif ms == '-':
                a = stack1.pop()
                b = stack1.pop()
                stack1.append(b - a)
            else:
                a = stack1.pop()
                b = stack1.pop()
                stack1.append(a * b)
        if answer < abs(stack1[0]):
            answer = abs(stack1[0])
    return answer