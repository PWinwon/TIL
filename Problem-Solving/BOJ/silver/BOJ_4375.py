

while True:
    try:
        N = int(input())

        target = '1'
        result = 1
        while True:
            if int(target) % N == 0:
                break
            target += '1'
            result += 1

        print(result)
    except:
        break