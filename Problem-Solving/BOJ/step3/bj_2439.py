n = int(input())
b = n - 1

for i in range(1,n+1):
    print(' ' * (n-i) , end ='')
    print('*' * i)
