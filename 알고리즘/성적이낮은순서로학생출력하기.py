n = int(input())

dic = {}
for _ in range(n):
    nam, sco= input().split(" ")
    dic[nam] = int(sco)

print(type(list(dic.values())[0]))


def counting_sorted(dic):
    cont_lst = [0] * 101
    sort_lst = [0] * len(list(dic.values()))

    for i in list(dic.values()):
        cont_lst[i] += 1

    for i in range(0, 101):
        cont_lst[i] += cont_lst[i-1]

    for i in range(len(dic)):
        sort_lst[cont_lst[list(dic.values())[i]]-1] = list(dic.values())[i]
        cont_lst[list(dic.values())[i]] -= 1
        
    return sort_lst
        
print(counting_sorted(dic))

