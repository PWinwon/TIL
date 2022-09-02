def solution(queue1, queue2):
    answer = -1
    idx1 = 0
    idx2 = 0
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    avg = (sum1 + sum2) // 2
    length = len(queue1)
    while idx1 < 2 * length and idx2 < 2 * length and sum1 != sum2:
        if sum1 < avg:
            sum1 += queue2[idx2]
            sum2 -= queue2[idx2]
            queue1.append(queue2[idx2])
            idx2 += 1
        else:
            sum1 -= queue1[idx1]
            sum2 += queue1[idx1]
            queue2.append(queue1[idx1])
            idx1 += 1
    if sum1 == avg:
        answer = idx1 + idx2

    return answer