from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 1
    que = deque([0]*(bridge_length-1))
    idx = 1
    que.append(truck_weights[0])
    my_w = truck_weights[0]
    while my_w:
        answer += 1
        temp = que.popleft()
        if temp:
            my_w -= temp
        if idx < len(truck_weights) and my_w+truck_weights[idx] <= weight:
            que.append(truck_weights[idx])
            my_w += truck_weights[idx]
            idx += 1
        else:
            que.append(0)
    return answer