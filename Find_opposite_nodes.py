inp_folder = 'inp/'
Inputfile = open(f"{inp_folder}RVE_single_fibre.inp",'r')
rawdata = Inputfile.read()
Inputfile.close()
data = rawdata.split('\n')

start_node_index = data.index('*Node')+1
end_node_index = data.index('*Element, type=C3D6')-1 #C3D6
#end_node_index = data.index('*Element, type=C3D8')-1 #C3D8
end_assembly_index = data.index('*End Assembly')

nodeNumber = []
nodeX = []
nodeY = []
nodeZ = []
for i in range(start_node_index,end_node_index):
    read_node = data[i].split(',')
    nodeNumber.append(int(read_node[0]))
    nodeX.append(round(float(read_node[1]),8))
    nodeY.append(round(float(read_node[2]),8))
    nodeZ.append(round(float(read_node[3]),8))
    #print(type(int(read_node[0])))

SurfaceNode = []

TopSet = []
BotSet = []
LeftSet = []
RightSet = []
BackSet = []
FrontSet = []

TotalNode = len(nodeNumber)

maxX, minX = max(nodeX), min(nodeX)
maxY, minY = max(nodeY), min(nodeY)
maxZ, minZ = max(nodeZ), min(nodeZ)

for i in range(0,TotalNode):
    if nodeX[i] == maxX or nodeX[i] == minX or nodeY[i] == maxY or nodeY[i] == minY or nodeZ[i] == maxZ or nodeZ[i] == minZ:
        SurfaceNode.append(i)

for i in SurfaceNode:
    if nodeY[i] == maxY:
        TopSet.append(nodeNumber[i])  
    elif nodeY[i] == minY:
        BotSet.append(nodeNumber[i])
    elif nodeX[i] == maxX:
        RightSet.append(nodeNumber[i])
    elif nodeX[i] == minX:
        LeftSet.append(nodeNumber[i])
    elif nodeZ[i] == maxZ:
        FrontSet.append(nodeNumber[i])
    elif nodeZ[i] == minZ:
        BackSet.append(nodeNumber[i])
    else:
        continue

FLedge = []
FRedge = []
FTedge = []
FBedge = []

BLedge = []
BRedge = []
BTedge = []
BBedge = []


LTedge = []
LBedge = []

RTedge = []
RBedge = []


for i in SurfaceNode:
    # Front
    if ( nodeZ[i] == maxZ ) and ( nodeX[i] == minX ):
        FLedge.append(nodeNumber[i])  
    elif ( nodeZ[i] == maxZ ) and ( nodeX[i] == maxX ):
        FRedge.append(nodeNumber[i])
    elif ( nodeZ[i] == maxZ ) and ( nodeY[i] == maxY ):
        FTedge.append(nodeNumber[i])
    elif ( nodeZ[i] == maxZ ) and ( nodeY[i] == minY ):
        FBedge.append(nodeNumber[i])
    # Back 
    elif ( nodeZ[i] == minZ ) and ( nodeX[i] == minX ):
        BLedge.append(nodeNumber[i])  
    elif ( nodeZ[i] == minZ ) and ( nodeX[i] == maxX ):
        BRedge.append(nodeNumber[i])
    elif ( nodeZ[i] == minZ ) and ( nodeY[i] == maxY ):
        BTedge.append(nodeNumber[i])
    elif ( nodeZ[i] == minZ ) and ( nodeY[i] == minY ):
        BBedge.append(nodeNumber[i])
    # Right 
    elif ( nodeX[i] == maxX ) and ( nodeY[i] == maxY ):
        RTedge.append(nodeNumber[i])  
    elif ( nodeX[i] == maxX ) and ( nodeY[i] == minY ):
        RBedge.append(nodeNumber[i])
    # Left
    elif ( nodeX[i] == minX ) and ( nodeY[i] == maxY ):
        LTedge.append(nodeNumber[i])  
    elif ( nodeX[i] == minX ) and ( nodeY[i] == minY ):
        LBedge.append(nodeNumber[i])
    else:
        continue

C1 = [] #left front top
C2 = [] #right front top
C3 = [] #right front bot ...
C4 = []
C5 = []
C6 = []
C7 = []
C8 = []


