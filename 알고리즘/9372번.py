"""
2021-01-19
길이가 없는 간선, 모든 노드를 거치는 최소 간선의 갯수 구하기
크루스칼 알고리즘 이용

하지만 n-1 로 풀어도 가능!
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

# 테스트 케이스
T = int(input())

for _ in range(T):
    # 국가의 수, 비행기의 종류
    n, m = map(int, input().split())

    parent = [0] * (n+1)
    edges = []
    result = 0

    for i in range(1, n+1):
        parent[i] = i
    
    for _ in range(m):
        a, b = map(int, input().split())
        edges.append((1, a, b))

    edges.sort()

    for edge in edges:
        cost, a, b = edge

        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost
    print(result)

# 프림
