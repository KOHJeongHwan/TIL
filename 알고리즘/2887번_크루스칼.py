"""
2021-01-20
골드2 문제
크루스칼을 이용할 뿐만 아니라 메모리 제한에도 신경써야한다.
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

# 노드 갯수
n = int(input())

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

edges = []
star = [0]
for _ in range(1, n+1):
    a, b, c = map(int, input().split())
    star.append((a, b, c))

result = 0

x_list = []
y_list = []
z_list = []

for i in range(1, n+1):
    x_list.append((star[i][0], i))
    y_list.append((star[i][1], i))
    z_list.append((star[i][2], i))

x_list.sort()
y_list.sort()
z_list.sort()

all_list = []
for i in range(n-1):
    all_list.append((abs(x_list[i][0]-x_list[i+1][0]), x_list[i][1], x_list[i+1][1]))
    all_list.append((abs(y_list[i][0]-y_list[i+1][0]), y_list[i][1], y_list[i+1][1]))
    all_list.append((abs(z_list[i][0]-z_list[i+1][0]), z_list[i][1], z_list[i+1][1]))

all_list.sort()

for edge in all_list:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)
