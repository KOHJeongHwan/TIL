"""
2021-01-29
프로그래머스 문제
"""
def solution(s):
    answer = 0
    lenght = len(s)
    new_s_len = []

    for i in range(1, (lenght//2)+2): # i 는 몇칸씩 볼지, +2 한 이유는 길이가 1인것 때문에
        cnt = 1 # 몇번 반복해쓰
        new_s = ""
        for j in range(lenght//i): # j는 시작점. i*j 를 하면 시작 인덱스를 알 수 있음.
            if s[i*j:i*(j+1)] == s[i*(j+1):i*(j+2)]:
                cnt += 1
            else:
                if cnt > 1:
                    new_s = new_s + str(cnt) + s[i*j:i*(j+1)]
                else:
                    new_s = new_s + s[i*j:i*(j+1)]
                cnt = 1
            if j+1 == (lenght//i): # 나눈뒤, 나머지 값들은 그냥 더해준다.
                new_s = new_s + s[i*(j+1):]
        new_s_len.append(len(new_s))

    new_s_len.sort()
    answer = new_s_len[0]
    return answer

s = "aabbaccc"
# s = "abcabcabcabcdededededede"
# s = "xababcdcdababcdcd"
# s = "ababcdcdababcdcd"
# s = "a"

print(solution(s))