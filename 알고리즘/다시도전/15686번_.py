"""
2021-02-01

"""
# 도시의 크기, 치킨집 최대 갯수
n, m = map(int, input().split())
# 도시정보

h_lst = [] # 집
c_lst = [] # 취킨
# 각각의 좌표값을 받아서 따로 저장
for i in range(n):
    in_list = list(map(int, input().split()))
    for j in range(n):
        if in_list[j] == 1:
            h_lst.append((i+1, j+1))
        elif in_list[j] == 2:
            c_lst.append((i+1, j+1))
        else:
            pass

# print(h_lst)
# print(c_lst)

small_lenght = []

# 집마다
for h in range(len(h_lst)):
    lenght = []
    # 치킨집 거리를 계산합니다.
    for c in range(len(c_lst)):
        lenght.append((abs(c_lst[c][0]-h_lst[h][0]) + abs(c_lst[c][1]-h_lst[h][1]), c))
    # 가까운 치킨집 거리를 알기위해 sort
    lenght.sort()

    print("c",c)
    print(lenght)
    # 제일 가까운 치킨집 좌표를 
    small_lenght.append(lenght[0])

    # for i in range(m+1): # 제일 작은 m개를 뽑는다.
    #     small_lenght.append(lenght[i])

print("small",small_lenght)

how_many_c = [0 for _ in range(len(c_lst))]
hmc = 0

# for i in small_lenght:
#     if how_many_c[i[1]] == 0:
#         how_many_c[i[1]] += 1
#         hmc += 1
# if hmc < 
        






    


# 폐기
# c_len_lst = []
# for c in range(len(c_lst)):
#     lenght = 0
#     for h in range(len(h_lst)):
#         lenght += abs(c_lst[c][0]-h_lst[h][0]) + abs(c_lst[c][1]+h_lst[h][1])
#     c_len_lst.append((c, lenght))
# print(c_len_lst)





