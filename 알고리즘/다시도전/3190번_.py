"""
2021-01-30

"""
from collections import deque

# 보드의 크기 n
n = int(input())
# 사과의 개수 k
k = int(input())

graph = [[0 for i in range(n+2)] for i in range(n+2)]

# 벽 만들기
for i in range(n+2):
    for j in range(n+2):
        if i == 0:
            graph[i][j] = 2
        if j == 0:
            graph[i][j] = 2
        if i == n+1:
            graph[i][j] = 2
        if j == n+1:
            graph[i][j] = 2


# 사과의 위치
for _ in range(k):
    x, y = map(int, input().split())
    graph[x][y] = 1

# 방향 전환 횟수
move_time = int(input())

# 게임시작후 시간, 방향 변환 정보
# L 은 왼쪽 D 은 오른쪽 으로 90도
graph[1][1] = 4 # 시작지점

bam_go = 90
queue = deque([(1,1)])
play_time = 0
stop_flag = False
for i in range(move_time):
    sec, c = input().split()
    for j in range(int(sec)-play_time):
        # 전체 실행 횟수 +1
        play_time += 1
        # 방향 전환
        if play_time == int(sec):
            if c == 'D':
                bam_go += 90
            else:
                bam_go += 270
            bam_go = bam_go % 360
        print(bam_go)
        now_x, now_y = queue[0]
        # 아래
        if bam_go == 180:
            # 벽에 부딛혔을때
            if graph[now_x+1][now_y] == 2:
                stop_flag = True
                break
            # 사과를 안 먹었을때
            elif graph[now_x+1][now_y] == 0:
                b_x, b_y = queue.pop()
                graph[b_x][b_y] = 0
                queue.appendleft((now_x+1, now_y))
                graph[now_x+1][now_y] = 4
            # 사과 먹었을때
            elif graph[now_x+1][now_y] == 1:
                queue.appendleft((now_x+1, now_y))
                graph[now_x+1][now_y] = 4
            # 몸에 부딛혔을때
            elif (now_x+1,now_y) in queue:
                stop_flag = True
                break
        # 오른쪽
        elif bam_go == 90:
            # 벽에 부딛혔을때
            if graph[now_x][now_y+1] == 2:
                stop_flag = True
                break
            # 사과를 안 먹었을때
            elif graph[now_x][now_y+1] == 0:
                b_x, b_y = queue.pop()
                graph[b_x][b_y] = 0
                queue.appendleft((now_x, now_y+1))
                graph[now_x][now_y+1] = 4
            # 사과 먹었을때
            elif graph[now_x][now_y+1] == 1:
                queue.appendleft((now_x, now_y+1))
                graph[now_x][now_y+1] = 4
            # 몸에 부딛혔을때
            elif (now_x,now_y+1) in queue:
                stop_flag = True
                break
        # 위
        elif bam_go == 0:
            # 벽에 부딛혔을때
            if graph[now_x-1][now_y] == 2:
                stop_flag = True
                break
            # 사과를 안 먹었을때
            elif graph[now_x-1][now_y] == 0:
                b_x, b_y = queue.pop()
                graph[b_x][b_y] = 0
                queue.appendleft((now_x-1, now_y))
                graph[now_x-1][now_y] = 4
            # 사과 먹었을때
            elif graph[now_x-1][now_y] == 1:
                queue.appendleft((now_x-1, now_y))
                graph[now_x-1][now_y] = 4
            # 몸에 부딛혔을때
            elif (now_x-1,now_y) in queue:
                stop_flag = True
                break
        #왼쪽
        elif bam_go == 270:
            # 벽에 부딛혔을때
            if graph[now_x][now_y-1] == 2:
                stop_flag = True
                break
            # 사과를 안 먹었을때
            elif graph[now_x][now_y-1] == 0:
                b_x, b_y = queue.pop()
                graph[b_x][b_y] = 0
                queue.appendleft((now_x, now_y-1))
                graph[now_x][now_y-1] = 4
            # 사과 먹었을때
            elif graph[now_x][now_y-1] == 1:
                queue.appendleft((now_x, now_y-1))
                graph[now_x][now_y-1] = 4
            # 몸에 부딛혔을때
            elif (now_x,now_y-1) in queue:
                stop_flag = True
                break
        # 그려진 그래프 확인
        for i in range(n+2):
            print(graph[i])
        print("현재 뱀", queue)
    if stop_flag:
        break


print(play_time)


# 몇초에 게임이 끝나는가?



