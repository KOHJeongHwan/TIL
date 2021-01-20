n = int(input())
lst = []

for _ in range(n):
    m = int(input())
    if m == None:
        break
    lst.append(m)

for i in range(1, len(lst)):
    for j in range(i, 0, -1):
        if lst[j] > lst[j-1]:
            lst[j], lst[j-1] = lst[j-1], lst[j]
        else : break

for k in lst:
    print(k, end="")
    print(" ", end="")


# 삽입정렬



    