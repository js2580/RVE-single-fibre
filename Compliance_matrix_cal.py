import numpy as np

np.set_printoptions(precision=2)        #Set float value to 2 decimal places

coefficient = []
strain = []
def extract_data(name):
    Inputfile = open('homogenised_stress_output_' + name + '.txt','r')
    Inputfile.data = Inputfile.read()
    Inputfile.data = Inputfile.data.split('\n')
    coefficient = []
    strain = []
    for i in range (1,7):  #Line 0 is header
        coefficient.append(Inputfile.data[i].split('\t')[2])
        strain.append(Inputfile.data[i].split('\t')[1])
        #print(sigma)
    Inputfile.close()
    return coefficient, strain

#           sigma[0],   sigma[1],   sigma[2],   sigma[3],   sigma[4],   sigma[5]
# global        x   ,     y   ,         z   ,      xy   ,       xz  ,       yz

# NOTE: E1 = E2, G12 = G23 and v13 = v23


C11 = float(extract_data('case2')[0][0])
C22 = float(extract_data('case3')[0][1])
C33 = float(extract_data('case1')[0][2]) 

C44 = float(extract_data('case4')[0][3])
C55 = float(extract_data('case5')[0][4])
C66 = float(extract_data('case6')[0][5])

C12 = C22 * -float(extract_data('case3')[1][0])/float(extract_data('case3')[1][1])
C13 = C33 * -float(extract_data('case1')[1][0])/float(extract_data('case1')[1][2])
C23 = C33 * -float(extract_data('case1')[1][1])/float(extract_data('case1')[1][2])

print(C12)
print(C13)
print(C23)

# C12 = float(extract_data('case7')[0][4])
# C13 = float(extract_data('case8')[0][5])
# C23 = float(extract_data('case9')[0][3])


#Form Stiffness tensor
C_matrix = np.array([ [C11, C12, C13,   0,   0,     0,],
                      [C12, C22, C23,   0,   0,     0,],
                      [C13, C23, C33,   0,   0,     0,],
                      [  0,   0,   0, C44,   0,     0,],
                      [  0,   0,   0,   0, C55,     0,],
                      [  0,   0,   0,   0,   0,   C66,],    ])

#print(C_matrix)

############### Calculate the inverse of the stiffness tensor ###################
S_matrix = np.linalg.inv(C_matrix)
#print(S_matrix)

############### Calculate the effective properties ###################
E1 = 1/S_matrix[0][0]
E2 = 1/S_matrix[1][1]
E3 = 1/S_matrix[2][2]

v12 = -S_matrix[0][1]/S_matrix[0][0]
v13 = -S_matrix[0][2]/S_matrix[0][0]
v23 = -S_matrix[1][2]/S_matrix[1][1]

G12 = 1/S_matrix[3][3]
G13= 1/S_matrix[4][4]
G23 = 1/S_matrix[5][5]

outputfile = open('Result_effective_properties.txt','w')
############### C matrix ###################
outputfile.write('############### C matrix ###################\n')

outputfile.write(str(C_matrix/10**3) + '\n')

outputfile.write('############### S matrix ###################\n')

outputfile.write(str(S_matrix/10**3) + '\n')

outputfile.write('############### Properties ###################\n')

outputfile.write('E1 = ' + str("{0:.3f}".format(E1)) + '\n')
outputfile.write('E2 = ' + str("{0:.3f}".format(E2)) + '\n')
outputfile.write('E3 = ' + str("{0:.3f}".format(E3)) + '\n')
outputfile.write('v12 = ' + str("{0:.3f}".format(v12)) + '\n')
outputfile.write('v13 = ' + str("{0:.3f}".format(v13)) + '\n')
outputfile.write('v23 = ' + str("{0:.3f}".format(v23)) + '\n')
outputfile.write('G12 = ' + str("{0:.3f}".format(G12)) + '\n')
outputfile.write('G13 = ' + str("{0:.3f}".format(G13)) + '\n')
outputfile.write('G23 = ' + str("{0:.3f}".format(G23)) + '\n')

outputfile.close()


