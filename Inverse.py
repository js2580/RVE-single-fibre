import numpy as np
np.set_printoptions(precision=2)        #Set float value to 2 decimal places

S11 = 0.006962
S22 = 0.006962
S33 = 0.004653
S44 = 0.021864
S55 = 0.018437
S66 = 0.018437
S12 = -0.001779
S13 = -0.000906
S23 = -0.000906

#Form Stiffness tensor
S_matrix = np.array([ [S11, S12, S13,   0,   0,     0,],
                      [S12, S22, S23,   0,   0,     0,],
                      [S13, S23, S33,   0,   0,     0,],
                      [  0,   0,   0, S44,   0,     0,],
                      [  0,   0,   0,   0, S55,     0,],
                      [  0,   0,   0,   0,   0,   S66,],    ])

C_matrix = np.linalg.inv(S_matrix)

outputfile = open('Validate results.txt','w')
outputfile.write('############### C matrix ###################\n')
outputfile.write(str(C_matrix) + '\n')
outputfile.write('############### S matrix ###################\n')
outputfile.write(str(S_matrix/10**3) + '\n')

outputfile.write('############### Properties ###################\n')

# NOTE: E1 = E2, G12 = G23 and v13 = v23

outputfile.write('E1 = ' + '143' + '\n')
outputfile.write('E2 = ' + '143' + '\n')
outputfile.write('E3 = ' + '213' + '\n')
outputfile.write('v12 = ' + '0.194'  + '\n')
outputfile.write('v13 = ' + '0.256'  + '\n')
outputfile.write('v23 = ' + '0.256'  + '\n')
outputfile.write('G12 = ' + '53.8'  + '\n')
outputfile.write('G13 = ' + '45.4'  + '\n')
outputfile.write('G23 = ' + '53.8'  + '\n')
