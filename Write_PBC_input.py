## Write_PBC_input
from Find_opposite_nodes import *
from Write_Disp_Boundary import *


Disp = 0.008         #extrude_dept

writeinput = open('PBC_input.txt','w')

# writeinput.write('*Nset, nset="_T-Datum csys-1", internal\n')
# for i in SurfaceNode:
#     writeinput.write('Node' + str(i+1) + ',\n')
# for i in range(1,7):
#     writeinput.write('RP' + str(i) + ',\n')

# writeinput.write('*Transform, nset="_T-Datum csys-1"\n')
# writeinput.write('0.,           0.,           1.,           1.,           0.,           0.\n')
# writeinput.write('**Constraint\n')
##########################################################

writeinput.write('**TOP - BOT surfaces\n')
var = pairTB
for i in range (0,len(var)):
    for j in range (1,4):
        if j == 1 and DOF1 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('3\n')
            writeinput.write( 'Node' + str(var[i][0]) + ', ' + str(j) + ', 1., ' + 'Node' + str(var[i][1]) + ', ' + str(j) + ', -1., RP5, ' + str(j) + ', -1\n')
        elif j == 2 and DOF2 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('3\n')
            writeinput.write( 'Node' + str(var[i][0]) + ', ' + str(j) + ', 1., ' + 'Node' + str(var[i][1]) + ', ' + str(j) + ', -1., RP5, ' + str(j) + ', -1\n')
        elif j == 3 and DOF3 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('3\n')
            writeinput.write( 'Node' + str(var[i][0]) + ', ' + str(j) + ', 1., ' + 'Node' + str(var[i][1]) + ', ' + str(j) + ', -1., RP5, ' + str(j) + ', -1\n')

writeinput.write('**Front - Back surfaces\n')
var = pairFB
for i in range (0,len(var)):
    for j in range (1,4):
        if j == 1 and DOF1 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('3\n')
            writeinput.write( 'Node' + str(var[i][0]) + ', ' + str(j) + ', 1., ' + 'Node' + str(var[i][1]) + ', ' + str(j) + ', -1., RP4, ' + str(j) + ', -1\n')
        elif j == 2 and DOF2 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('3\n')
            writeinput.write( 'Node' + str(var[i][0]) + ', ' + str(j) + ', 1., ' + 'Node' + str(var[i][1]) + ', ' + str(j) + ', -1., RP4, ' + str(j) + ', -1\n')
        elif j == 3 and DOF3 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('3\n')
            writeinput.write( 'Node' + str(var[i][0]) + ', ' + str(j) + ', 1., ' + 'Node' + str(var[i][1]) + ', ' + str(j) + ', -1., RP4, ' + str(j) + ', -1\n')

writeinput.write('**Right - Left surfaces\n')
var = pairLR
for i in range (0,len(var)):
    for j in range (1,4):
        if j == 1 and DOF1 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('3\n')
            writeinput.write( 'Node' + str(var[i][1]) + ', ' + str(j) + ', 1., ' + 'Node' + str(var[i][0]) + ', ' + str(j) + ', -1., RP6, ' + str(j) + ', -1\n')
        elif j == 2 and DOF2 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('3\n')
            writeinput.write( 'Node' + str(var[i][1]) + ', ' + str(j) + ', 1., ' + 'Node' + str(var[i][0]) + ', ' + str(j) + ', -1., RP6, ' + str(j) + ', -1\n')
        elif j == 3 and DOF3 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('3\n')
            writeinput.write( 'Node' + str(var[i][1]) + ', ' + str(j) + ', 1., ' + 'Node' + str(var[i][0]) + ', ' + str(j) + ', -1., RP6, ' + str(j) + ', -1\n')        
##########################################################
#EdgeSet1 = RBEdge - LBEdge BF - AE            
#EdgeSet2 = LTEdge - LBEdge DH - AE
#EdgeSet3 = RTEdge - LBEdge CG - AE
#EdgeSet4 = FBEdge - BBEdge EF - AB 
#EdgeSet5 = BTEdge - BBEdge DC - AB
#EdgeSet6 = FTEdge - BBEdge HG - AB
#EdgeSet7 = BREdge - BLEdge BC - AD
#EdgeSet8 = FLEdge - BLEdge EH - AD
#EdgeSet9 = FREdge - BLEdge FG - AD

