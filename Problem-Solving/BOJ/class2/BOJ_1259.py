

def my_func(n):
    if len(n) < 2:
        return True
    else:
        if n[0] == n[-1]:
            my_func(n[1:len(n-2)])
        else:
            return False


while True:
    num = input()
    if num == '0':
        break
    if my_func(num):
        print('Yes')
    else:
        print('No')
