T = int(input())

for i in range(T):
    print(f'#{i+1}')
    N = int(input())
    idx = 0
    # 입력받은 문자와 그 개수에 대해 반복문을 통해 출력
    # 조건물을 통해 10의 배수를 출력한 뒤 줄바꿈
    for n in range(N):
        char, nums = input().split()
        nums = int(nums)
        for num in range(nums):
            print(char,end='')
            idx += 1
            if (idx > 0) and (idx % 10 == 0):
                print('')
    print('')