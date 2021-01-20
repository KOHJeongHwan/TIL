# 5
# 8 3 7 9 2
# 3
# 5 7 9

N = int(input())
a_lst = list(map(int, input().split()))
M = int(input())
b_lst = list(map(int, input().split()))

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    l_arr, c_arr, r_arr = [], [], []
    for num in arr:
        if num < pivot:
            l_arr.append(num)
        elif pivot < num:
            r_arr.append(num)
        else:
            c_arr.append(num)
    return quick_sort(l_arr) + c_arr + quick_sort(r_arr)

def B_search(arr, target, l, r):
    mid_idx = (l + r)//2
    mid = arr[mid_idx]

    print(l, mid_idx, r)

    if target == mid:
        print("yes")
        return True
    elif r == l:
        print("no")
        return False
    elif mid > target:
        B_search(arr, target, l, mid_idx-1)
    elif mid < target:
        B_search(arr, target, mid_idx+1, r)


a_lst = quick_sort(a_lst)
l = 0
r = len(a_lst)-1
for i in b_lst:
    B_search(a_lst, i, l, r)