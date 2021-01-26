"""
2021-01-25
30분
그리디문제

"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(50000)

def binarySearch(array, target, left, right):
    mid_idx = (left+right)//2
    mid = array[mid_idx]
    if target == mid:
        print(array[mid_idx])
        return -1
    elif mid > target:
        binarySearch(array, target, left, mid_idx-1)
    elif mid < target:
        binarySearch(array, target, mid_idx+1, right)
    else:
        print(array(mid_idx))
        return mid_idx


n = int(input())
a_list = []
a_list = list(map(int, input().split()))
a_list.sort()



flag = True
target = 8
length = len(a_list)
left = 0
right = length-1
while flag:
    idx = binarySearch(a_list, target, 0, right)
    if idx == -1:
        



