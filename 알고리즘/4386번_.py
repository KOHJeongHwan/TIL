"""
2021-01-19
이것도 크루스칼 문제인듯
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


n = int(input())

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i
edges = []
star_list = []
for i in range(n):
    a, b = map(float, input().split())
    star_list.append((a, b))

for i in range(n-1):
    for j in range(i+1, n):
        a1, b1 = star_list[i]
        a2, b2 = star_list[j]

        cost = ((a1 - a2)**2 + (b1 - b2)**2)**0.5
        edges.append((cost, i+1, j+1))

edges.sort()
result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(round(result, 2))