writeinput.write('**RBEdge - LBEdge BF - AE   \n')
var = EdgeSet1
for i in range (0,len(var)):
    for j in range (1,4):
        if j == 1 and DOF1 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('3\n')
            writeinput.write( 'Node' + str(var[i][0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var[i][1]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP6, ' + str(j) + ', -1\n')
        elif j == 2 and DOF2 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('3\n')
            writeinput.write( 'Node' + str(var[i][0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var[i][1]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP6, ' + str(j) + ', -1\n')
        elif j == 3 and DOF3 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('3\n')
            writeinput.write( 'Node' + str(var[i][0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var[i][1]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP6, ' + str(j) + ', -1\n')

writeinput.write('**LTEdge - LBEdge DH - AE\n')
var = EdgeSet2
for i in range (0,len(var)):
    for j in range (1,4):
        if j == 1 and DOF1 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('3\n')
            writeinput.write( 'Node' + str(var[i][0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var[i][1]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP5, ' + str(j) + ', -1\n')
        elif j == 2 and DOF2 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('3\n')
            writeinput.write( 'Node' + str(var[i][0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var[i][1]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP5, ' + str(j) + ', -1\n')
        elif j == 3 and DOF3 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('3\n')
            writeinput.write( 'Node' + str(var[i][0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var[i][1]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP5, ' + str(j) + ', -1\n')

writeinput.write('**RTEdge - LBEdge CG - AE\n')
var = EdgeSet3
for i in range (0,len(var)):
    for j in range (1,4):
        if j == 1 and DOF1 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('4\n')
            writeinput.write( 'Node' + str(var[i][0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var[i][1]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP6, ' + str(j) + ', -1\n')
            writeinput.write( 'RP5, '  + str(j) + ', -1\n')
        elif j == 2 and DOF2 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('4\n')
            writeinput.write( 'Node' + str(var[i][0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var[i][1]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP6, ' + str(j) + ', -1\n')
            writeinput.write( 'RP5, '  + str(j) + ', -1\n')
        elif j == 3 and DOF3 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('4\n')
            writeinput.write( 'Node' + str(var[i][0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var[i][1]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP6, ' + str(j) + ', -1\n')
            writeinput.write( 'RP5, '  + str(j) + ', -1\n')

writeinput.write('**FBEdge - BBEdge EF - AB \n')
var = EdgeSet4
for i in range (0,len(var)):
    for j in range (1,4):
        if j == 1 and DOF1 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('3\n')
            writeinput.write( 'Node' + str(var[i][0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var[i][1]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP4, ' + str(j) + ', -1\n')
        elif j == 2 and DOF2 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('3\n')
            writeinput.write( 'Node' + str(var[i][0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var[i][1]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP4, ' + str(j) + ', -1\n')
        elif j == 3 and DOF3 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('3\n')
            writeinput.write( 'Node' + str(var[i][0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var[i][1]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP4, ' + str(j) + ', -1\n')

writeinput.write('**BTEdge - BBEdge DC - AB\n')
var = EdgeSet5
for i in range (0,len(var)):
    for j in range (1,4):
        if j == 1 and DOF1 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('3\n')
            writeinput.write( 'Node' + str(var[i][0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var[i][1]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP5, ' + str(j) + ', -1\n')
        elif j == 2 and DOF2 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('3\n')
            writeinput.write( 'Node' + str(var[i][0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var[i][1]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP5, ' + str(j) + ', -1\n')
        elif j == 3 and DOF3 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('3\n')
            writeinput.write( 'Node' + str(var[i][0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var[i][1]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP5, ' + str(j) + ', -1\n')

writeinput.write('**FTEdge - BBEdge HG - AB\n')
var = EdgeSet6
for i in range (0,len(var)):
    for j in range (1,4):
        if j == 1 and DOF1 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('4\n')
            writeinput.write( 'Node' + str(var[i][0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var[i][1]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP5, ' + str(j) + ', -1\n')
            writeinput.write( 'RP4, '  + str(j) + ', -1\n')
        elif j == 2 and DOF2 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('4\n')
            writeinput.write( 'Node' + str(var[i][0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var[i][1]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP5, ' + str(j) + ', -1\n')
            writeinput.write( 'RP4, '  + str(j) + ', -1\n')
        elif j == 3 and DOF3 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('4\n')
            writeinput.write( 'Node' + str(var[i][0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var[i][1]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP5, ' + str(j) + ', -1\n')
            writeinput.write( 'RP4, '  + str(j) + ', -1\n')

writeinput.write('**BREdge - BLEdge BC - AD\n')
var = EdgeSet7
for i in range (0,len(var)):
    for j in range (1,4):
        if j == 1 and DOF1 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('3\n')
            writeinput.write( 'Node' + str(var[i][0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var[i][1]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP6, ' + str(j) + ', -1\n')
        elif j == 2 and DOF2 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('3\n')
            writeinput.write( 'Node' + str(var[i][0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var[i][1]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP6, ' + str(j) + ', -1\n')
        elif j == 3 and DOF3 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('3\n')
            writeinput.write( 'Node' + str(var[i][0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var[i][1]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP6, ' + str(j) + ', -1\n')

writeinput.write('**FLEdge - BLEdge EH - AD\n')
var = EdgeSet8
for i in range (0,len(var)):
    for j in range (1,4):
        if j == 1 and DOF1 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('3\n')
            writeinput.write( 'Node' + str(var[i][0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var[i][1]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP4, ' + str(j) + ', -1\n')
        elif j == 2 and DOF2 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('3\n')
            writeinput.write( 'Node' + str(var[i][0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var[i][1]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP4, ' + str(j) + ', -1\n')
        elif j == 3 and DOF3 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('3\n')
            writeinput.write( 'Node' + str(var[i][0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var[i][1]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP4, ' + str(j) + ', -1\n')

writeinput.write('**FREdge - BLEdge FG - AD\n')
var = EdgeSet9
for i in range (0,len(var)):
    for j in range (1,4):
        if j == 1 and DOF1 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('4\n')
            writeinput.write( 'Node' + str(var[i][0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var[i][1]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP6, ' + str(j) + ', -1\n')
            writeinput.write( 'RP4, '  + str(j) + ', -1\n')
        elif j == 2 and DOF2 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('4\n')
            writeinput.write( 'Node' + str(var[i][0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var[i][1]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP6, ' + str(j) + ', -1\n')
            writeinput.write( 'RP4, '  + str(j) + ', -1\n')
        elif j == 3 and DOF3 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('4\n')
            writeinput.write( 'Node' + str(var[i][0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var[i][1]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP6, ' + str(j) + ', -1\n')
            writeinput.write( 'RP4, '  + str(j) + ', -1\n')
#############################################################

writeinput.write('**C7 - C8 \n')
var1 = C7
var2 = C8
for i in range (0,len(var1)):
    for j in range (1,4):
        if j == 1 and DOF1 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('3\n')
            writeinput.write( 'Node' + str(var1[0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var2[0]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP6, ' + str(j) + ', -1.\n')

        elif j == 2 and DOF2 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('3\n')
            writeinput.write( 'Node' + str(var1[0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var2[0]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP6, ' + str(j) + ', -1.\n')

        elif j == 3 and DOF3 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('3\n')
            writeinput.write( 'Node' + str(var1[0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var2[0]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP6, ' + str(j) + ', -1.\n')


writeinput.write('**C4 - C8 \n')
var1 = C4
var2 = C8
for i in range (0,len(var1)):
    for j in range (1,4):
        if j == 1 and DOF1 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('3\n')
            writeinput.write( 'Node' + str(var1[0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var2[0]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP5, ' + str(j) + ', -1.\n')

        elif j == 2 and DOF2 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('3\n')
            writeinput.write( 'Node' + str(var1[0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var2[0]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP5, ' + str(j) + ', -1.\n')

        elif j == 3 and DOF3 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('3\n')
            writeinput.write( 'Node' + str(var1[0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var2[0]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP5, ' + str(j) + ', -1.\n')
  

writeinput.write('**C5 - C8 \n')
var1 = C5
var2 = C8
for i in range (0,len(var1)):
    for j in range (1,4):
        if j == 1 and DOF1 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('3\n')
            writeinput.write( 'Node' + str(var1[0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var2[0]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP4, ' + str(j) + ', -1.\n')

        elif j == 2 and DOF2 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('3\n')
            writeinput.write( 'Node' + str(var1[0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var2[0]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP4, ' + str(j) + ', -1.\n')

        elif j == 3 and DOF3 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('3\n')
            writeinput.write( 'Node' + str(var1[0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var2[0]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP4, ' + str(j) + ', -1.\n')


writeinput.write('**C3 - C8 \n')
var1 = C3
var2 = C8
for i in range (0,len(var1)):
    for j in range (1,4):
        if j == 1 and DOF1 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('4\n')
            writeinput.write( 'Node' + str(var1[0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var2[0]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP6, ' + str(j) + ', -1.\n')
            writeinput.write( 'RP5, '  + str(j) + ', -1.\n')
        elif j == 2 and DOF2 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('4\n')
            writeinput.write( 'Node' + str(var1[0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var2[0]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP6, ' + str(j) + ', -1.\n')
            writeinput.write( 'RP5, '  + str(j) + ', -1.\n')
        elif j == 3 and DOF3 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('4\n')
            writeinput.write( 'Node' + str(var1[0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var2[0]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP6, ' + str(j) + ', -1.\n')
            writeinput.write( 'RP5, '  + str(j) + ', -1.\n')

writeinput.write('**C1 - C8 \n')
var1 = C1
var2 = C8
for i in range (0,len(var1)):
    for j in range (1,4):
        if j == 1 and DOF1 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('4\n')
            writeinput.write( 'Node' + str(var1[0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var2[0]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP5, ' + str(j) + ', -1.\n')
            writeinput.write( 'RP4, '  + str(j) + ', -1.\n')
        elif j == 2 and DOF2 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('4\n')
            writeinput.write( 'Node' + str(var1[0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var2[0]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP5, ' + str(j) + ', -1.\n')
            writeinput.write( 'RP4, '  + str(j) + ', -1.\n')
        elif j == 3 and DOF3 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('4\n')
            writeinput.write( 'Node' + str(var1[0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var2[0]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP5, ' + str(j) + ', -1.\n')
            writeinput.write( 'RP4, '  + str(j) + ', -1.\n')

writeinput.write('**C6 - C8 \n')
var1 = C6
var2 = C8
for i in range (0,len(var1)):
    for j in range (1,4):
        if j == 1 and DOF1 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('4\n')
            writeinput.write( 'Node' + str(var1[0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var2[0]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP6, ' + str(j) + ', -1.\n')
            writeinput.write( 'RP4, '  + str(j) + ', -1.\n')
        elif j == 2 and DOF2 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('4\n')
            writeinput.write( 'Node' + str(var1[0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var2[0]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP6, ' + str(j) + ', -1.\n')
            writeinput.write( 'RP4, '  + str(j) + ', -1.\n')
        elif j == 3 and DOF3 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('4\n')
            writeinput.write( 'Node' + str(var1[0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var2[0]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP6, ' + str(j) + ', -1.\n')
            writeinput.write( 'RP4, '  + str(j) + ', -1.\n')

writeinput.write('**C2 - C8 \n')
var1 = C2
var2 = C8
for i in range (0,len(var1)):
    for j in range (1,4):
        if j == 1 and DOF1 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('5\n')
            writeinput.write( 'Node' + str(var1[0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var2[0]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP6, ' + str(j) + ', -1.\n')
            writeinput.write( 'RP5, '  + str(j) + ', -1.\n')
            writeinput.write( 'RP4, '  + str(j) + ', -1.\n')
        elif j == 2 and DOF2 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('5\n')
            writeinput.write( 'Node' + str(var1[0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var2[0]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP6, ' + str(j) + ', -1.\n')
            writeinput.write( 'RP5, '  + str(j) + ', -1.\n')
            writeinput.write( 'RP4, '  + str(j) + ', -1.\n')
        elif j == 3 and DOF3 == True:
            writeinput.write('*EQUATION\n')
            writeinput.write('5\n')
            writeinput.write( 'Node' + str(var1[0]) + ', ' + str(j) + ', 1.\n')
            writeinput.write( 'Node' + str(var2[0]) + ', ' + str(j) + ', -1.\n')
            writeinput.write( 'RP6, ' + str(j) + ', -1.\n')
            writeinput.write( 'RP5, '  + str(j) + ', -1.\n')
            writeinput.write( 'RP4, '  + str(j) + ', -1.\n')

         
writeinput.close()

#Inputfile = open("RVE_single_fibre.inp",'a')
#Inputfile.write('*INCLUDE, INPUT=PBC_input.txt')

#total_eq = (len(pairTB) + len(pairLR) + len(pairFB) + len(EdgeSet1) + len(EdgeSet2) + len(EdgeSet3) + len(EdgeSet4) + len(EdgeSet5) + len(EdgeSet6) + 4)*3
#print(total_eq)