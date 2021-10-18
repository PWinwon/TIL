my_alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
            'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']


def dfs(level, s, n, arr, res):
    if len(s) == n:
        if s in res.keys():
            res[s] += 1
        else:
            res[s] = 1
        return
    if level == 26:
        return
    if arr[level] == 1:
        dfs(level+1, s+my_alpha[level], n, arr, res)
    dfs(level+1, s, n, arr, res)
    return


def solution(orders, course):
    answer = []
    total = []
    adj = [[0 for _ in range(26)] for _ in range(len(orders))]
    for idx in range(len(orders)):
        for i in range(len(orders[idx])):
            for j in range(26):
                if my_alpha[j] == orders[idx][i]:
                    adj[idx][j] = 1
                    break
    for num in course:
        pattern = dict()
        for r in range(len(orders)):
            dfs(0, '', num, adj[r], pattern)
        total.append(pattern)
    for i in range(len(course)):
        for idx, val in total[i].items():
            if val == max(total[i].values()) and val >= 2:
                answer.append(idx)
    answer.sort()
    return answer