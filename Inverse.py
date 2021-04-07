import numpy as np

C11 = 0.006962
C22 = 0.006962
C33 = 0.004653
C44 = 0.021864
C55 = 0.018437
C66 = 0.018437
C12 = -0.001779
C13 = -0.000906
C23 = -0.000906

#Form Stiffness tensor
C_matrix = np.array([ [C11, C12, C13,   0,   0,     0,],
                      [C12, C22, C23,   0,   0,     0,],
                      [C13, C23, C33,   0,   0,     0,],
                      [  0,   0,   0, C44,   0,     0,],
                      [  0,   0,   0,   0, C55,     0,],
                      [  0,   0,   0,   0,   0,   C66,],    ])

S_matrix = np.linalg.inv(C_matrix)

print(S_matrix)