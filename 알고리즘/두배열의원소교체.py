# 5 3
# 1 2 5 4 3
# 5 5 6 6 5

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    l_arr, c_arr, r_arr = [], [], []
    for num in arr:
        if num < pivot:
            l_arr.append(num)
        elif num > pivot:
            r_arr.append(num)
        else:
            c_arr.append(num)
    return quick_sort(l_arr) + c_arr + quick_sort(r_arr)

def D_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    l_arr, c_arr, r_arr = [], [], []
    for num in arr:
        if num > pivot:
            l_arr.append(num)
        elif num < pivot:
            r_arr.append(num)
        else:
            c_arr.append(num)
    return quick_sort(l_arr) + c_arr + quick_sort(r_arr)

A = quick_sort(A)
B = D_quick_sort(B)

a = 0

for i in range(K):
    if A[i] < B[i]:
        A[i] = B[i]

for i in A:
    a += i

print(a) 
    

