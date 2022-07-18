M, S = map(int, input().split(':'))
cnt = 1
cnt += (M//10 + M%10)
if S < 30:
    cnt += (S//10)
elif S >= 30:
    cnt += ((S-30)//10)

print(cnt)