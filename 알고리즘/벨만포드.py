def bellman_ford(graph, start):
    distance, predecessor = dict(), dict()

    for node in graph:
        distance[node], predecessor[node] = float('inf'), None
    distance[start] = 0

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbour in graph[node]:  # 각 정점마다 모든 인접 정점들을 탐색
                # (기존 인접 정점까지의 거리 > 기존 현재 정점까지 거리 + 현재 정점부터 인접 정점까지 거리)인 경우 갱신
                if distance[neighbour] > distance[node] + graph[node][neighbour]:
                    distance[neighbour] = distance[node] + graph[node][neighbour]
                    predecessor[neighbour] = node
                    print("predecessor: ", predecessor)    

    return distance, predecessor



graph = {
    'A': {'B': -1, 'C':  4},
    'B': {'C':  3, 'D':  2, 'E':  2},
    'C': {},
    'D': {'B':  1, 'C':  5},
    'E': {'D': -3}
}

distance, predecessor = bellman_ford(graph, start='A')

print(distance)
print(predecessor)

