###############################################
# q 연습

# q_lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# front = 0
# rear = 0
#
# q_lst[rear] = 3
# rear += 1
# q_lst[rear] = 7
# rear += 1
# q_lst[rear] = 5
# rear += 1
#
# ret = q_lst[front]
# print(ret)
# front += 1
# ret = q_lst[front]
# print(ret)
# front += 1
# ret = q_lst[front]
# print(ret)
# front += 1

########################################################
# 교수님 풀이

# queue = [0,0,0,0,0,0,0,0,0,0]
# front = 0 # 데이터 나오는곳
# rear = 0 # 데이터 넣는곳
#
# queue[rear] = 3
# rear += 1
# queue[rear] = 5
# rear += 1
# queue[rear] = 7
# rear += 1
#
# ret = queue[front]
# front += 1
# ret = queue[front]
# front += 1


########################################################
# de que 연습

# queue = [3, 7, 2, 1, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# front = 0
# rear = 5
#
# while front < rear:
#     print(queue[front])
#     front += 1


########################################################
# 교수님 풀이 - de que

# queue = [3, 7, 2, 1, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# front = 0
# rear = 5
#
# while front < rear:  # queue 안에 있을때 not isEmpty
#     # deque
#     ret = queue[front]
#     front += 1
#     print(ret, end=' ')


#######################################################
# queue 라이브러리 이용하기

from collections import deque

queue = deque() # queue 생성
queue.append(3) # rear 에다가 넣는다 ( Enqueue )
queue.append(2)
queue.append(1)
queue.append(5)
queue.append(7)
ret = queue[0] # peek
ret = queue.popleft() # peek + dequeue

while queue :
    ret = queue.popleft()
    print(ret , end = ' ')