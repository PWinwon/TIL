def made_knum(num, k):
    ret = ''
    while num > 0:
        ret = str(num%k) + ret
        num //= k

    return ret


def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    k_num = made_knum(n, k)
    k_list = list(k_num.split('0'))
    max_len = 0
    for kl in k_list:
        temp = len(kl)
        if max_len < temp:
            max_len = temp
    
    for kl in k_list:
        if kl and kl != '1':
            kn = int(kl)
            if is_prime(kn):
                answer += 1
                                
    return answer