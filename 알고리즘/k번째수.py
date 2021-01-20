# 이진탐색

n = int(input())

k = int(input())

target = 25
m_list = [1!, 2!, 3!, 4!, 5!, 5!+4, 5!+4+3, 5!+4+3+2, 5!+4+3+2+1]
length = len(m_list)

m_list.sort()
left = 0 
right = length-1

while left<=right:
    mid = (left+right)//2
    if m_list[mid] == target:
        print(mid+1)
        break
    elif m_list[mid]>target:
        right = mid-1
    else :
        left = mid+1