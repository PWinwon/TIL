def my_dice(level, path, c):
    if level == N:
        print(' '.join(path))
        return
    if M==1:
        for i in range(1, 7):
            my_dice(level+1, path+str(i), c)
        return
    elif M==2:
        for i in range(1, 7):
            if path and path[-1] > str(i):
                continue
            my_dice(level+1, path+str(i), c)
        return
    else:
        for i in range(1, 7):
            if used[i] == 1:
                continue
            used[i] = 1
            my_dice(level+1, path+str(i), c)
            used[i] = 0
        return


N, M = map(int, input().split())
used = [0] * 7
my_dice(0, '', M)