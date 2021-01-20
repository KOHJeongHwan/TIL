N = int(input())
w_lst = []
for _ in range(N):
    w_lst.append(input())

w_dic = {}
for i in range(N):
    length, word= len(w_lst[i]), w_lst[i]
    w_dic[word] = length

def counting_sorted(arr, K):
    c = [0] * K
    sorted_arr = [0] * len(arr)
    
    for i in arr:
        c[i] += 1
    
    for i in range(1,K):
        c[i] += c[i-1]
   
    for i in range(len(arr)):
        sorted_arr[c[arr[i]]-1] = arr[i]
        c[arr[i]] -= 1
        
    return sorted_arr
        
arr = list(w_dic.values())
# print(counting_sorted(arr, len(arr)+1))
length_lst = counting_sorted(arr, 50)
r_lst=[]
for i in set(length_lst):
    for key, value in w_dic.items():
        if value == i: 
            # print(key)
            r_lst.append(key)
print(r_lst)





def sol(arr, i):
    if 


def solution2(a, b, i): # 알파벳 하나하나씩 비교하여 정렬 하는 함수 아스키를 이용!
	if i == len(a):
		return a, b
	if ord(a[i]) > ord(b[i]): # 아스키값 비교
		return b, a
	return solution2(a, b, i + 1) # a, b 의 값이 계속 같을 경우 인덱스를 증가시켜 다시 
            
