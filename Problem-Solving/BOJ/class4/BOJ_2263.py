import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline


def preorder(in_s, in_e, post_s, post_e):
    if in_s > in_e or post_s > post_e:
        return

    root = post_order[post_e]

    left_node = node_index[root] - in_s
    right_node = in_e - node_index[root]

    print(root, end=' ')

    preorder(in_s, in_s + left_node - 1, post_s, post_s + left_node - 1)
    preorder(in_e - right_node + 1, in_e, post_e - right_node, post_e - 1)


N = int(input().strip())

in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

node_index = [0] * (N+1)

for i in range(N):
    node_index[in_order[i]] = i

preorder(0, N-1, 0, N-1)

