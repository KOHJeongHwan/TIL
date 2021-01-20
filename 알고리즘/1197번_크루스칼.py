"""
2021-01-19
크루스칼 알고리즘 이용
음수가 존재하는 간선이지만 별다른건 없음
"""

import sys
sys.setrecursionlimit(50000)
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
# 노드의 개수, 간선의 개수
v, e = map(int, input().split())

parent = [0] * (v+1)
edges = []
# 노드를 자기자신으로 초기화
for i in range(1, v+1):
    parent[i] = i
# 간선 개수 만큼 반복
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 간선의 코스트로 비교할것이기 때문에 cost를 맨 앞에 둔다.
    edges.append((cost, a, b))

edges.sort()
print(edges)
result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)
