def DP_one(X, a):

    if a * 5 < X:
        a = a *5
    elif a * 3 < X:
        a = a * 3
    elif a * 2 < X:
        a = a * 2
    elif a + 1:
        a += 1
    return a

def sol(x):
    cache = [ 0 for i in range(x+1) ]
    cache[0] = 2
    cnt = 0

    for i in range(1, x+1):
        cache[i] = DP_one(x, cache[i-1]) 
        if cache[i] == x:
            cnt += 1
            # print(cache)
            return cnt
        else:
            cnt += 1
            

num = int(input())
print(sol(num))