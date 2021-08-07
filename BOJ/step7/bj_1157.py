chars = input()
chars = chars.upper()

result = dict()

for char in chars:
    if char in result.keys():
        result[char] += 1
    else:
        result[char] = 1

max_val = 0
for val in result.values():
    if val > max_val:
        max_val = val


max_list = []
for k, val in result.items():
    if val == max_val:
        max_list.append(k)

if len(max_list) == 1:
    print(max_list[0])
else:
    print('?')
