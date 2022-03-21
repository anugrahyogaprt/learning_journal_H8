'''
h8dsft_Linear_Algebra1
1. Buatlahvektordi bawahinidenganPython : 17,22,19
2. Diberikan3 buah vector 3 dimensi: A = 17,22,19, B = 10,20,11, C = 5,12,9 Hitunglah:
*A+B
*B-C
*A dot C
*A x B
*norm A
*Sudut antara vektor A dan B
3. Buatlah plot darivector berikutinikedalambidang2D: u = 2,5, v = 3,1
'''

import numpy as np
import matplotlib.pyplot as plt

#Number 1
a = np.array([17, 22, 19])

#Number 2
b = np.array([10, 20, 11])
c = np.array([5, 12, 9])
print(a+b)
print(b-c)
print(a.dot(c))
print(a*b)
print(np.linalg.norm(a))
angle_ab = np.arccos(a.dot(b)/(np.linalg.norm(a)*np.linalg.norm(b)))
print(f'angle between a and b = {angle_ab} rad')
print(f'angle between a and b = {np.degrees(angle_ab)} deg')

#Number 3
u = np.array([2, 5])
v = np.array([3, 1])

def plot_vector2d(vector2d, origin=[0, 0], **options):
    return plt.arrow(origin[0], origin[1], vector2d[0], vector2d[1],
              head_width=0.2, head_length=0.3, length_includes_head=True,
              **options)

plot_vector2d(u, color="r")
plot_vector2d(v, color="b")
plt.axis([0, 9, 0, 6])
plt.grid()
plt.show()