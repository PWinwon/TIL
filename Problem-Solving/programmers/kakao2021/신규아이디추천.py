special_char = '~!@#$%^&*()=+[{]}:?,<>/'

def solution(new_id):
    global special_char
    answer = ''
    new_id_1 = new_id.lower()
    for sc in special_char:
        new_id_1 = new_id_1.replace(sc, '')
    new_id_2 = ''
    while True:
        new_id_2 = new_id_1.replace('..', '.')
        if new_id_1 == new_id_2:
            break
        new_id_1 = new_id_2
    if len(new_id_2) >= 1 and new_id_2[0] == '.':
        new_id_2 = new_id_2[1:]
    if len(new_id_2) >= 1 and new_id_2[-1] == '.':
        new_id_2 = new_id_2[:-1]
    if new_id_2 == '':
        new_id_2 = 'a'
    if len(new_id_2) >= 16:
        new_id_2 = new_id_2[:15]
    if new_id_2[-1] == '.':
        new_id_2 = new_id_2[:-1]
    while len(new_id_2) < 3:
        new_id_2 += new_id_2[-1]
    answer = new_id_2
    return answer