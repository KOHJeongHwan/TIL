import heapq

# 정점의 갯수, 간선의 갯수
n, e = map(int, input().split())
start = int(input())


INF = int(1e9)

graph = [[] for i in range(n+1)]
distance = [INF] *(n+1)
visited = [False] * (n+1)

for i in range(e):
    # 시작 노드, 도착 노드, 간선 길이
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

def pream(start):
    q = []
    # 노드 최단 거리, 노드
    heapq.heappush(q, (0, start))
    # distance[start] = 0
    visited[start] = True

    while q: # q가 빌 때까지
        dist, now = heapq.heappop(q)
        # 현재 길이가 힙에 저장된 길이보다 짧다 = 이미 처리된 노드  라면 무시!
        # if distance[now] < dist:
        #     continue
        for i in graph[now]:
            # cost = dist + i[1]
            # if cost < distance[i[0]]:
            #     distance[i[0]] = cost

            heapq.heappush(q, (cost, i[0]))

pream(start)
print("다익스트라")
for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])