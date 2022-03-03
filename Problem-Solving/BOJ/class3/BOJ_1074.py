def my_func(sr, er, sc, ec, num):
    global R, C
    if sr == R and sc == C:
        print(num)
        return
    mr = (sr + er) // 2
    mc = (sc + ec) // 2

    n = (mr - sr) * (mc - sc)

    if sr <= R < mr and sc <= C < mc:
        my_func(sr, mr, sc, mc, num)
    elif sr <= R < mr and mc <= C < ec:
        my_func(sr, mr, mc, ec, num + n)
    elif mr <= R < er and sc <= C < mc:
        my_func(mr, er, sc, mc, num + 2 * n)
    elif mr <= R < er and mc <= C < ec:
        my_func(mr, er, mc, ec, num + 3 * n)


N, R, C = map(int, input().split())
my_func(0, 2**N, 0, 2**N, 0)