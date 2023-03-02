import sys

# sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline


N = int(input().strip())
lst = list(map(int, input().split()))

my_lis = []
cnt = 0

for i in range(N):
    if my_lis:
        if my_lis[-1] < lst[i]:
            my_lis.append(lst[i])
            cnt += 1
        else:
            l = 0
            r = cnt-1
            while l <= r:
                mid = (l + r) // 2
                if my_lis[mid] < lst[i]:
                    l = mid + 1
                else:
                    r = mid - 1
            if l >= cnt:
                my_lis.append(lst[i])
                cnt += 1
            else:
                my_lis[l] = lst[i]
    else:
        my_lis.append(lst[i])
        cnt += 1

print(cnt)