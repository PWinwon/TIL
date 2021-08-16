test_case = int(input())

for tc in range(test_case):
    n = int(input())
    lst_n = [list(map(int, input().split())) for _ in range(n)]
    lst_room = [0] * 200
    for idx in range(n):
        if lst_n[idx][0] > lst_n[idx][1]:
            lst_n[idx][0], lst_n[idx][1] = lst_n[idx][1], lst_n[idx][0]
        st = (lst_n[idx][0]-1)//2
        ed = (lst_n[idx][1]-1)//2
        for move in range(st, ed+1):
            lst_room[move] += 1
    max_move = 0
    for m in range(200):
        if max_move < lst_room[m]:
            max_move = lst_room[m]
    print('#{} {}'.format(tc+1, max_move))