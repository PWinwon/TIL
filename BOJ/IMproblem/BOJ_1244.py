button_num = int(input())
button_list = []
for i in range(button_num//10 + 1):
    button_list.extend(list(map(int,input().split())))

people_num = int(input())
people_list = []
for i in range(people_num):
    people_list.append(list(map(int, input().split())))

for people in people_list:
    idx = 1
    if people[0] == 1:
        for button in button_list:
            
