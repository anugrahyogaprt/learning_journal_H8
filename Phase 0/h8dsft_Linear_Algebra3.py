import numpy as np

A = np.array([[1, -1], [6, 4]])
vec_e = np.array([1, 3])

# Ax = λx
# λ = Ax / x
value_test = A@vec_e / vec_e
print(value_test

#it will print -2, 6. and not the same number, so its not eigen value)