for i in SurfaceNode:
    # Front 
    if ( nodeX[i] == minX ) and ( nodeY[i] == maxY ) and ( nodeZ[i] == maxZ ):
        C1.append(nodeNumber[i])
    elif ( nodeX[i] == maxX ) and ( nodeY[i] == maxY ) and ( nodeZ[i] == maxZ ):
        C2.append(nodeNumber[i])
    elif ( nodeX[i] == maxX ) and ( nodeY[i] == minY ) and ( nodeZ[i] == maxZ ):
        C6.append(nodeNumber[i])
    elif ( nodeX[i] == minX ) and ( nodeY[i] == minY ) and ( nodeZ[i] == maxZ ):
        C5.append(nodeNumber[i])
    # Back
    elif ( nodeX[i] == minX ) and ( nodeY[i] == maxY ) and ( nodeZ[i] == minZ ):
        C4.append(nodeNumber[i])
    elif ( nodeX[i] == maxX ) and ( nodeY[i] == maxY ) and ( nodeZ[i] == minZ ):
        C3.append(nodeNumber[i])
    elif ( nodeX[i] == maxX ) and ( nodeY[i] == minY ) and ( nodeZ[i] == minZ ):
        C7.append(nodeNumber[i])
    elif ( nodeX[i] == minX ) and ( nodeY[i] == minY ) and ( nodeZ[i] == minZ ):
        C8.append(nodeNumber[i])
    else:
        continue

allCorner = C1 + C2 + C3 + C4 + C5 + C6 + C7 + C8

TopS = ((((set(TopSet) - set(FTedge) ) - set(BTedge) ) - set(RTedge) ) - set(LTedge) ) - set(allCorner)
BotS = ((((set(BotSet) - set(FBedge) ) - set(BBedge) ) - set(RBedge) ) - set(LBedge) ) - set(allCorner)
LeftS = ((((set(LeftSet) - set(LTedge) ) - set(LBedge) ) - set(FLedge) ) - set(BLedge) ) - set(allCorner)
RightS = ((((set(RightSet) - set(RTedge) ) - set(RBedge) ) - set(FRedge) ) - set(BRedge) ) - set(allCorner)
BackS = ((((set(BackSet) - set(BTedge) ) - set(BBedge) ) - set(BLedge) ) - set(BRedge) ) - set(allCorner)
FrontS = ((((set(FrontSet) - set(FTedge) ) - set(FBedge) ) - set(FLedge) ) - set(FRedge) ) - set(allCorner)

TopS = list(TopS)
BotS = list(BotS)
LeftS = list(LeftS)
RightS = list(RightS)
BackS = list(BackS)
FrontS = list(FrontS)



FLEdge = list(set(FLedge) - set(allCorner))
FTEdge = list(set(FTedge) - set(allCorner))
FREdge = list(set(FRedge) - set(allCorner))
FBEdge = list(set(FBedge) - set(allCorner))

BLEdge = list(set(BLedge) - set(allCorner))
BREdge = list(set(BRedge) - set(allCorner))
BTEdge = list(set(BTedge) - set(allCorner))
BBEdge = list(set(BBedge) - set(allCorner))

LTEdge = list(set(LTedge) - set(allCorner))
LBEdge = list(set(LBedge) - set(allCorner))

RTEdge = list(set(RTedge) - set(allCorner))
RBEdge = list(set(RBedge) - set(allCorner))



################# Paired nodes between two opposite surfaces ###############
Mapping_tolerance = 1*10**-6
pairRL = []
pairTB = []
pairFB = []
errorpair = []


# Right to Left along X-axis
for i in range (0,len(RightS)):
    iNode = RightS[i]
    for j in range (0,len(LeftS)):
        jNode = LeftS[j]
        #print(abs( nodeY[iNode-1] - nodeY[jNode-1] ))
        if abs( nodeY[iNode-1] - nodeY[jNode-1] ) <= Mapping_tolerance:
            if abs( nodeZ[iNode-1] - nodeZ[jNode-1] ) <= Mapping_tolerance:
                pairRL.append([iNode, jNode])
                continue

# Top to Bot along Y-axis
for i in range (0,len(TopS)):
    iNode = TopS[i]
    for j in range (0,len(BotS)):
        jNode = BotS[j] 
        if abs( nodeX[iNode-1] - nodeX[jNode-1] ) <= Mapping_tolerance:
            if abs( nodeZ[iNode-1] - nodeZ[jNode-1] ) <= Mapping_tolerance:
                pairTB.append([iNode, jNode])
                continue

# Front to Back along Z-axis
for i in range (0,len(FrontS)):
    iNode = FrontS[i]
    for j in range (0,len(BackS)):
        jNode = BackS[j] 
        if abs( nodeX[iNode-1] - nodeX[jNode-1] ) <= Mapping_tolerance:
            if abs( nodeY[iNode-1] - nodeY[jNode-1] ) <= Mapping_tolerance:
                pairFB.append(list([iNode, jNode]))
                continue

#nodePair = open('Paired node.txt','w')
#nodePair.write("[L, R]\n")
#for i in range (0,max(len(pairLR),len(pairTB),len(pairFB))):
#    nodePair.write(str(pairLR[i]) +  str(pairTB[i])  +   str(pairFB[i]) + "\n")

################# Paired nodes between two opposite edges ###############


EdgeSet1 = []
EdgeSet2 = []
EdgeSet3 = []
EdgeSet4 = []
EdgeSet5 = []
EdgeSet6 = []
EdgeSet7 = []
EdgeSet8 = []
EdgeSet9 = []


