'''
Cari integral
3x^2 - 6x +3 dx
8x^3 -x^2 +5x -1 dx
'''

import sympy as sy

x = sy.Symbol('x', real=True)
f1 = 3*(x**2) - 6*x + 3
f2 = 8*(x**3) - x**2 + 5*x - 1

print(sy.integrate(f1))
print(sy.integrate(f2))