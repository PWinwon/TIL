def gcd(a, b):
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return abs(a)


# 성원이가 말하는 답의 개수는 전체 순열의 경우의 수
# 정답은 순열 중 조건을 만족

N = int(input())

lst = []

for n in range(N):
    string_temp = input()
    string_temp2 = string_temp[::-1]
    lst.append(string_temp2)
K = int(input())

# 성원이가 말할 수 있는 답의 개수 : N!

nfact = 1
for n in range(1, N+1):
    nfact *= n

# 1~ 10^50 50개의 배열에 각각 K로 나눈 나머지

# 123에 45를 붙이는 순열에서 나머지를 구한다고 가정
# 12345 mod 12 = 12mod7 + 45mod7 = 123mod7 * 100mod7 + 45mod7 %7 = 0~6  # -2 + 7 = 5
#                                       1       2          3
# 12mod7 = 6mod7 + 6mod7 = 12mod7 (0 = 7 = 14 = 21)
# 13mod7 = 6 + 1mod7 = 7mod7 = 0

# (2) 50자리 확장에 대한 K에 대한 나머지 미리 구하기 [extnd_lst]

extnd_lst = [0] * 51
extnd_lst[0] = 1

for i in range(1, 51):
    extnd_lst[i] = (extnd_lst[i-1] * 10) % K


# (1) 확장되었을 때 나머지 미리 구하기
mod_lst = [0] * N
for i in range(N):
    temp = 0
    for j in range(len(lst[i])):
        temp += (int(lst[i][j]) * extnd_lst[j]) % K
        temp %= K
    mod_lst[i] = temp



# dp 만들기
# dp[현재뽑은숫자들을 2진수형태로 비트마스킹 후 10진수로 변환한 index][K로 나누었을 때 나머지]
dp = [[0] * K for _ in range(1<<N)]
dp[0][0] = 1
for i in range(1<<N):
    for j in range(K):
        for k in range(N):
            if (i&(1<<k)) == 0:
                temp = j*extnd_lst[len(lst[k])]
                temp %= K
                temp += mod_lst[k]
                temp %= K
                dp[i|(1<<k)][temp] += dp[i][j]


g = gcd(dp[(1<<N)-1][0], nfact)
print('{}/{}'.format(dp[(1<<N)-1][0] // g, nfact//g))