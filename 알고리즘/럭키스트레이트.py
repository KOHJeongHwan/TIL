"""
2021-01-27
123402
LUCKY
"""
n = input()
mid=int(len(n)/2)
left = n[:mid]
right = n[mid:]
L_cnt = 0
R_cnt = 0
for i in left:
    L_cnt += int(i)
for i in right:
    R_cnt += int(i)
if L_cnt == R_cnt:
    print("LUCKY")
else:
    print("READY")