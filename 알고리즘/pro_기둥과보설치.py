"""
2021-01-31
프로그래머스
카카오 2020 블라인드 문제
"""
from collections import deque

def del_x(answer, x):
    for idx, val in enumerate(answer):
        if val == x:
            if idx == 0:
                answer = answer[1:]
            elif idx == len(answer)-1:
                answer = answer[:len(answer)-2]
            else:
                answer = answer[:idx-1] + answer[idx+1:]
    return answer

def solution(n, bulid_frame):
    answer =[]

    b_queue = deque()
    for i in range(len(bulid_frame)):
        b_queue.append(bulid_frame[i])

    while b_queue:
        x, y, a, b = b_queue.popleft()
        # 작업장을 벗어나면 다음으로 넘어간다.
        if x < 0 or y < 0 or x > n or y > n:
            continue

        if a == 0: # 기둥일때
            if b == 0: # 삭제
                # 위에 보가 없을때
                if [x,y+1,1] not in answer and [x-1,y+1,1] not in answer:
                    answer = del_x(answer, [x,y,0])
                # 보가 있다면
                else:
                    # 바로 옆에 기둥이 있을때
                    if [x-1,y,0] in answer or [x+1,y,0]:
                        pass
                        
            elif b == 1: # 설치
                # 바닥일때( [x,0] 좌표에 해당할 경우)
                if y == 0:
                    answer.append([x,y,0])
                # 해당 위치에 보가 있을때
                elif [x,y,1] in answer or [x-1,y,1] in answer:
                    answer.append([x,y,0])
                # 아래에 기둥이 있을때
                elif [x,y-1,0] in answer:
                    answer.append([x,y,0])
                else:
                    continue
        elif a == 1: # 보일때
            if b == 0: # 삭제
                pass
            elif b == 1: # 설치
                # 설치하고자 하는 위치에 기둥이 있을때
                if [x,y-1,0] in answer or [x+1,y-1,0] in answer:
                    answer.append([x,y,1])
                # 양 옆에 보가 있고, 그를 지탱하는 기둥이 있을때
                elif [x-1,y,1] in answer and [x+1,y,1] in answer:
                    if [x-1,y-1,0] in answer and [x+2,y-1,0] in answer:
                        answer.append([x,y,1])
                else:
                    continue
        
        print("answer: ",answer)
                

    answer.sort()

    return answer

#1
n = 5
bulid_frame = [[1,0,0,1], [1,1,1,1], [2,1,0,1], [2,2,1,1],
                [5,0,0,1], [5,1,0,1], [4,2,1,1], [3,2,1,1]]
# x,y,a,b 
# a : 0 기둥, 1 보
# b : 0 삭제, 1 설치


print(solution(n,bulid_frame))

#result = [[1,0,0], [1,1,1], [2,1,0], [2,2,1], [3,2,1], [4,2,1], [5,0,0], [5,1,0]]


#2
#n = 5
#bulid_frame =	[[0,0,0,1], [2,0,0,1], [4,0,0,1], [0,1,1,1], [1,1,1,1], [2,1,1,1], [3,1,1,1], [2,0,0,0], [1,1,1,0], [2,2,0,1]]