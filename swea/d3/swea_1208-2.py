# flatten
for t in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))
    gap = 0
    while True:
        max_val = 0
        max_idx = 0
        min_val = 100
        min_idx = 0
        for box_idx in range(100):
            if max_val < boxes[box_idx]:
                max_val = boxes[box_idx]
                max_idx = box_idx
            if min_val > boxes[box_idx]:
                min_val = boxes[box_idx]
                min_idx = box_idx
        if dump == 0:
            gap = boxes[max_idx] - boxes[min_idx]
            break
        dump -= 1
        boxes[max_idx] -= 1
        boxes[min_idx] += 1
    print('#{} {}'.format(t, gap))