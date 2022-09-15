gap = 0
result = [-1]


def equal_chk(r):
    global result
    for i in range(10, -1, -1):
        if r[i] == result[i]:
            continue
        if r[i] < result[i]:
            return False
        if r[i] > result[i]:
            return True
    return False


# n은 깊이, score는 획득점수의 차이, cnt 남은 화살수, arrows 화살 사용 list,
def my_dfs(n, score, peach_arrows, lion_cnt, lion_arrows):
    global gap, result
    if n == 11:
        if lion_cnt:
            lion_arrows[10] = lion_cnt
        if gap < score:
            gap = score
            result = lion_arrows
        elif gap == score and result == [-1]:
            gap = score
            result = lion_arrows
        elif result != [-1] and gap == score:
            if equal_chk(lion_arrows):
                result = lion_arrows
        return
    if lion_cnt < 0:
        return
    else:
        now_peach_cnt = peach_arrows[n]
        my_dfs(n + 1, score + 10 - n, peach_arrows, lion_cnt - now_peach_cnt - 1, lion_arrows + [now_peach_cnt + 1])
        if peach_arrows[n]:
            my_dfs(n + 1, score - (10 - n), peach_arrows, lion_cnt, lion_arrows + [0])
        else:
            my_dfs(n + 1, score, peach_arrows, lion_cnt, lion_arrows + [0])
    return


def solution(n, info):
    global result, gap
    my_dfs(0, 0, info, n, [])
    answer = result
    if gap == 0:
        answer = [-1]
    return answer