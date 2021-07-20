# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스 별로 첫 줄에는 자연수 N(2 ≤ N ≤ 1,000,000)이 주어지고,
# 둘째 줄에는 각 날의 매매가를 나타내는 N개의 자연수들이 공백으로 구분되어 순서대로 주어진다.
# 각 날의 매매가는 10,000이하이다.

import sys

T = int(input())

for i in range(T):
    n = int(input())
    n_list = list(map(int, sys.stdin.readline().split()))
    max_money = 0
    while(True):
        n_max = None
        for j in range(len(n_list)):
            if n_max is None:
                n_max = n_list[j]
            if n_max <= n_list[j]:
                n_max = n_list[j]
                idx = j
        for k in range(idx):
            max_money = max_money + n_max - n_list[k]
        if idx == len(n_list)-1:
            break
        else:
            n_list = n_list[idx+1:len(n_list)+1]
    print(f'#{i+1} {max_money}')
