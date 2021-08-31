def solution(phone_book):
    answer = True
    dict1 = {}
    for pn in phone_book:
        dict1[pn] = 1
    for phn in phone_book:
        sample = ""
        for num in phn:
            sample += num
            if sample in dict1 and sample != phn:
                return False
    return answer