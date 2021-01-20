n = int(input())
lst = [input() for _ in range(n)]

def solution(data): # 정렬 정의 1
	return len(data)

sort_lst = sorted(lst, key=solution) # 길이로 정렬
print(sort_lst)

def solution2(a, b, i): # 알파벳 하나하나씩 비교하여 정렬 하는 함수 아스키를 이용!
	if i == len(a):
		return a, b
	if ord(a[i]) > ord(b[i]): # 아스키값 비교
		print("스왑 전 : ", a, b)	
		a, b = b, a
		print("스왑 후 : ", a, b)
		return a, b
	solution2(a, b, i + 1) # a, b 의 값이 계속 같을 경우 인덱스를 증가시켜 다시 

length = len(sort_lst)
for i in range(length - 1):
	for j in range(length - i - 1):
		a = sort_lst[j]
		b = sort_lst[j + 1]
		if (len(a) == len(b) and a[0] == b[0]):
			print(solution2(a, b, 0))
			# print(a, b)
# print(result)