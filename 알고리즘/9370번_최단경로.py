import sys
import heapq
input=sys.stdin.readline

# 테스트 케이스
# test = int(input())

# 정점의 갯수, 간선의 갯수, 목적지 후보 갯수
n, m, t = map(int, input().split())
# 출발지, 지나가야할 노드 2개
s, g, h = map(int, input().split())
INF = int(1e9)

graph = [[] for i in range(n+1)]

for i in range(m):
    # 시작 노드, 도착 노드, 간선 길이
    a, b, d = map(int, input().split())
    graph[a].append((b, d))
    graph[b].append((a, d))

x_list=[]

for i in range(t):
    # print("t: ", i)
    x_list.append(int(input()))

# x_list = x_list.sort()
# print(x_list)
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

s_dist = dijkstra(s)
g_dist = dijkstra(g)
h_dist = dijkstra(h)
# print(graph[g])
# for i in graph[g]:
#     if i[0] == h:
#         doro = i[1]

min_g = 100
for i in g_dist:
    if i == 0:
        continue
    elif min_g < i:
        min_g = i

min_h = 100
for i in h_dist:
    if i == 0:
        continue
    elif min_h < i:
        min_h = i


min_g_list = []
min_h_list = []

print("ww", min_g, min_h)

for i in x_list:
    if g_dist[i] == min_g:
        min_g_list.append(i)
    if h_dist[i] == min_h:
        min_h_list.append(i)

if s_dist[g] + min_g > s_dist[h] + min_h:
    print(min_h_list)
else:
     print(min_g_list)