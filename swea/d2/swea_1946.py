T = int(input())

for i in range(T):
    print(f'#{i+1}')
    N = int(input())
    idx = 0
    for n in range(N):
        char, nums = input().split()
        nums = int(nums)
        for num in range(nums):
            print(char,end='')
            idx += 1
            if (idx > 0) and (idx % 10 == 0):
                print('')
    print('')