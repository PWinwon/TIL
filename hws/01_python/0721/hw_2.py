def get_middle_char(stc):
    result = ''
    cnt = 0
    idx = 0
    for i in stc:
        cnt += 1
    idx = cnt // 2
    if cnt % 2 == 0:
        result += stc[idx-1:idx+1]
    else:
        result += stc[idx]
    print(result)

get_middle_char('hello')
get_middle_char('coding')

