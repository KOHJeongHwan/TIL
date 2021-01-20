import sys
input = sys.stdin.readline

# 노드 갯수
n = int(input())
# 간선 갯수
m = int(input())
# start = int(input())
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    u, v, w = map(int, input().split())
    if graph[u][v] == INF:
        graph[u][v] = w
    else:
        if graph[u][v] > w:
            graph[u][v] = w

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print("0", end=" ")
        else:
            print(graph[i][j], end=" ")
    print()