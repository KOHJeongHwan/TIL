"""
2021-01-25
30분
그리디문제
"""
# 볼링공의 개수, 공의 최대 무게
n, m = map(int, input().split())

balls = list(map(int, input().split()))
balls.sort()

b = ((n-1)*n)/2

cnt = 0 # 같은 공으로 나오는 조합수
same_num = 1

for idx in range(n-1):
    if balls[idx] == balls[idx+1]:
        same_num += 1

        if idx+2 > n-1: # 마지막 케이스를 위한 코드
            cnt += (same_num*(same_num-1))/2
            same_num = 1
    else:
        cnt += (same_num*(same_num-1))/2
        same_num = 1

result = b - cnt
print(int(result))