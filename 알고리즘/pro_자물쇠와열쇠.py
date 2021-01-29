"""
2021_01_29

2020_kakao
프로그래머스 문제
"""
def degree(key, x): # 회전시키기
    length = len(key)
    new_key = [key[a][:] for a in range(length)]

    for _ in range(x):
        for i in range(length): # 행렬 -> 좌우
            for j in range(length):
                new_key[i][j] = key[abs(j-(length-1))][i]
        key = [new_key[a][:] for a in range(length)]
    return new_key


def solution(key, lock):
    answer = False

    K_len = len(key)
    L_len = len(lock)
    # 패딩해준다.
    padding_lock = [[0 for i in range(L_len+(K_len*2)-2)] for i in range(L_len+(K_len*2)-2)]
    for i in range(L_len):
        for j in range(L_len):
            padding_lock[i+(K_len-1)][j+(K_len-1)] = lock[i][j]
    
    # for i in range(len(padding_lock)):
    #     print(padding_lock[i])


    for i in range(4): # 0, 90, 190, 270
        new_key = degree(key, i)
        # print(i,"번째 key")
        # for u in range(K_len):
        #     print(new_key[u])
        for x in range(K_len+L_len-1): # 가로에 더해줄 값
            for y in range(K_len+L_len-1): # 세로에 더해줄 값
                bin_lock = [padding_lock[a][:] for a in range(len(padding_lock))]
                for m in range(K_len):
                    for n in range(K_len):
                        bin_lock[m+x][n+y] = padding_lock[m+x][n+y] + new_key[m][n]  # 키는 움직이지 않고, padding한 자물쇠만 움직인다. 
                cnt = 0
                for j in range(K_len-1, len(padding_lock)-K_len+1):
                    for k in range(K_len-1, len(padding_lock)-K_len+1):
                        if bin_lock[j][k] == 1:
                            cnt += 1
                # print("")
                # for h in range(len(bin_lock)):
                #     print(bin_lock[h])
                # print(cnt)
                if cnt == (L_len)**2:
                    answer = True
                    return answer
    # print(K_len, len(padding_lock)-K_len+1)

    return answer


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key, lock))