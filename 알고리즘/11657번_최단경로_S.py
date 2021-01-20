n, m = map(int, input().split())

graph = [[] for i in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
print(graph)

INF = int(1e9)

distance = [INF] * (n+1)

distance[1] = 0
for _ in range(n-1): # 최단 사이클은 n-1이라서!
    for node in range(1, n+1): # distance에 들어갈때 편할려구.
        for i in graph[node]:
            if distance[node] != INF:
                if distance[i[0]] > distance[node] + i[1]:
                    distance[i[0]] = distance[node] + i[1]
                    print(distance)

result = 0

for node in range(1, n+1):
    for i in graph[node]:
        if distance[node] != INF:
            if distance[i[0]] > distance[node] + i[1]:
                result = -1
        
if result == -1:
    print(-1)
else:
    a = distance[2:]
    for i in a:
        if i == INF:
            print(-1)
        else:
            print(i)


