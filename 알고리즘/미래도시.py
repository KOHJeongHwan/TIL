"""
길찾기

1출발, k 경유, n 도착

개선된 다익스트라 2번 쓰면 될듯!
"""
import sys

input = sys.stdin.readline
INF = int(1e9)


# 노드와 간선 갯수 입력
n, m = map(int, input().split())

graph = [[] for i in range(n + 1)]


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

X , K = map(int, input().split())

def dijkstra(start, end):
    distance = [INF] * (n+1)

    visited = [False] * (n + 1)
    
    distance[start] = 0

    idx = 0 # 가장 최단 거리가 짧은 노드(인덱스)


    for _ in range(n - 1):
        min_value = int(1e9)
        for i2 in range(1, n+1):
            if distance[i2] < min_value and not visited[i2]:
                min_value = distance[i2]
                idx = i2
        visited[idx] = True        
        for j in graph[idx]:
            cost = distance[idx] + 1
            if cost < distance[j]:
                distance[j] = cost
                print(distance)
    # print(distance)
    for i in range(1, n+1):
        print(distance[i])
        if distance[i] == INF:
            result = -1
        else:
            result = distance[end]
    
    return result

StoX = dijkstra(1, K)
XtoK = dijkstra(K, X)

if StoX == -1:
    print("StoX: ",-1)
elif XtoK == -1:
    print("XtoK: ",-1)
else:
    print(StoX+XtoK)





