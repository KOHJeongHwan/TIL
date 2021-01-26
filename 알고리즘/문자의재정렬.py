"""
2021-01-27
"""

n = input()
A = []
N = 0
B = ''
for i in range(len(n)):
    if n[i] in '1234567890':
        N += int(n[i])
    else:
        A.append(n[i])
A.sort()
for i in A:
    B += i
print(B+str(N))