#EdgeSet1 = RBEdge - LBEdge BF - AE            
#EdgeSet2 = LTEdge - LBEdge DH - AE
#EdgeSet3 = RTEdge - LBEdge CG - AE
#EdgeSet4 = FBEdge - BBEdge EF - AB 
#EdgeSet5 = BTEdge - BBEdge DC - AB
#EdgeSet6 = FTEdge - BBEdge HG - AB
#EdgeSet7 = BREdge - BLEdge BC - AD
#EdgeSet8 = FLEdge - BLEdge EH - AD
#EdgeSet9 = FREdge - BLEdge FG - AD

#EdgeSet1 = RBEdge - LBEdge BF - AE            
for i in range (0,len(RBEdge)):
    iNode = RBEdge[i]
    for j in range (0,len(LBEdge)):
        jNode = LBEdge[j]
        if abs( nodeZ[iNode-1] - nodeZ[jNode-1] ) <= Mapping_tolerance:
                EdgeSet1.append([iNode, jNode])
                continue

#EdgeSet2 = LTEdge - LBEdge DH - AE
for i in range (0,len(LTEdge)):
    iNode = LTEdge[i]
    for j in range (0,len(LBEdge)):
        jNode = LBEdge[j]
        if abs( nodeZ[iNode-1] - nodeZ[jNode-1] ) <= Mapping_tolerance:
                EdgeSet2.append([iNode, jNode])
                continue

#EdgeSet3 = RTEdge - LBEdge CG - AE
for i in range (0,len(RTEdge)):
    iNode = RTEdge[i]
    for j in range (0,len(LBEdge)):
        jNode = LBEdge[j]
        if abs( nodeZ[iNode-1] - nodeZ[jNode-1] ) <= Mapping_tolerance:
                EdgeSet3.append([iNode, jNode])
                continue

#EdgeSet4 = FBEdge - BBEdge EF - AB 
for i in range (0,len(FBEdge)):
    iNode = FBEdge[i]
    for j in range (0,len(BBEdge)):
        jNode = BBEdge[j]
        if abs( nodeX[iNode-1] - nodeX[jNode-1] ) <= Mapping_tolerance:
                EdgeSet4.append([iNode, jNode])
                continue

#EdgeSet5 = BTEdge - BBEdge DC - AB
for i in range (0,len(BTEdge)):
    iNode = BTEdge[i]
    for j in range (0,len(BBEdge)):
        jNode = BBEdge[j]
        if abs( nodeX[iNode-1] - nodeX[jNode-1] ) <= Mapping_tolerance:
                EdgeSet5.append([iNode, jNode])
                continue

#EdgeSet6 = FTEdge - BBEdge HG - AB
for i in range (0,len(FTEdge)):
    iNode = FTEdge[i]
    for j in range (0,len(BBEdge)):
        jNode = BBEdge[j]
        if abs( nodeX[iNode-1] - nodeX[jNode-1] ) <= Mapping_tolerance:
                EdgeSet6.append([iNode, jNode])
                continue

#EdgeSet7 = BREdge - BLEdge BC - AD
for i in range (0,len(BREdge)):
    iNode = BREdge[i]
    for j in range (0,len(BLEdge)):
        jNode = BLEdge[j]
        if abs( nodeY[iNode-1] - nodeY[jNode-1] ) <= Mapping_tolerance:
                EdgeSet7.append([iNode, jNode])
                continue

#EdgeSet8 = FLEdge - BLEdge EH - AD
for i in range (0,len(FLEdge)):
    iNode = FLEdge[i]
    for j in range (0,len(BLEdge)):
        jNode = BLEdge[j]
        if abs( nodeY[iNode-1] - nodeY[jNode-1] ) <= Mapping_tolerance:
                EdgeSet8.append([iNode, jNode])
                continue

#EdgeSet9 = FREdge - BLEdge FG - AD
for i in range (0,len(FREdge)):
    iNode = FREdge[i]
    for j in range (0,len(BLEdge)):
        jNode = BLEdge[j]
        if abs( nodeY[iNode-1] - nodeY[jNode-1] ) <= Mapping_tolerance:
                EdgeSet9.append([iNode, jNode])
                continue


################# Determine Reference point at centre of each face ###############


RP1coord = []           #Back   -E11
RP1coord.append([0, 0, minZ])
RP2coord = []           #Bot    -E22
RP2coord.append([0, minY, maxZ/2])
RP3coord = []           #Right  -E33
RP3coord.append([minX, 0, maxZ/2])

RP4coord = []           #Front  E11
RP4coord.append([0, 0, maxZ])
RP5coord = []           #Top    E22
RP5coord.append([0, maxY, maxZ/2])
RP6coord = []           #Left   E33
RP6coord.append([maxX, 0, maxZ/2])
