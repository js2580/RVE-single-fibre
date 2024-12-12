from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup

#abaqus cae -noGUI Single_fibre_RVE.py


# RVE dimensions
fibre_diametre = 0.007 #mm #(7 micron)
matrix_dimensions = 0.008 #mm
extrude_depth = 0.008 #mm

# Fibre properties
Ef11 = 231E3 #MPa
Ef22 = 13E3  #MPa
Ef33 = Ef22
vf12 = 0.3
vf13 = 0.3
vf23 = 0.46
Gf12 = 11.3E3 #MPa
Gf13 = Gf12   #MPa
Gf23 = 4.45E3 #MPa
alphaf11 = 0.1E-6 #/C
alphaf22 = 22E-6 #/C
alphaf33 = alphaf22 #/C

# Matrix properties
Em = 5070 #MPa
vm = 0.35
alpham = 48.5E-6

# Mesh size 
mesh_size = 0.0002

inp_folder = 'inp/'
inp_file = 'RVE_single_fibre' + '.inp'




########### CREATE FIBRE #################

s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(fibre_diametre/2, 0))
p = mdb.models['Model-1'].Part(name='Fibre', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Fibre']
p.BaseSolidExtrude(sketch=s, depth=extrude_depth)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Fibre']
del mdb.models['Model-1'].sketches['__profile__']

########### CREATE MATRIX #################

s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.rectangle(point1=(-matrix_dimensions/2,matrix_dimensions/2), point2=(matrix_dimensions/2,-matrix_dimensions/2))
p = mdb.models['Model-1'].Part(name='Matrix', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Matrix']
p.BaseSolidExtrude(sketch=s, depth=extrude_depth)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Matrix']
del mdb.models['Model-1'].sketches['__profile__']


a = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Fibre']
a.Instance(name='Fibre-1', part=p, dependent=ON)
p = mdb.models['Model-1'].parts['Matrix']
a.Instance(name='Matrix-1', part=p, dependent=ON)

a = mdb.models['Model-1'].rootAssembly
a.InstanceFromBooleanMerge(name='Union_part', instances=(a.instances['Fibre-1'], 
    a.instances['Matrix-1'], ), keepIntersections=ON, originalInstances=DELETE, 
    domain=GEOMETRY)
#p = mdb.models['Model-1'].parts['Union_part']

###################### Material properties ##########################
################ ~~~~~~ Fibre ~~~~~~~~~ ##########################
# mdb.models['Model-1'].Material(name='Fibre')
# mdb.models['Model-1'].materials['Fibre'].Elastic(table=((379.3E3, 0.1), ))

mdb.models['Model-1'].Material(name='Fibre')
mdb.models['Model-1'].materials['Fibre'].Elastic(type=ENGINEERING_CONSTANTS, 
    table=((Ef11, Ef22, Ef33, vf12, vf13, vf23, Gf12, Gf13, Gf23), ))
mdb.models['Model-1'].materials['Fibre'].Expansion(type=ORTHOTROPIC, 
    table=((alphaf11, alphaf22, alphaf33), ))

################ ~~~~~~ Matrix ~~~~~~~~~ ##########################
mdb.models['Model-1'].Material(name='Matrix')
mdb.models['Model-1'].materials['Matrix'].Elastic(table=((Em, vm), ))
mdb.models['Model-1'].materials['Matrix'].Expansion(table=((alpham, ), ))
mdb.models['Model-1'].materials['Matrix'].ConcreteDamagedPlasticity(table=((
    29.0, 0.1, 1.29, 1.0, 0.0001), ))
mdb.models['Model-1'].materials['Matrix'].concreteDamagedPlasticity.ConcreteCompressionHardening(
    table=((176.0, 0.0), (176.0, 0.32), (17.6, 0.64), (1.76, 3.2)))
mdb.models['Model-1'].materials['Matrix'].concreteDamagedPlasticity.ConcreteTensionStiffening(
    table=((121.0, 0.0), (1.21, 0.001652893)))
mdb.models['Model-1'].materials['Matrix'].concreteDamagedPlasticity.ConcreteCompressionDamage(
    table=((0.0, 0.0), (0.0, 0.32), (0.8, 0.64), (0.9, 3.2)))

################ ~~~~~~ Cohesive ~~~~~~~~~ ##########################
mdb.models['Model-1'].Material(name='Cohesive')
mdb.models['Model-1'].materials['Cohesive'].Elastic(type=TRACTION, table=((
    7612.0, 1370.0, 1370.0), ))
mdb.models['Model-1'].materials['Cohesive'].QuadsDamageInitiation(table=((42.0, 
    63.0, 63.0), ))
mdb.models['Model-1'].materials['Cohesive'].quadsDamageInitiation.DamageEvolution(
    type=ENERGY, mixedModeBehavior=BK, power=1.45, table=((0.002, 0.03, 0.03), 
    ))
mdb.models['Model-1'].materials['Cohesive'].quadsDamageInitiation.DamageStabilizationCohesive(
    cohesiveCoeff=0.0001)

###################### Create Section ##########################
mdb.models['Model-1'].HomogeneousSolidSection(name='Fibre section', 
    material='Fibre', thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(name='Matrix section', 
    material='Matrix', thickness=None)
p = mdb.models['Model-1'].parts['Union_part']

###################### Create Sets ##########################
p = mdb.models['Model-1'].parts['Union_part']
c = p.cells
cells = c.findAt(((0,0,0), ))
p.Set(cells=cells, name='Fibre cell')

p = mdb.models['Model-1'].parts['Union_part']
c = p.cells
cells = c.findAt(((matrix_dimensions/2,matrix_dimensions/2,0), ))
p.Set(cells=cells, name='Matrix cell')

###################### Assign Section ##########################

p = mdb.models['Model-1'].parts['Union_part']
region = p.sets['Fibre cell']
p = mdb.models['Model-1'].parts['Union_part']
p.SectionAssignment(region=region, sectionName='Fibre section', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)

p = mdb.models['Model-1'].parts['Union_part']
region = p.sets['Matrix cell']
p = mdb.models['Model-1'].parts['Union_part']
p.SectionAssignment(region=region, sectionName='Matrix section', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)  


###################### Assign Material orientation ##########################

p = mdb.models['Model-1'].parts['Union_part']
region = p.sets['Fibre cell']
mdb.models['Model-1'].parts['Union_part'].MaterialOrientation(region=region, 
    orientationType=DISCRETE, axis=AXIS_3, normalAxisDefinition=VECTOR, 
    normalAxisVector=(0.0, 1.0, 0.0), flipNormalDirection=False, 
    normalAxisDirection=AXIS_3, primaryAxisDefinition=VECTOR, 
    primaryAxisVector=(0.0, 0.0, 1.0), primaryAxisDirection=AXIS_1, 
    flipPrimaryDirection=False, additionalRotationType=ROTATION_NONE, 
    angle=0.0, additionalRotationField='', stackDirection=STACK_3)

p = mdb.models['Model-1'].parts['Union_part']
region = p.sets['Matrix cell']
mdb.models['Model-1'].parts['Union_part'].MaterialOrientation(region=region, 
    orientationType=DISCRETE, axis=AXIS_3, normalAxisDefinition=VECTOR, 
    normalAxisVector=(0.0, 1.0, 0.0), flipNormalDirection=False, 
    normalAxisDirection=AXIS_3, primaryAxisDefinition=VECTOR, 
    primaryAxisVector=(0.0, 0.0, 1.0), primaryAxisDirection=AXIS_1, 
    flipPrimaryDirection=False, additionalRotationType=ROTATION_NONE, 
    angle=0.0, additionalRotationField='', stackDirection=STACK_3)

###################### Assign Mesh ##########################

######## FIBRE 


p = mdb.models['Model-1'].parts['Union_part']
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, 
    secondOrderAccuracy=OFF, distortionControl=DEFAULT)
elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
p = mdb.models['Model-1'].parts['Union_part']
region1 = p.sets['Fibre cell']
p.setElementType(regions=region, elemTypes=(elemType1, elemType2, 
    elemType3))

p = mdb.models['Model-1'].parts['Union_part']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
pickedRegions =(cells, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
    elemType3))

p = mdb.models['Model-1'].parts['Union_part']
c = p.cells
pickedRegions = c.getSequenceFromMask(mask=('[#1 ]', ), )
p.setMeshControls(regions=pickedRegions, elemShape=WEDGE)
#p.setMeshControls(regions=pickedRegions, algorithm=MEDIAL_AXIS)

######## MATRIX 

p = mdb.models['Model-1'].parts['Union_part']
elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, 
    secondOrderAccuracy=OFF, distortionControl=DEFAULT)
elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
p = mdb.models['Model-1'].parts['Union_part']
region = p.sets['Matrix cell']
p.setElementType(regions=region, elemTypes=(elemType1, elemType2, 
    elemType3))

p = mdb.models['Model-1'].parts['Union_part']
c = p.cells
pickedRegions = c.getSequenceFromMask(mask=('[#2 ]', ), )
p.setMeshControls(regions=pickedRegions, elemShape=WEDGE)


# p = mdb.models['Model-1'].parts['Union_part']
# c = p.cells
# pickedRegions = c.getSequenceFromMask(mask=('[#2 ]', ), )
# # #p.setMeshControls(regions=pickedRegions, elemShape=WEDGE)
# p.setMeshControls(regions=pickedRegions, algorithm=MEDIAL_AXIS)

p = mdb.models['Model-1'].parts['Union_part']
p.seedPart(size=mesh_size, deviationFactor=0.1, minSizeFactor=0.1)
p.generateMesh()

# ##################### Create surfaces #########################
# p = mdb.models['Model-1'].parts['Union_part']
# s = p.faces
# side1Faces = s.findAt(((fibre_diametre/2,0,extrude_depth/2),),)
# p.Surface(side1Faces=side1Faces, name='Cohesive surface')


# p = mdb.models['Model-1'].parts['Union_part']
# elements = p.surfaces['Cohesive surface'].elements
# face2Elements = elements
# p.Surface(face2Elements=face2Elements, name='Cohesive mesh')

