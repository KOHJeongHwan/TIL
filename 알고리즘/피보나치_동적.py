def solution(x):
   if x == 1 or x == 2: # 재귀함수의 종료조건
      return 1
   if d[x] != 0: # 이미 계산한적 있는 문제하면 그대로 반환
      return d[x]
   d[x] = fixo(x - 1) + fibo(x - 2) # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
   return d[x]

print(fibo(99))