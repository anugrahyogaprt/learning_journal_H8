from re import L
import numpy as np
from numpy.linalg import inv, det
#Number 1
tensor_a = np.array([[[23, 50], [7, 12]], [[57, 67], [99, 43]],
                [[75, 21], [57, 12]], [[87, 26], [18, 84]]])
print(tensor_a)

print('++'*20)
#Number 2
mat_a = np.array([[23, 50, 19], [7, 12, 109],[57, 67, 98]])
mat_b = np.array([17, 22, 19])
print(mat_a * mat_b)

print('++'*20)
print(mat_a.T)

print(det(mat_a))
print(inv(mat_a))