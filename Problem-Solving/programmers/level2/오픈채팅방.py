def solution(record):
    answer = []
    id_dict = dict()
    actid_lst = []
    n = len(record)
    for i in range(n):
        sample = record[i].split()
        if sample[0] != 'Change':
            actid_lst.append([sample[0], sample[1]])
        if sample[0] != 'Leave':
            id_dict[sample[1]] = sample[2]        
    for j in range(len(actid_lst)):
        if actid_lst[j][0] == 'Enter':
            answer.append('{}님이 들어왔습니다.'.format(id_dict[actid_lst[j][1]]))
        else:
            answer.append('{}님이 나갔습니다.'.format(id_dict[actid_lst[j][1]]))
    return answer