# 완전탐색 결과 10개중 3개... 제한시간 초과... Fail

test_case = int(input())

for t in range(test_case):
    camera_num = int(input())
    cmr_list = []
    for c in range(camera_num):
        cmr_list.append(list(map(int, input().split())))

    result = 0
    for x in range(camera_num-2):
        for y in range(x+1,camera_num-1):
            if cmr_list[x][0] > cmr_list[y][2] or cmr_list[x][2] < cmr_list[y][0] or cmr_list[x][1] > cmr_list[y][3] or cmr_list[x][3] < cmr_list[y][1]:
                continue
            else:
                # chk_list = [max(cmr_list[x][0], cmr_list[y][0]), max(cmr_list[x][1], cmr_list[y][1]), min(cmr_list[x][2], cmr_list[y][2]), min(cmr_list[x][3], cmr_list[y][3])]
                for z in range(y+1, camera_num):
                    if max(cmr_list[x][0], cmr_list[y][0]) > cmr_list[z][2] or min(cmr_list[x][2], cmr_list[y][2]) < cmr_list[z][0] or max(cmr_list[x][1], cmr_list[y][1]) > cmr_list[z][3] or min(cmr_list[x][3], cmr_list[y][3]) < cmr_list[z][1]:
                        continue
                    else:
                        result += 1

    print(f'#{t+1} {result}')


