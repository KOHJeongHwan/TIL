"""
2021-01-22
위상정렬 문제
골드1

다시 풀기

"""
import sys
input = sys.stdin.readline

from collections import deque

# 테스트 케이스 개수
n = int(input())

for _ in range(n):
    team_num = int(input())

    graph = [[] for i in range(team_num+1)]
    for i in range(1, team_num+1):
        num = int(input())
    
    indegree = [0] * (team_num+1)
    graph = [[] for i in range(team_num+1)]

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if team_list[a] < team_list[b]: # 작년에 a가 b보다 등수가 높다면
            graph[b].append(a)
            indegree[a] += 1
        else:
            graph[a].append(b)
            indegree[b] += 1
    
    topology_sort()
    
def topology_sort():
    result = [] # 올해 순서
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    # 쿠가 빌 때까지 반복
    while q:
        # 큐에 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 위상 정렬을 수행한 결과 출력
    for i in result:
        print(i, end=' ')

topology_sort()

