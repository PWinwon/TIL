T = int(input())

for tc in range(T):
    input_txt = input()
    stck = []

    for item in input_txt:
        if item == '(':
            stck.append(item)
        else:
            if stck:
                stck.pop()
            else:
                print('NO')
                break
    else:
        if stck:
            print('NO')
        else:
            print('YES')