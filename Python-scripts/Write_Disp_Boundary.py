E1 = False
E2 = False
E3 = False
G1 = False
G2 = True
G3 = False

Disp = 0.008

DispBoundary = open('Disp_Boundary.txt','w')
DispBoundary.write('** \n** BOUNDARY CONDITIONS \n** \n')
if E1 == True:
    DispBoundary.write('*Boundary\n')
    DispBoundary.write('RP4, 3, 3, ' + str(Disp) + '\n')
    DOF1 = True
    DOF2 = True
    DOF3 = True


if E2 == True:
    DispBoundary.write('*Boundary\n')
    DispBoundary.write('RP6, 1, 1, ' + str(Disp) + '\n')
    DOF1 = True
    DOF2 = True
    DOF3 = True

if E3 == True:
    DispBoundary.write('RP5, 2, 2, ' + str(Disp) + '\n')
    DOF1 = True
    DOF2 = False
    DOF3 = False

if G1 == True:  #epsilon_xy
    DispBoundary.write('*Boundary\n')
    DispBoundary.write('RP6, 3, 3, ' + str(Disp) + '\n')
    DispBoundary.write('RP4, 1, 1, ' + str(Disp) + '\n')
    DOF1 = True
    DOF2 = True
    DOF3 = True

if G2 == True:  #epsilon_xz
    DispBoundary.write('*Boundary\n')
    DispBoundary.write('RP6, 2, 2, ' + str(Disp) + '\n')
    DispBoundary.write('RP5, 1, 1, ' + str(Disp) + '\n')
    DOF1 = True
    DOF2 = True
    DOF3 = True
# else:
#     DispBoundary.write('*Boundary\n')
#     DispBoundary.write('RP3, 3, 3, 0 \n')

if G3 == True:  #epsilon_yz
    DispBoundary.write('*Boundary\n')
    DispBoundary.write('RP5, 3, 3, ' + str(Disp) + '\n')
    DispBoundary.write('RP4, 2, 2, ' + str(Disp) + '\n')
    DOF1 = True
    DOF2 = True
    DOF3 = True

# else:
#     DispBoundary.write('*Boundary\n')
#     DispBoundary.write('RP1, 3, 3, 0 \n')  
#Inputfile.write('*INCLUDE, INPUT=Disp_Boundary.txt')
