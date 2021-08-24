order_oper = {
    '+': 1,
    '*': 2,
    '(': 0,
}


for tc in range(1, 11):
    N = int(input())
    expr = input().rstrip()
    stack = []
    back = []
    idx = 0

    while idx < N:
        if expr[idx].isdigit():
            back.append(expr[idx])
        elif expr[idx] == '(':
            stack.append(expr[idx])
        elif expr[idx] == ')':
            while stack[-1] != '(':
                back.append(stack.pop())
            stack.pop()
        else:
            if stack == [] or order_oper[expr[idx]] > order_oper[stack[-1]]:
                stack.append(expr[idx])
            else:
                while order_oper[expr[idx]] <= order_oper[stack[-1]]:
                    back.append(stack.pop())
                stack.append(expr[idx])
        idx += 1

    while stack:
        back.append(stack.pop())

    idx = 0
    while idx < len(back):
        if back[idx].isdigit():
            stack.append(int(back[idx]))
        elif back[idx] == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(b+a)
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(b*a)
        idx += 1

    print('#{} {}'.format(tc, stack[0]))