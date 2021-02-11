"""
2021-02-11
"""
N = int(input())

graph = [[0 for i in range(N+2)]]
insert = []
for _ in range(N):
    insert = [0] + list(input().split()) + [0]

    graph.append(insert)
graph.append([0 for i in range(N+2)])

def solution(N, graph):

    t_list = []
    # 선생님 자리 저장
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][j] == "T":
                t_list.append((i,j))

    # 선생님 바로 옆에 학생이 있는 경우는 "NO"
    for idx in t_list:
        x, y = idx
        if graph[x+1][y] == "S":
            return "NO"
        if graph[x-1][y] == "S":
            return "NO"
        if graph[x][y+1] == "S":
            return "NO"
        if graph[x][y-1] == "S":
            return "NO"

    # T 상하좌우에 S 가 있는지 확인
    for idx in t_list:
        x, y = idx
        # 아래
        for num in range(1, N+1):
            # 확인하는 도중, 벽이나 T 가 있을경우 break
            if graph[x+num][y] == 0 or graph[x+num][y] == "T":
                break
            # S 를 만난다면, 그 동안의 길에 +1
            if graph[x+num][y] == "S":
                for down in range(x+1, x+num):
                    if graph[down][y] == "X":
                        graph[down][y] = 1
                    elif graph[down][y] == 1:
                        graph[down][y] += 1
                break
        # 위
        for num in range(1, N+1):
            if graph[x-num][y] == 0 or graph[x-num][y] == "T":
                break
            if graph[x-num][y] == "S":
                for up in range(x-num+1, x):
                    if graph[up][y] == "X":
                        graph[up][y] = 1
                    elif graph[up][y] == 1:
                        graph[up][y] += 1
                break
        # 오른쪽
        for num in range(1, N+1):
            if graph[x][y+num] == 0 or graph[x][y+num] == "T":
                break
            if graph[x][y+num] == "S":
                for right in range(y+1, y+num):
                    if graph[x][right] == "X":
                        graph[x][right] = 1
                    elif graph[x][right] == 1:
                        graph[x][right] += 1
                break
        # 왼쪽
        for num in range(1, N+1):
            if graph[x][y-num] == 0 or graph[x][y-num] == "T":
                break
            if graph[x][y-num] == "S":
                for left in range(y-num+1, y):
                    if graph[x][left] == "X":
                        graph[x][left] = 1
                    elif graph[x][left] == 1:
                        graph[x][left] += 1
                break

    print("")
    for i in range(1, N+1):
        for j in range(1, N+1):
            print(graph[i][j], end=" ")
        print("")

    # 기둥(B)를 크로스된 부분(2)에 먼저 설치
    for i in range(1, N+1):
        for j in range(1, N+1): 
            if graph[i][j] == 2:
                graph[i][j] = "B"
                # B 기준으로 상하좌우에 1를 없앤다.
                # 아래
                for num in range(1, N+1):
                    # 벽이나, S나 T를 만나면 break
                    if graph[i+num][j] == 0 or graph[i+num][j] == "S" or graph[i+num][j] == "T":
                        break
                    if graph[i+num][j] == 1: 
                        graph[i+num][j] = "X"
                # 위
                for num in range(1, N+1):
                    if graph[i-num][j] == 0 or graph[i-num][j] == "S" or graph[i-num][j] == "T":
                        break
                    if graph[i-num][j] == 1: 
                        graph[i-num][j] = "X"
                # 오른쪽
                for num in range(1, N+1):
                    if graph[i][j+num] == 0 or graph[i][j+num] == "S" or graph[i][j+num] == "T":
                        break
                    if graph[i][j+num] == 1: 
                        graph[i][j+num] = "X"
                # 왼쪽
                for num in range(1, N+1):
                    if graph[i][j-num] == 0 or graph[i][j-num] == "S" or graph[i][j-num] == "T":
                        break
                    if graph[i][j-num] == 1: 
                        graph[i][j-num] = "X"
    # 나머지 1들은, 어디에나 기둥을 설치해도 되는 장소
    # 나는 임의로 T근처에 설치
    for idx in t_list:
        x, y = idx
        if graph[x+1][y] == 1:
            graph[x+1][y] = "B"
        if graph[x-1][y] == 1:
            graph[x-1][y] = "B"
        if graph[x][y+1] == 1:
            graph[x][y+1] = "B"
        if graph[x][y-1] == 1:
            graph[x][y-1] = "B"


    print("")
    for i in range(1, N+1):
        for j in range(1, N+1):
            print(graph[i][j], end=" ")
        print("")

    # graph에서 B개수를 cnt에 저장
    cnt = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][j] == "B":
                cnt += 1
    # B가 3 이상이면 NO
    if cnt > 3:
        return "NO"
    else:
        return "YES"

print(solution(N, graph))
                

