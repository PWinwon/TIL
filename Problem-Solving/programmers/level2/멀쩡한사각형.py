def solution(w,h):
    answer = w * h
    width = w
    height = h
    cross = 0
    G = 1
    num = 2
    while num <= w or num <= h:
        if width % num == 0 and height % num == 0:
            G *= num
            width = width // num
            height = height // num
            continue
        num += 1
    cross = G * (width + height - 1)
    answer -= cross
    return answer