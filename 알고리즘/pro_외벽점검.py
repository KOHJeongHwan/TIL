"""
2021-02-02
"""
# 외벽의 둘레 n
# 취약 지점의 위치가 담긴 배열 weak
# 각 친구가 1시간 동안 걸을수 있는 거리 dist
# return 점검할 최소 친구 수 
def solution(n, weak, dist):
    answer = 0
    dist.sort(reverse=True)


    weak_point = [[] for _ in range(len(dist))]

    new_weak = weak
    chack_weak = []
    
    for i in range(len(dist)): # 친구마다
        print(i,"놈")
        cnt = 0
        len_weak = 0
        
        for j in range(n): # 둘레를 1m 씩
            print("j: ",j)
            cnt_point = []
                           # 출발점부터 친구가 갈 수 있는 범위까지
            for k in range(dist[i]+1): # 친구가 갈수 있는 최대 범위 안에서
                print("j+k:", j+k)
                if j+k >= n: # 둘레를 넘는다면, 
                    for over_num in range((j+k)%n + 1):
                        print("((j+k)%n + 1): ",(j+k)%n + 1)
                        if over_num in new_weak and over_num not in cnt_point:
                            cnt_point.append(over_num)
                else:
                    if j + k in new_weak and j + k not in cnt_point:
                        cnt_point.append(j + k)
                
            if len(cnt_point) > 0:
                print("cnt_point", cnt_point)
                if cnt < len(cnt_point): # 최대화
                    cnt = len(cnt_point)
                    weak_point[i] = cnt_point
                    if abs(cnt_point[0] - cnt_point[-1]) < (n//2)+1:
                        len_weak = abs(cnt_point[0] - cnt_point[-1])
                    else:
                        len_weak = abs(cnt_point[0]-n) + cnt_point[-1]
                    print(weak_point[i],"로 바뀜")
                elif cnt == len(cnt_point):    
                    if abs(cnt_point[0] - cnt_point[-1] - n) > len_weak:
                        cnt = len(cnt_point)
                        weak_point[i] = cnt_point
                        if abs(cnt_point[0] - cnt_point[-1]) <= n//2:
                            len_weak = abs(cnt_point[0] - cnt_point[-1])
                        else:
                            len_weak = abs(cnt_point[0]-n) + cnt_point[-1]
                        print(weak_point[i],"로 바뀜")
        new_weak = []
        for L in weak:
            if L in weak_point[i] and L not in chack_weak:
                chack_weak.append(L)
            if L not in chack_weak:
                new_weak.append(L)
        answer += 1
        if len(chack_weak) == len(weak):
            return answer
    answer = -1
    print(dist)
    print(weak_point)

    return answer

n = 12
weak = [1,5,6,10]
dist = [1,2,3,4]
result = 2

# n = 12
# weak = [1, 3, 4, 9, 10]
# dist = [3, 5, 7]
# result = 1

print(solution(n, weak, dist))


from itertools import permutations

def book_solution(n, weak, dist):
    lenght = len(weak)
    for i in range(lenght):
        weak.append(weak[i] + n)
    anwser = len(dist) + 1

    for start in range(lenght):
        for frineds in list(permutations(dist, len(dist))):    
            count = 1
            position = weak[start] + frineds[count - 1]
            for index in range(start, start + lenght):
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + frineds[count - 1]
        anwser = min(anwser, count)
    if anwser > len(dist):
        return -1
    return anwser