import sys

list_n = [0] * 9

for i in range(0,9):
    list_n[i] = int(input())

for j in range(0,9):
    if(max(list_n) == list_n[j]):
        print(max(list_n))
        print(j+1)

