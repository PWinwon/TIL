test_case = int(input())
for tc in range(test_case):
    lst = list(input().split())
    stack = []
    idx = 0
    while lst:
        if lst[idx].isdigit():
            stack.append(int(lst[idx]))
        elif lst[idx] == '.':
            if len(stack) == 1:
                print('#{} {}'.format(tc+1, stack.pop()))
            else:
                print('#{} error'.format(tc+1))
            break
        elif len(stack) > 1:
            if lst[idx] == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(b + a)
            elif lst[idx] == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif lst[idx] == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(b * a)
            elif lst[idx] == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))
        else:
            print('#{} error'.format(tc+1))
            break
        idx += 1