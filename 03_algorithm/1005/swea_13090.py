def func_run(cards):
    for c in range(8):
        if cards[c] and cards[c+1] and cards[c+2]:
            return True
    return 0


def func_triplet(cards):
    for c in range(10):
        if cards[c] >= 3:
            return True
    return False


T = int(input())

for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    ply1 = [0] * 10
    ply2 = [0] * 10
    result = 0
    for i in range(12):
        if i % 2:
            ply1[lst[i]] += 1
            if func_run(ply1) or func_triplet(ply1):
                result = 2
        else:
            ply2[lst[i]] += 1
            if func_run(ply2) or func_triplet(ply2):
                result = 1
        if result:
            break
    print('#{} {}'.format(tc, result))