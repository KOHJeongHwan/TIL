"""
2021-01-28
프로그래머스 문제
"""
def solution(m, musicinfos):
    answer = ''
    code_list = []
    for lst in musicinfos:
        start, end, name, m_code = map(str, lst.split(','))
        # print(start)
        # print(end)
        # print(name)
        # print(m_code)
        HH = (int(end[:2]) - int(start[:2]))*60
        mm = int(end[3:]) - int(start[3:])
        play_time = HH + mm  # 총 플레이 타임 계산


        new_m_code = []
        new_m = []

        for NMC in m_code:
            if NMC != '#':
                new_m_code.append(NMC)
            else:
                new_m_code.append(new_m_code.pop()+'#')
        
        for NM in m:
            if NM != '#':
                new_m.append(NM)
            else:
                new_m.append(new_m.pop()+'#')


        all_code = new_m_code*(play_time//len(new_m_code)) + new_m_code[:play_time%len(new_m_code)]
        # all_code = m_code*(play_time//len(m_code)) + m_code[:play_time%len(m_code)] 
        # print(all_code)

        stop_cnt = 0

        for i in range(len(all_code)):
            if all_code[i] == new_m[0]:
                bin = i
                for j in new_m:
                    if bin<len(all_code) and all_code[bin] == j:
                        bin += 1
                        stop_cnt += 1
                    else:
                        break
                bin = 0
                if stop_cnt == len(new_m):
                    break
        
        # print(stop_cnt)
        # print(len(m_code))
        if stop_cnt == len(new_m):
            # print("_____________________________________")
            code_list.append((play_time, name))
            # print(code_list[0][1])
    
    if len(code_list) > 0:
        code_list.sort()
        # print("code_list", code_list[0][1])
        answer = code_list[0][1]
    else:
        answer = "(None)"
    # print("정답: ", answer)
    return answer

# m = "ABCDEFG"
# mu = ['12:00,12:14,HELLO,CDEFGAB', '13:00,13:05,WORLD,ABCDEF']

# m = "CC#BCC#BCC#BCC#B"
# mu = ['03:00,03:30,FOO,CC#B', '04:00,04:08,BAR,CC#BCC#BCC#B']

# m = "A#"
# mu = ['13:00,13:02,HAPPY,B#A#']

# m = "CDEFGAC"
# mu = ['12:00,12:06,HELLO,CDEFGA']

m = 'CCB'
mu = ['03:00,03:10,FOO,CCB#CCB','04:00,04:08,BAR,ABC']

print(solution(m, mu))