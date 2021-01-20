# 큐 이용, BSP

# 다시 한번 해봐야 겠당!!

from collections import deque


m, n = map(int, input().split())

tmt_list = []

for _ in range(n):
    tmt_list.append(list(map(int, input().split())))

queue = deque([])

for i in range(n):
    for j in range(m):
        if tmt_list[i][j] == 1:
            queue.append((i,j))


# x,y = queue.popleft()
# print(x, y)

while queue:
    x,y=queue.popleft()

    move = [(-1,0), (1,0), (0,-1), (0,1)] # 상하좌우







for i in tmt_list:
    print(i)