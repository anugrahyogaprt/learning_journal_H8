'''
Carilahturunandarifungsi
y = x^2 +2x +1
y = 4x^3 + 3x^2 + 2x -1
'''

import sympy as sy

x = sy.Symbol('x', real=True)
y1 = x**2 + 2*x + 1
y2 = 4*(x**3) + 3*(x**2) + 2*x - 1

print(y1.diff(x))
print(y2.diff(x))