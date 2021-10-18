def solution(s):
    answer = 0
    n = len(s)
    pl = 1
    min_len = 1000
    if n == 1:
        answer = 1
        return answer
    while pl <= n // 2:
        pl_len = 0
        idx = 0
        while idx < n:
            cnt = 0
            pattern = s[idx:idx + pl]
            if len(pattern) < pl:
                pl_len += len(pattern)
                break
            jdx = idx + pl
            while jdx < n:
                if pattern == s[jdx:jdx + pl]:
                    cnt += 1
                    jdx += pl
                else:
                    break
            if cnt >= 999:
                pl_len += pl + 4
            elif cnt >= 99:
                pl_len += pl + 3
            elif cnt >= 9:
                pl_len += pl + 2
            elif cnt > 0:
                pl_len += pl + 1
            else:
                pl_len += pl
            idx = jdx
        if pl_len < min_len:
            min_len = pl_len
        pl += 1
    answer = min_len

    return answer