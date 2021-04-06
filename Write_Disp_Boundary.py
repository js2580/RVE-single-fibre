E1 = True
E2 = True
E3 = True
G1 = True
G2 = True
G3 = True

Disp = 0.008


if E1 == True:
    DispBoundary = open('Disp_Boundary_case1.txt','w')
    DispBoundary.write('** \n** BOUNDARY CONDITIONS \n** \n')
    DispBoundary.write('*Boundary\n')
    DispBoundary.write('RP4, 3, 3, ' + str(Disp) + '\n')
    DOF1 = True
    DOF2 = True
    DOF3 = True
    DispBoundary.close()


if E2 == True:
    DispBoundary = open('Disp_Boundary_case2.txt','w')
    DispBoundary.write('** \n** BOUNDARY CONDITIONS \n** \n')
    DispBoundary.write('*Boundary\n')
    DispBoundary.write('RP6, 1, 1, ' + str(Disp) + '\n')
    DOF1 = True
    DOF2 = True
    DOF3 = True
    DispBoundary.close()


if E3 == True:
    DispBoundary = open('Disp_Boundary_case3.txt','w')
    DispBoundary.write('** \n** BOUNDARY CONDITIONS \n** \n')
    DispBoundary.write('*Boundary\n')
    DispBoundary.write('RP5, 2, 2, ' + str(Disp) + '\n')
    DOF1 = True
    DOF2 = True
    DOF3 = True
    DispBoundary.close()


if G1 == True:  #epsilon_xy
    DispBoundary = open('Disp_Boundary_case4.txt','w')
    DispBoundary.write('** \n** BOUNDARY CONDITIONS \n** \n')
    DispBoundary.write('*Boundary\n')
    DispBoundary.write('RP6, 2, 2, ' + str(Disp) + '\n')
    DispBoundary.write('RP5, 1, 1, ' + str(Disp) + '\n')
    DOF1 = True
    DOF2 = True
    DOF3 = True
    DispBoundary.close()


if G2 == True:  #epsilon_xz
    DispBoundary = open('Disp_Boundary_case5.txt','w')
    DispBoundary.write('** \n** BOUNDARY CONDITIONS \n** \n')
    DispBoundary.write('*Boundary\n')
    DispBoundary.write('RP4, 1, 1, ' + str(Disp) + '\n')
    DispBoundary.write('RP6, 3, 3, ' + str(Disp) + '\n')
    DOF1 = True
    DOF2 = True
    DOF3 = True
    DispBoundary.close()

# else:
#     DispBoundary.write('*Boundary\n')
#     DispBoundary.write('RP3, 3, 3, 0 \n')

if G3 == True:  #epsilon_yz
    DispBoundary = open('Disp_Boundary_case6.txt','w')
    DispBoundary.write('** \n** BOUNDARY CONDITIONS \n** \n')
    DispBoundary.write('*Boundary\n')
    DispBoundary.write('RP4, 2, 2, ' + str(Disp) + '\n')
    DispBoundary.write('RP5, 3, 3, ' + str(Disp) + '\n')
    DOF1 = True
    DOF2 = True
    DOF3 = True
    DispBoundary.close()


# else:
#     DispBoundary.write('*Boundary\n')
#     DispBoundary.write('RP1, 3, 3, 0 \n')  
#Inputfile.write('*INCLUDE, INPUT=Disp_Boundary.txt')
