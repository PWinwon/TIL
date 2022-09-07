def solution(id_list, report, k):
    cnt = 0
    idx = dict()
    id_len = len(id_list)
    report = list(set(report))

    answer = [0] * id_len
    for id in id_list:
        idx[id] = [cnt, 0]
        cnt += 1

    arr = [[0 for _ in range(id_len)] for _ in range(id_len)]

    for re in report:
        a, b = re.split()
        arr[idx[b][0]][idx[a][0]] = 1
        idx[b][1] += 1

    for key, value in idx.items():
        if value[1] >= k:
            for i in range(id_len):
                if arr[value[0]][i]:
                    answer[i] += 1

    return answer