#1
# def duplicated_letters(word):
#     result = []
#     for char in word:
#         # 1. 조건문으로 리스트에 중복되는 값이 들어가지 않도록 하는 방법
#         if word.count(char) > 1: # and char not in result:
#             result.append(char)
#     result = list(set(result)) # 2. set 으로 리스트 중복 제거하는 방법
#     return result

# print(duplicated_letters('apple'))
# print(duplicated_letters('banana'))

#2
# def low_and_up(word):
    # 1. for 사용
    # result = ''
    # for idx, w in enumerate(word):
    #     if idx % 2:
    #         result += word[idx].upper()
    #     else:
    #         result += word[idx].lower()
    # 2. 리스트 컴프리헨션 + 조건표현식
#     result = [char.upper() if idx % 2 else char.lower() for idx, char in enumerate(word)]
#     return ''.join(result)

# res1 = low_and_up('apple')
# res2 = low_and_up('banana')
# print(res1)
# print(res2)

#3
# def lonely(numbers):
#     result = [numbers[0]]
#     for num in numbers:
#         if result[-1] != num:
#             result.append(num)
#     return result

# res1 = lonely([1, 1, 3, 3, 0, 1, 1])
# res2 = lonely([4, 4, 4, 3, 3])
# print(res1)
# print(res2)