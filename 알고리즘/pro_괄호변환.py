"""
2020-02-08
"""
def solution(p):
    answer = ''
    
    # 빈 문자열 반환
    if len(p) == 0:
        return ""
    u = []
    v = []

    open_cnt = 0
    close_cnt = 0

    for i in range(len(p)):
        if p[i] == "(":
            open_cnt += 1
        else:
            close_cnt += 1
        if open_cnt-close_cnt == 0:
            u = p[:i+1]
            v = p[i+1:]
            break
    print("u", u)
    # 올바른지 먼저 검사
    if u[0] == ')':
        for i in range(1, len(u)-1):
            if u[i] == "(":
                answer += ")"
            else:
                answer += "("

        return "("+solution(v)+")" + answer
    else:
        return u + solution(v)

# p = "(()())()"
p = ")("
# p = "()))((()"
# p = ")()("
# p = "()()()))((()()"
# p = ")()()()("

print(solution(p))