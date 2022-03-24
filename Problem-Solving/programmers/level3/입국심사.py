def solution(n, times):
    left = 1
    right = max(times) * n

    while left <= right:
        mid = (left + right) // 2
        total = 0
        for time in times:
            total += mid // time
            if total >= n:
                break
        if total < n:
            left = mid + 1
        else:
            right = mid - 1

    return left