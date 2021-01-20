n, m = map(int, input().split())

tt_list = list(map(int, input().split()))

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    l_arr, c_arr, r_arr = [], [], []
    for num in arr:
        if num > pivot:
            l_arr.append(num)
        elif pivot > num:
            r_arr.append(num)
        else:
            c_arr.append(num)
    return quick_sort(l_arr) + c_arr + quick_sort(r_arr)
        
# arr = [3, 5, 1, 2, 9, 6, 4, 7, 5]
# arr = [19, 15, 10, 17]

sorted_list = quick_sort(tt_list)
# print("정렬된 리스트: ", sorted_list)
# n = 4
# m = 6

mm_list = []
max_num = sorted_list[0]
# print(max_num)

while max_num > 0:
    for num in sorted_list:
        stop_num = num-max_num
        if stop_num < 0:
            break
        mm_list.append(num-max_num)
    # print(mm_list)
    
    result_num = 0
    for i in mm_list:
        result_num += i
    if result_num < m:
        max_num -= 1
        mm_list=[]
    else:
        # print(max_num)
        break
    


