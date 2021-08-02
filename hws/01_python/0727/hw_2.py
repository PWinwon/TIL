test_list = ['apple', 'orange']
print(test_list)

test_list.append(['peach'])
print(f"#test_list.append(['peach']) >>", test_list)

test_list.extend(['melon'])
print(f"#test_list.extend(['melon']) >>", test_list)

test_list.append('banana')
print(f"#test_list.append('banana') >>", test_list)

test_list.extend('lemon')
print(f"#test_list.extend('lemon') >>", test_list)