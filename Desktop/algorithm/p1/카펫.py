import sympy as sp

brown = 8
yellow = 0

import sympy as sp

# 변수 x,y 정의
x = sp.Symbol('x')
y = sp.Symbol('y')

# 방정식을 정의
eq = sp.Eq(x * (0.5*brown + 2 - x), brown + yellow)

# 방정식 푸는 함수 solve를 호출
solution = sp.solve(eq)
sol_list = [int(i) for i in solution]
if len(sol_list) == 1:
    sol_list = sol_list * 2
# 결과를 출력
#print(sorted(sol_list, reverse=True))








import math

a = 1
b = -0.5*brown -2
c = brown + yellow

# 근의 공식을 사용해 x의 값을 구함
x1 = int((-b + math.sqrt(b**2 - 4*a*c)) / (2*a))
x2 = int((-b - math.sqrt(b**2 - 4*a*c)) / (2*a))

print(sorted([x1, x2], reverse=True))