# p = mdb.models['Model-1'].parts['Union_part']
# p.generateMeshByOffset(region=p.surfaces['Cohesive mesh'], meshType=SOLID, 
#     totalThickness=0.0, numLayers=1, shareNodes=True)

# p = mdb.models['Model-1'].parts['Union_part']
# p.generateMesh()

# p = mdb.models['Model-1'].parts['Union_part']
# elements = p.surfaces['Cohesive surface'].elements
# p.Set(elements=elements, name='Cohesive mesh')

# #################### Cohesive section ########################
# mdb.models['Model-1'].CohesiveSection(name='Cohesive section', 
#     material='Cohesive', response=TRACTION_SEPARATION, 
#     initialThicknessType=GEOMETRY, outOfPlaneThickness=None)

# p = mdb.models['Model-1'].parts['Union_part']
# p.SectionAssignment(region=region, sectionName='Cohesive section', offset=0.0, 
#     offsetType=MIDDLE_SURFACE, offsetField='', 
#     thicknessAssignment=FROM_SECTION)


###################### Create Steps ##########################

# Linear
# mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial', 
#     maxNumInc=1000, initialInc=0.1, maxInc=0.1)
# Non-linear
# mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial', 
#     maxNumInc=1000, initialInc=0.1, maxInc=1, nlgeom=ON)

mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial', 
    maxNumInc=1000, stabilizationMagnitude=0.0002, 
    stabilizationMethod=DISSIPATED_ENERGY_FRACTION, 
    continueDampingFactors=False, adaptiveDampingRatio=0.05, initialInc=0.1, 
    minInc=1e-15, maxInc=0.1, nlgeom=ON
    )

mdb.models['Model-1'].steps['Step-1'].control.setValues(allowPropagation=OFF, 
    resetDefaultValues=OFF, timeIncrementation=(20.0, 40.0, 9.0, 16.0, 10.0, 
    4.0, 12.0, 10.0, 6.0, 3.0, 50.0))
###################### Output History ##########################

mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(
    variables=('S', 'PE', 'PEEQ', 'PEMAG', 'LE', 'U', 'RF', 'CF', 'CSTRESS', 
    'CDISP', 'IVOL','ENER'))

###################### Create inp file ##########################

mdb.Job(name='RVE_single_fibre', model='Model-1', description='', 
    type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, 
    memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
    numGPUs=0)


##################### Generate inp file and move to inp folder ###########################
mdb.jobs['RVE_single_fibre'].writeInput(consistencyChecking=OFF)

import os
if not os.path.exists(inp_folder):
    os.makedirs(inp_folder)

import shutil
if not os.path.exists(f'{inp_folder}{inp_file}'):
    shutil.move(inp_file, inp_folder)
else:
    os.remove(f"{inp_folder}{inp_file}")
    shutil.move(inp_file, inp_folder)

###################### PBC Surface Set ##########################
from Find_opposite_nodes import *

