import sys

button_num = int(sys.stdin.readline())
button_list = list(map(int,sys.stdin.readline().split()))

people_num = int(sys.stdin.readline())
people_list = []
for i in range(people_num):
    people_list.append(list(map(int, sys.stdin.readline().split())))

#버튼의 on / off 의 조작을 도와줄 리스트 생성
swich_on = [1, 0]
for people in people_list:
    if people[0] == 1:  #남자 조건에 따른 버튼 리스트의 값 변화
        for button in range(button_num):
            if (button+1) % people[1] == 0:
                button_list[button] = swich_on[button_list[button]]
    else: #여자 조건에 따른 버튼 리스트의 값 변화
        idx = people[1] - 1
        idx_x = 1
        button_list[idx] = swich_on[button_list[idx]]
        while idx+idx_x < button_num and idx-idx_x >= 0:
            if button_list[idx-idx_x] == button_list[idx+idx_x]:
                button_list[idx-idx_x] = swich_on[button_list[idx-idx_x]]
                button_list[idx+idx_x] = swich_on[button_list[idx+idx_x]]
                idx_x += 1
            else:
                break
# 20개씩 잘라 출력하기 위해 반복문 사용
for j in range(0, button_num , 20):
    print(*button_list[j:j+20])



