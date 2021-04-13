import numpy as np

#           sigma[0],   sigma[1],   sigma[2],   sigma[3],   sigma[4],   sigma[5]
# global        x   ,     y   ,         z   ,      xy   ,       xz  ,       yz

# NOTE: E1 = E2, G12 = G23 and v13 = v23
stress = []
strain = []
coefficient = []
energy = []
volume = []
def extract_data(name):
    stress = []
    strain = []
    coefficient = []
    energy = []
    volume = []
    Inputfile = open('homogenised_stress_output_' + name + '.txt','r')
    Inputfile.data = Inputfile.read()
    Inputfile.data = Inputfile.data.split('\n')
    for i in range (1,7):  #Line 0 is header
        stress.append(Inputfile.data[i].split('\t')[0])
        strain.append(Inputfile.data[i].split('\t')[1])
        coefficient.append(Inputfile.data[i].split('\t')[2])
        energy.append(Inputfile.data[i].split('\t')[3])
        volume.append(Inputfile.data[i].split('\t')[4])
        #print(sigma)
    Inputfile.close()
    return stress, strain, coefficient, energy, volume


C11 = float(extract_data('case1')[2][0])
C22 = float(extract_data('case2')[2][1])
C33 = float(extract_data('case3')[2][2]) 

# C11 = 160720
# C22 = 160720
# C33 = 230610

C44 = float(extract_data('case4')[2][3])
C55 = float(extract_data('case5')[2][4])
C66 = float(extract_data('case6')[2][5])


def solve_energy_equation(name):
    stress = []
    strain = []
    coefficient = []
    energy = []
    volume = []
    stress, strain, coefficient, energy, volume = (extract_data(name))
    energy = float(energy[0])
    volume = float(volume[0])
#ABAQUS always reports shear strain as engineering strain :::: https://classes.engineering.wustl.edu/2009/spring/mase5513/abaqus/docs/v6.6/books/usb/default.htm?startat=pt01ch01s02aus02.html
#engineering strain = tensorial shear strain (for pure shear deformation only)
    term1 = 0.5 * C11 * float(strain[0])**2
    term4 = 0.5 * C22 * float(strain[1])**2
    term6 = 0.5 * C33 * float(strain[2])**2
    # term7 = 0.5 * C44 * (float(strain[3])/2)**2
    # term8 = 0.5 * C55 * (float(strain[4])/2)**2
    # term9 = 0.5 * C66 * (float(strain[5])/2)**2
    term7 = 0.5 * C44 * float(strain[3])**2
    term8 = 0.5 * C55 * float(strain[4])**2
    term9 = 0.5 * C66 * float(strain[5])**2
    RH = (energy/volume) - (term1 + term4 + term6 + term7 + term8 + term9)
    term2_coeff = float(strain[0]) * float(strain[1])
    term3_coeff = float(strain[0]) * float(strain[2])
    term5_coeff = float(strain[1]) * float(strain[2])
    LH = np.array([term2_coeff, term3_coeff, term5_coeff])

    return RH, LH

RH1, LH1 = solve_energy_equation('case1')
RH2, LH2 = solve_energy_equation('case2')
RH3, LH3 = solve_energy_equation('case3')


RH = np.array([ [RH1], [RH2], [RH3] ])
LH = np.array([ [LH1[0], LH1[1], LH1[2] ], [LH2[0], LH2[1], LH2[2] ], [LH3[0], LH3[1], LH3[2] ] ])
print('C11 =' + str(C11))
print(RH)
print(LH)


inverse_matrix = np.linalg.inv(LH)
solution = np.dot(inverse_matrix,RH)
print(solution)


# print(C12)
# print(C13)
# print(C23)
C12 = float(solution[0])
C13 = float(solution[1])
C23 = float(solution[2])

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
np.set_printoptions(precision=2)        #Set float value to 2 decimal places
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


