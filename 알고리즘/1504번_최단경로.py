import sys
import heapq
input=sys.stdin.readline


# 정점의 갯수, 간선의 갯수
n, e = map(int, input().split())

INF = int(1e9)

graph = [[] for i in range(n+1)]

for i in range(e):
    # 시작 노드, 도착 노드, 간선 길이
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

start1, start2 = map(int, input().split())

def dijkstra(start):
    distance = [INF] *(n+1)
    q = []
    # 노드 최단 거리, 노드
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q: # q가 빌 때까지
        dist, now = heapq.heappop(q)
        # 현재 길이가 힙에 저장된 길이보다 짧다 = 이미 처리된 노드  라면 무시!
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

s_dist = dijkstra(1)
s1_dist = dijkstra(start1)
s2_dist = dijkstra(start2)


# print(s_dist)
# print(s1_dist)
# print(s2_dist)
# print(s_dist[2]+s1_dist[3]+s2_dist[n], s_dist[3]+s2_dist[2]+s1_dist[n])
result = min(s_dist[start1]+s1_dist[start2]+s2_dist[n], s_dist[start2]+s2_dist[start1]+s1_dist[n])
if result < INF:
    print(result)
else:
    print(-1)