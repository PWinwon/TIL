def solution(str1, str2):
    answer = 0
    str1 = str1.upper()
    str2 = str2.upper()
    dict1 = dict()
    for i in range(len(str1)-1):
        sample = str1[i:i+2]
        if ord('A') <= ord(sample[0]) <= ord('Z') and ord('A') <= ord(sample[1]) <= ord('Z'):
            if sample in dict1.keys():
                dict1[sample][0] += 1
            else:
                dict1[sample] = [0, 0]
                dict1[sample][0] += 1
    for j in range(len(str2)-1):
        sample = str2[j:j+2]
        if ord('A') <= ord(sample[0]) <= ord('Z') and ord('A') <= ord(sample[1]) <= ord('Z'):
            if sample in dict1.keys():
                dict1[sample][1] += 1
            else:
                dict1[sample] = [0, 0]
                dict1[sample][1] += 1
    min_val = 0
    max_val = 0
    for idx, val in dict1.items():
        min_val += min(val)
        max_val += max(val)
    if min_val == 0 and max_val == 0:
        answer = 1
    else:
        answer = min_val / max_val
    return int(answer * 65536)