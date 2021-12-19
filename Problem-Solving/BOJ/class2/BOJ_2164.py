from collections import deque

N = int(input())

cards = deque([i for i in range(1, N+1)])
flag = True

while len(cards) > 1:
    if flag:
        cards.popleft()
        flag = False

    else:
        card = cards.popleft()
        cards.append(card)
        flag = True

print(cards[0])