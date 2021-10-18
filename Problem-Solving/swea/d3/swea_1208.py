for t in range(1,11):
    dump = int(input())
    boxes = list(map(int, input().split()))
    for dum in range(dump):
        # input받은 리스트에 max값과 min값의 index를 알기 위해 enuerate 함수를 사용
        data_boxes = enumerate(boxes)
        cnt = 0
        max_box = max(boxes)
        min_box = min(boxes)
        max_loop = 0
        min_loop = 0
        for idx, value in data_boxes:
            # dump 한번에 다수의 max값에 대해 여러번 연산하는 경우를 방지하기 위해
            # max_loop, min_loop 변수를 통해 1번만 시행되도록 제어
            if (max_box == value) and (max_loop == 0):
                boxes[idx] -= 1
                max_loop = 1
            if (min_box == value) and (min_loop == 0):
                boxes[idx] += 1
                min_loop = 1
    print(f'#{t} {max(boxes) - min(boxes)}')