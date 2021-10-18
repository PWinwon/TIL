# 2차원 리스트 90도 회전하는 함수
def rotate_90(sqare, sq_len):
    result = []
    for x in range(sq_len):
        sample_ls = []
        for y in range(sq_len-1,-1,-1):
            sample_ls.append(sqare[y][x])
        result.append(sample_ls)
    return result

T = int(input())

for i in range(T):
    list_N = []
    N = int(input())
    for n in range(N):
        sample_ls = list(map(int, input().split()))
        list_N.append(sample_ls)
    list_90 = rotate_90(list_N, N)
    list_180 = rotate_90(list_90, N)
    list_270 = rotate_90(list_180, N)
    print(f'#{i+1}')
    # 출력을 할 때 문제에서 요구한 모습으로 출력하기 위해 반복문을 사용하였습니다.
    for x in range(N):
        for y in range(N):
            print(list_90[x][y], end = '')
        print(' ', end ='')
        for y in range(N):
            print(list_180[x][y], end = '')
        print(' ', end ='')
        for y in range(N):
            print(list_270[x][y], end = '')
        print('')
        