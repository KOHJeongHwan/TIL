import sys
sys.setrecursionlimit(50000)
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x][2] != x:
        parent[x][2] = find_parent(parent, parent[x][2])
    return parent[x][2]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b][2] = a
        return a
    else:
        parent[a][2] = b
        return b

def expend_list(parent):
    bin_list = [["", int(0), int(0)] for _ in range(len(parent)+1)]
    for i in range(len(parent)):
        bin_list[i] = parent[i]
    return bin_list


n = int(input())

for _ in range(n):
    f = int(input())
    parent = [["", int(0), int(0)]]
    
    for _ in range(f):
        a_idx = 0
        b_idx = 0
        a, b = input().split()

        for i in range(len(parent)):
            name, idx, papa = parent[i]
            if name == a:
                a_idx = idx
            if name == b:
                b_idx = idx
                
        if a_idx == 0:
            parent = expend_list(parent)
            parent[-1] = [a, len(parent)-1, len(parent)-1]
            a_idx = parent[-1][1]
        if b_idx == 0:
            parent = expend_list(parent)
            parent[-1] = [b, len(parent)-1, len(parent)-1]
            b_idx = parent[-1][1]

        papa_num = union_parent(parent, a_idx, b_idx)
        cnt = 0
        for i in range(1, len(parent)):
            if papa_num == find_parent(parent, parent[i][1]):
                cnt += 1
        print(cnt)
        print(parent)

        
                

