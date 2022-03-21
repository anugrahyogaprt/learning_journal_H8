'''
Carilah Gradient dari sebuah fungsi berikut:3x+4y=5
'''

import sympy as sy

x, y = sy.symbols('x y')

f = 3*x + 4*y
print(sy.diff(f, x))
print(sy.diff(f, y))