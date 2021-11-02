from collections import deque


dr = [-1, 1, 0, 0, -1, 1, -1, 1]
dc = [0, 0, -1, 1, -1, -1, 1, 1]


N, M, K = map(int, input().split())
MAP = [[deque() for _ in range(N)] for _ in range(N)]
energy = [[5 for _ in range(N)] for _ in range(N)]
A = [list(map(int, input().split())) for _ in range(N)]

for m in range(M):
    row, col, z = map(int, input().split())
    MAP[row-1][col-1].append(z)

de = -1
for k in range(K):
    add_tree = [[0 for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if MAP[r][c]:
                tree_cnt = len(MAP[r][c])
                need_energy = 0
                dead_line = tree_cnt
                # 봄
                for i in range(tree_cnt):
                    # 데드라인 설정
                    if need_energy + MAP[r][c][i] > energy[r][c]:
                        dead_line = i
                        break
                    # 필요한 에너지 따로 저장
                    need_energy += MAP[r][c][i]
                    # 나무 나이 증가
                    MAP[r][c][i] += 1
                # 봄의 양분을 받은 나무들의 나이만큼 연산
                energy[r][c] -= need_energy
                # 여름 죽은 나무 미리 양분 +
                for j in range(dead_line, tree_cnt):
                    energy[r][c] += MAP[r][c][j]//2
                # 죽은 나무 제거
                for dead in range(tree_cnt-dead_line):
                    MAP[r][c].pop()

                # 가을 번식(죽은나무가 있으니 tree_cnt 못씀)
                # 개수만 세서 나중에 반영 >> 반복문 중에 번식되어버리면 숫자가 꼬임
                for tree in range(len(MAP[r][c])):
                    if MAP[r][c][tree] % 5 == 0:
                        for idx in range(8):
                            r_idx = r + dr[idx]
                            c_idx = c + dc[idx]
                            if r_idx < 0 or r_idx >= N or c_idx < 0 or c_idx >= N:
                                continue
                            add_tree[r_idx][c_idx] += 1
                # 겨울 양분 보충
                energy[r][c] += A[r][c]
            else:
                # 나무가 없어도 영양분은 보충
                energy[r][c] += A[r][c]
    # 한해가 끝나면 번식 반영
    for rr in range(N):
        for cc in range(N):
            for cnt in range(add_tree[rr][cc]):
                MAP[rr][cc].appendleft(1)

result = 0
for y in range(N):
    for x in range(N):
        result += len(MAP[y][x])
print(result)