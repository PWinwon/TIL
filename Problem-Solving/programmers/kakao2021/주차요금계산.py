LAST_OUT = 23 * 60 + 59

def solution(fees, records):
    global LAST_OUT
    answer = []
    in_out = [[-1, 0] for _ in range(10000)]
    for record in records:
        time, num, flag = record.split()
        num = int(num)
        h, m = map(int, time.split(":"))
        t = h * 60 + m
        if flag == 'IN':
            in_out[num][0] = t
        elif flag == 'OUT':
            in_out[num][1] += t - in_out[num][0]
            in_out[num][0] = -1

    for i in range(10000):
        if in_out[i][0] != -1:
            in_out[i][1] += LAST_OUT - in_out[i][0]
        if in_out[i][1]:
            temp = 0
            if in_out[i][1] <= fees[0]:
                temp += fees[1]
            else:
                temp += fees[1] + (in_out[i][1]-fees[0]) // fees[2] * fees[3]
                if (in_out[i][1] - fees[0]) % fees[2]:
                    temp += fees[3]
            answer.append(temp)
    return answer