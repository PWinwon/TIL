dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def solution(rows, columns, queries):
    answer = []
    idx = 1
    MAP = [[0 for _ in range(columns)] for _ in range(rows)]
    for r in range(rows):
        for c in range(columns):
            MAP[r][c] = idx
            idx += 1
    for q in range(len(queries)):
        row = queries[q][0] - 1
        col = queries[q][1] - 1
        moder = [queries[q][3] - queries[q][1], queries[q][2] - queries[q][0]]
        lst = []
        for i in range(4):
            for j in range(moder[i % 2]):
                row += dr[i]
                col += dc[i]
                lst.append(MAP[row][col])
        idx = len(lst) - 2
        answer.append(min(lst))
        if q == len(queries)-1:
            break
        for i in range(4):
            for j in range(moder[i%2]):
                MAP[row][col] = lst[idx%len(lst)]
                idx += 1
                row += dr[i]
                col += dc[i]

    return answer