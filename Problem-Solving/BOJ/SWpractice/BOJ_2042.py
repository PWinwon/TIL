import sys

def my_tree(s, e, idx):
    if s == e:
        tree[idx] = lst[s]
        return tree[idx]
    mid = (s + e) // 2
    tree[idx] = my_tree(s, mid, idx * 2) + my_tree(mid+1, e, idx*2 + 1)
    return tree[idx]


def my_sum(s, e, idx):
    global b, c
    if b > e or c < s:
        return 0
    if b <= s and c >= e:
        return tree[idx]

    mid = (s + e) // 2
    return my_sum(s, mid, idx * 2) + my_sum(mid+1, e, idx * 2 + 1)


def my_update(s, e, idx):
    global b, temp
    if b < s or b > e:
        return
    tree[idx] += temp
    if s == e:
        return
    mid = (s + e) // 2
    my_update(s, mid, idx * 2)
    my_update(mid+1, e, idx * 2 + 1)


N, M, K = map(int, sys.stdin.readline().split())
lst = []
for n in range(N):
    lst.append(int(sys.stdin.readline().strip()))

tree = [0] * (N * 4)
my_tree(0, N-1, 1)

for m in range(M+K):
    a, b, c = map(int, sys.stdin.readline().split())
    b -= 1
    if a == 1:
        temp = c - lst[b]
        lst[b] = c
        my_update(0, N-1, 1)
    elif a == 2:
        c -= 1
        ret = my_sum(0, N-1, 1)
        print(ret)