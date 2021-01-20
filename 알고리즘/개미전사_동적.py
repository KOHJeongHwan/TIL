# 4
# 1 3 1 5

x = int(input())
x_lst = list(map(int, input().split()))

cache = [0] * len(x_lst)

cache[0] = x_lst[0]
cache[1] = x_lst[1]
cache[2] = x_lst[2]
max_num = 0
for i in range(2, x):
    cache[i] = cache[i-2] + x_lst[i]

    print('본래', x_lst)
    print('캐시', cache)
    print('')
    max_num = max(cache[i], cache[i-1])

print(max_num)