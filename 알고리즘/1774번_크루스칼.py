"""
2021-01-20

"""
import sys
sys.setrecursionlimit(50000)
input = sys.stdin.readline
# 부모노드 찾는 함수
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
# 부모 노드 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
# 부모노드 자기 자신으로 초기화
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

edges = [] # 전체 간선을 저장할 리스트
god = [0] # 문제에서 제공되는 좌표값을 저장(1부터 시작하기 위해 의미없는 값을 넣어 0번을 제거)

for _ in range(n):
    a, b = map(int, input().split())
    god.append((a, b))

connect_node = [] # 반드시 이어지는 노드 좌표 저장
for _ in range(m):
    a, b = map(int, input().split())
    connect_node.append((a, b))

# 전체 간선 길이 구하기
for i in range(1, len(god)-1):
    for j in range(i+1, len(god)):
        a1, b1 = god[i]
        a2, b2 = god[j]
        cost = ((a1-a2)**2 + (b1-b2)**2)**0.5
        edges.append((cost, i, j))

# 필수 노드들 부터 parent 업데이트
for edge in connect_node:
    a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)

# cost 가 작은순으로 정렬
edges.sort()

result = 0
# 자동으로 이어진 노드들은 넘어간다.
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print("{:.2f}".format(result))