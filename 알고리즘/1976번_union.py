# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        # parent[x] = find_parent(parent, parent[x])
        return find_parent(parent, parent[x])
    # return parent[x]
    return x

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
m = int(input())

# 2차원 배열 만들기
graph = [ [0]*(n+1) for i in range(n+1)]
for i in range(1, n+1):
    a = list(map(int, input().split()))
    for j in range(1, n+1):
        graph[i][j] = a[j-1]

visited = list(map(int, input().split()))

parent = [0] * (n+1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, n+1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == 1:
            union_parent(parent, i, j)
            print(parent)
flag = False

for i in range(m-1):
    if find_parent(parent, visited[i]) != find_parent(parent, visited[i+1]):
        flag = True
        break

print(parent)

if flag:
    print("NO")
else:
    print("YES")
