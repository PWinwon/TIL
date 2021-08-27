shape_lst = ['S', 'D', 'H', 'C']

test_case = int(input())

for tc in range(test_case):
    cards = input()
    cnt_lst = [13, 13, 13, 13]
    card_lst = []
    ero = 0
    for i in range(0, len(cards), 3):
        card_lst.append(cards[i:i+3])
    for j in range(len(card_lst)-1):
        for k in range(j+1, len(card_lst)):
            if card_lst[j] == card_lst[k]:
                ero = 1
    if ero:
        print('#{} ERROR'.format(tc+1))
    else:
        for card in card_lst:
            for idx in range(4):
                if card[0] == shape_lst[idx]:
                    cnt_lst[idx] -= 1
        print('#{} {}'.format(tc+1, ' '.join(map(str, cnt_lst))))