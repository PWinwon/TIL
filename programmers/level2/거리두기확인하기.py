dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(level, row, col, lst, vis, res):
    if 0 > row or row >= 5 or 0 > col or col >= 5:
        return res
    if level != 0 and vis[row][col] == 1:
        return res
    if lst[row][col] == 'X':
        level += 1
    if level > 2:
        return res
    if level != 0 and lst[row][col] == 'P':
        res = True
        return res
    for i in range(4):
        vis[row][col] = 1
        res = dfs(level + 1, row + dr[i], col + dc[i], lst, vis, res)
        vis[row][col] = 0

    return res


def solution(places):
    answer = []
    for plc in places:
        chk = False
        result = 1
        used = [[0 for _ in range(5)] for _ in range(5)]
        for r in range(5):
            for c in range(5):
                if plc[r][c] == 'P':
                    if dfs(0, r, c, plc, used, chk):
                        result = 0
        answer.append(result)

    return answer