while True:
    s = input()
    if s == '0':
        break
    chk = True
    while len(s) >= 2:
        if s[0] == s[len(s)-1]:
            s = s[1:len(s)-1]
        else:
            chk = False
            break

    if chk:
        print('yes')
    else:
        print('no')