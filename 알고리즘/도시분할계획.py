"""
2021-01-15
크루스칼 문제
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4

8
"""
import sys
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

# 마을 개수, 간선 개수
n, m = map(int, input().split())
parent = [0] * (n+1)
edge = []
results = []
result = 0

for i in range(1, n+1):
    parent[i] = i

for _ in range(m):
    a, b, c = map(int, input().split())
    edge.append((c, a, b))
edge.sort()

for i in edge:
    cost, a, b = i
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        results.append(cost)
        
for i in results[:-1]:
    result += i

print(result)

#===========================================
# 프림으로 풀기