p = mdb.models['Model-1'].parts['Union_part']
nodeLabels = tuple(TopS)
n = p.SetFromNodeLabels(name='TopS', nodeLabels = nodeLabels)

p = mdb.models['Model-1'].parts['Union_part']
nodeLabels = tuple(BotS)
n = p.SetFromNodeLabels(name='BotS', nodeLabels = nodeLabels)

p = mdb.models['Model-1'].parts['Union_part']
nodeLabels = tuple(LeftS)
n = p.SetFromNodeLabels(name='LeftS', nodeLabels = nodeLabels)

p = mdb.models['Model-1'].parts['Union_part']
nodeLabels = tuple(RightS)
n = p.SetFromNodeLabels(name='RightS', nodeLabels = nodeLabels)

p = mdb.models['Model-1'].parts['Union_part']
nodeLabels = tuple(BackSet)
n = p.SetFromNodeLabels(name='BackS', nodeLabels = nodeLabels)

p = mdb.models['Model-1'].parts['Union_part']
nodeLabels = tuple(FrontS)
n = p.SetFromNodeLabels(name='FrontS', nodeLabels = nodeLabels)

###################### PBC Edge Set ##########################

p = mdb.models['Model-1'].parts['Union_part']
nodeLabels = tuple(FLEdge)
n = p.SetFromNodeLabels(name='FLEdge', nodeLabels = nodeLabels)

p = mdb.models['Model-1'].parts['Union_part']
nodeLabels = tuple(FREdge)
n = p.SetFromNodeLabels(name='FREdge', nodeLabels = nodeLabels)

p = mdb.models['Model-1'].parts['Union_part']
nodeLabels = tuple(FTEdge)
n = p.SetFromNodeLabels(name='FTEdge', nodeLabels = nodeLabels)

p = mdb.models['Model-1'].parts['Union_part']
nodeLabels = tuple(FBEdge)
n = p.SetFromNodeLabels(name='FBEdge', nodeLabels = nodeLabels)

p = mdb.models['Model-1'].parts['Union_part']
nodeLabels = tuple(BLEdge)
n = p.SetFromNodeLabels(name='BLEdge', nodeLabels = nodeLabels)

p = mdb.models['Model-1'].parts['Union_part']
nodeLabels = tuple(BREdge)
n = p.SetFromNodeLabels(name='BREdge', nodeLabels = nodeLabels)

p = mdb.models['Model-1'].parts['Union_part']
nodeLabels = tuple(BTEdge)
n = p.SetFromNodeLabels(name='BTEdge', nodeLabels = nodeLabels)

p = mdb.models['Model-1'].parts['Union_part']
nodeLabels = tuple(BBEdge)
n = p.SetFromNodeLabels(name='BBEdge', nodeLabels = nodeLabels)

p = mdb.models['Model-1'].parts['Union_part']
nodeLabels = tuple(LTEdge)
n = p.SetFromNodeLabels(name='LTEdge', nodeLabels = nodeLabels)

p = mdb.models['Model-1'].parts['Union_part']
nodeLabels = tuple(LBEdge)
n = p.SetFromNodeLabels(name='LBEdge', nodeLabels = nodeLabels)

p = mdb.models['Model-1'].parts['Union_part']
nodeLabels = tuple(RTEdge)
n = p.SetFromNodeLabels(name='RTEdge', nodeLabels = nodeLabels)

p = mdb.models['Model-1'].parts['Union_part']
nodeLabels = tuple(RBEdge)
n = p.SetFromNodeLabels(name='RBEdge', nodeLabels = nodeLabels)

###################### PBC Corner Set ##########################

p = mdb.models['Model-1'].parts['Union_part']
nodeLabels = tuple(C1)
n = p.SetFromNodeLabels(name='C1', nodeLabels = nodeLabels)

p = mdb.models['Model-1'].parts['Union_part']
nodeLabels = tuple(C2)
n = p.SetFromNodeLabels(name='C2', nodeLabels = nodeLabels)

p = mdb.models['Model-1'].parts['Union_part']
nodeLabels = tuple(C3)
n = p.SetFromNodeLabels(name='C3', nodeLabels = nodeLabels)

p = mdb.models['Model-1'].parts['Union_part']
nodeLabels = tuple(C4)
n = p.SetFromNodeLabels(name='C4', nodeLabels = nodeLabels)

