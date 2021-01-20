"""
union-find 정렬?
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1

NO
NO
YES
"""
#  팀갯수 ,입력 수
n, m = map(int, input().split())

parent = [0] * (n+1)
# 부모노드를 자기 자신으로 초기화
for i in range(1, n+1):
    parent[i] = i

# 부모노드 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 간선 갯수만큼 반복
for i in range(m):
    x, a, b = map(int, input().split())
    if x == 0:
        union(parent, a, b)
    if x == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")

