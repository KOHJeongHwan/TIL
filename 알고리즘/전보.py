"""
최단 거리 문제

이것이 다익스트라로 풀면 될듯 ㄹㅇ
"""
INF = (1e9)
# 도시수, 간선수, 출발 도시
n, m, c = map(int, input().split())

graph = [[] for i in range(n+1)]

for _ in range(m):
    # 출발 도시, 도착 도시, 거리
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

visited = [False] * (n+1)

distance = [INF] * (n+1)

def small():
    min_value = INF
    idx = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            idx = i
    return idx

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for i in graph[start]:
        distance[i[0]] = i[1]
    for _ in range(n-1):
        idx = small()
        visited[idx] = True

        for i in graph[idx]:
            cost = distance[idx] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
    # print(distance)

dijkstra(c)

cnt = 0
max_time = 0

for i in range(1, n+1):
    if distance[i] != INF and distance[i] != 0:
        if max_time < distance[i]:
            max_time = distance[i]
        cnt += 1
print(cnt, max_time)
