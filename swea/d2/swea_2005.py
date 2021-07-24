T = int(input())

for i in range(T):
    N = int(input())
    print(f'#{i+1}')
    for n in range(1,N+1):
        n_list = [1] * n
        if n > 2:
            for idx in range(1,n-1):
                n_list[idx] = sum(before_l[idx-1:idx+1])
            for x in n_list:
                before_l = n_list
                print(x, end = ' ')
            print('')
        else:
            for x in n_list:
                before_l = n_list
                print(x, end = ' ')
            print('')
    