p = mdb.models['Model-1'].parts['Union_part']
nodeLabels = tuple(C5)
n = p.SetFromNodeLabels(name='C5', nodeLabels = nodeLabels)

p = mdb.models['Model-1'].parts['Union_part']
nodeLabels = tuple(C6)
n = p.SetFromNodeLabels(name='C6', nodeLabels = nodeLabels)

p = mdb.models['Model-1'].parts['Union_part']
nodeLabels = tuple(C7)
n = p.SetFromNodeLabels(name='C7', nodeLabels = nodeLabels)

p = mdb.models['Model-1'].parts['Union_part']
nodeLabels = tuple(C8)
n = p.SetFromNodeLabels(name='C8', nodeLabels = nodeLabels)

###################### Create Reference points ##########################

a = mdb.models['Model-1'].rootAssembly
a.ReferencePoint(point=(RP1coord[0][0], RP1coord[0][1], RP1coord[0][2]))
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[7], )
a.Set(referencePoints=refPoints1, name='RP1')

a = mdb.models['Model-1'].rootAssembly
a.ReferencePoint(point=(RP2coord[0][0], RP2coord[0][1], RP2coord[0][2]))
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[9], )
a.Set(referencePoints=refPoints1, name='RP2')

a = mdb.models['Model-1'].rootAssembly
a.ReferencePoint(point=(RP3coord[0][0], RP3coord[0][1], RP3coord[0][2]))
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[11], )
a.Set(referencePoints=refPoints1, name='RP3')

a = mdb.models['Model-1'].rootAssembly
a.ReferencePoint(point=(RP4coord[0][0], RP4coord[0][1], RP4coord[0][2]))
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[13], )
a.Set(referencePoints=refPoints1, name='RP4')

a = mdb.models['Model-1'].rootAssembly
a.ReferencePoint(point=(RP5coord[0][0], RP5coord[0][1], RP5coord[0][2]))
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[15], )
a.Set(referencePoints=refPoints1, name='RP5')

a = mdb.models['Model-1'].rootAssembly
a.ReferencePoint(point=(RP6coord[0][0], RP6coord[0][1], RP6coord[0][2]))
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[17], )
a.Set(referencePoints=refPoints1, name='RP6')


a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Model-1'].rootAssembly
a.regenerate()

# a = mdb.models['Model-1'].rootAssembly
# a.DatumCsysByThreePoints(name='Datum csys-1', coordSysType=CARTESIAN, origin=(
#     0.0, 0.0, 0.0), point1=(0.0, 0.0, 1.0), point2=(1.0, 0.0, 1.0))

###################### Create node Sets ##########################

for i in SurfaceNode:
    a = mdb.models['Model-1'].rootAssembly.SetFromNodeLabels(name='Node' + str(i+1), nodeLabels=(('Union_part-1', (i+1,)),)) 


##################### Generate inp file and move to inp folder ###########################
mdb.jobs['RVE_single_fibre'].writeInput(consistencyChecking=OFF)

import os
if not os.path.exists(inp_folder):
    os.makedirs(inp_folder)

import shutil
if not os.path.exists(f'{inp_folder}{inp_file}'):
    shutil.move(inp_file, inp_folder)
else:
    os.remove(f"{inp_folder}{inp_file}")
    shutil.move(inp_file, inp_folder)



##################### Function Generate new .inp file with PBC and Disp_boundary included ##########################
def generate_input_file(caseNo):
    Inputfile = open(f"{inp_folder}{inp_file}",'r')
    rawdata = Inputfile.read()
    Inputfile.close()
    data = rawdata.split('\n')
    end_assembly_index = data.index('*End Assembly')
    output_field_index = data.index('** OUTPUT REQUESTS')
    #######################################################
    writefile = open(f"{inp_folder}PBC_RVE_single_fibre_" + caseNo + ".inp",'w')
    for i in range (0,len(data)):
        if i == end_assembly_index:
            writefile.write("*INCLUDE, INPUT=PBC_input.txt \n")
            writefile.write(data[i] + "\n")
        elif i == output_field_index:
            writefile.write("*INCLUDE, INPUT=Disp_Boundary_" + caseNo + ".txt \n")
            writefile.write(data[i] + "\n") 
        else:
            writefile.write(data[i] + "\n")
    writefile.close()


###################### Generate new input files with different boundary conditions ##########################
for i in range (1,10):
    generate_input_file("case" + str(i))






