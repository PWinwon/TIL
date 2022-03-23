def solution(stones, k):

    left = 0
    right = 200000000

    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        chk = True
        for i in stones:
            if i - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                chk = False
        if chk:
            left = mid + 1
        else:
            right = mid - 1

    answer = left
    return answer