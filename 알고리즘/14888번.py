"""
2021-02-08
"""
from itertools import permutations

N = int(input())
A_list = list(map(int, input().split()))
cal_list = list(map(int, input().split()))

per = []
for idx, val in enumerate(cal_list):
    if idx == 0:
        for j in range(val):
            per.append("+")
    elif idx == 1:
        for j in range(val):
            per.append("-")
    elif idx == 2:
        for j in range(val):
            per.append("*")
    else:
        for j in range(val):
            per.append("/")

per_list = list(permutations(per, len(per)))


max_num = -1000000000
min_num = 1000000000

for pers in per_list:
    num = A_list[0]
    for i in range(len(pers)):
        if pers[i] == "+":
            num = num + A_list[i+1]
        elif pers[i] == "-":
            num = num - A_list[i+1]
        elif pers[i] == "*":
            num = num * A_list[i+1]
        else:
            if num < 0:
                num = -(abs(num)//A_list[i+1])
            else:
                num = num//A_list[i+1]
    if max_num < num:
        max_num = num
    if min_num > num:
        min_num = num
print(max_num)
print(min_num)

