n = int(input())

cache = [0]*100

cache[0] = 1

two_num = n // 2

def soon(n, x):
    eve = 1
    one = 1
    two = 1
    
    for i in range(1, n+1):
        eve = eve*i

    for i in range(1, n-x+1):
        one = one*i

    for i in range(1, x+1):
        two = two*i

    return eve//(one*two)
    
if n % 2 == 0:
    for idx in range(1, two_num+1):
        cache[idx] = cache[idx-1] + soon(n, idx)
else:
    for idx in range(1, two_num+1):
        cache[idx] = cache[idx-1] + soon(n, idx)
    
print(cache)