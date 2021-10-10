T = int(input())

for tc in range(1, T+1):
    s1, s2 = input().split()
    used = {
        'a': 0, 'b': 0, 'c': 0, 'd': 0,
        'e': 0, 'f': 0, 'g': 0, 'h': 0,
        'i': 0, 'j': 0, 'k': 0, 'l': 0,
        'm': 0, 'n': 0, 'o': 0, 'p': 0,
        'q': 0, 'r': 0, 's': 0, 't': 0,
        'u': 0, 'v': 0, 'w': 0, 'x': 0,
        'y': 0, 'z': 0,
    }
    result = 0
    for s in s1:
        used[s] += 1
    s2_dict = {
        'a': 0, 'b': 0, 'c': 0, 'd': 0,
        'e': 0, 'f': 0, 'g': 0, 'h': 0,
        'i': 0, 'j': 0, 'k': 0, 'l': 0,
        'm': 0, 'n': 0, 'o': 0, 'p': 0,
        'q': 0, 'r': 0, 's': 0, 't': 0,
        'u': 0, 'v': 0, 'w': 0, 'x': 0,
        'y': 0, 'z': 0,
    }
    for idx in range(len(s1)):
        s2_dict[s2[idx]] += 1
    if used == s2_dict:
        result += 1
    for i in range(len(s1), len(s2)):
        s2_dict[s2[i]] += 1
        s2_dict[s2[i-len(s1)]] -= 1
        if used == s2_dict:
            result += 1
    print('#{} {}'.format(tc, result))