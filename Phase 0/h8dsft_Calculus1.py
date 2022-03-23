'''
Carilahturunandarifungsi
y = x^2 +2x +1
y = 4x^3 + 3x^2 + 2x -1

+ Cari global min dan max
'''

import sympy as sy
from scipy.optimize import minimize_scalar

x = sy.Symbol('x', real=True)

y1 = x**2 + 2*x + 1
y2 = 4*(x**3) + 3*(x**2) + 2*x - 1

def f1(x):
    return x**2 + 2*x + 1

def f2(x):
    return 4*(x**3) + 3*(x**2) + 2*x - 1

print(y1.diff(x))
print(y2.diff(x))

try:
    print(minimize_scalar(f1))
    print(minimize_scalar(f2))
except:
    print('No minimum value')
