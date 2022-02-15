import sys

N, M = map(int, input().split())

site_dict = dict()

for n in range(N):
    site, pwd = sys.stdin.readline().split()
    site_dict[site] = pwd

for m in range(M):
    site = sys.stdin.readline().strip()
    print(site_dict[site])