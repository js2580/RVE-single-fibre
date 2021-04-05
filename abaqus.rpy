# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2020 replay file
# Internal Version: 2019_09_13-18.49.31 163176
# Run by js2580 on Mon Apr  5 21:26:43 2021
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=149.865615844727, 
    height=33.4370384216309)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
cliCommand("""from abaqus import *""")
cliCommand("""from abaqusConstants import *""")
cliCommand("""from caeModules import *""")
cliCommand("""from driverUtils import executeOnCaeStartup""")
cliCommand("""fibre_diametre = 0.0062 #mm #(7 micron)""")
cliCommand("""matrix_dimensions = 0.008 #mm""")
cliCommand("""extrude_depth = 0.008 #mm""")
cliCommand("""########### CREATE FIBRE #################""")
cliCommand("""s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)""")
cliCommand("""g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints""")
cliCommand("""s.setPrimaryObject(option=STANDALONE)""")
cliCommand("""s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(fibre_diametre/2, 0))""")
#: mdb.models['Model-1'].sketches['__profile__'].geometry[2]
cliCommand("""p = mdb.models['Model-1'].Part(name='Fibre', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)""")
cliCommand("""p = mdb.models['Model-1'].parts['Fibre']""")
cliCommand("""p.BaseSolidExtrude(sketch=s, depth=extrude_depth)""")
#: mdb.models['Model-1'].parts['Fibre'].features['Solid extrude-1']
cliCommand("""s.unsetPrimaryObject()""")
cliCommand("""p = mdb.models['Model-1'].parts['Fibre']""")
cliCommand("""del mdb.models['Model-1'].sketches['__profile__']""")
cliCommand("""s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)""")
cliCommand("""g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints""")
cliCommand("""s.setPrimaryObject(option=STANDALONE)""")
cliCommand("""s.rectangle(point1=(-matrix_dimensions/2,matrix_dimensions/2), point2=(matrix_dimensions/2,-matrix_dimensions/2))""")
cliCommand("""p = mdb.models['Model-1'].Part(name='Matrix', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)""")
cliCommand("""p = mdb.models['Model-1'].parts['Matrix']""")
cliCommand("""p.BaseSolidExtrude(sketch=s, depth=extrude_depth)""")
#: mdb.models['Model-1'].parts['Matrix'].features['Solid extrude-1']
cliCommand("""s.unsetPrimaryObject()""")
cliCommand("""p = mdb.models['Model-1'].parts['Matrix']""")
cliCommand("""del mdb.models['Model-1'].sketches['__profile__']""")
cliCommand("""a = mdb.models['Model-1'].rootAssembly""")
cliCommand("""p = mdb.models['Model-1'].parts['Fibre']""")
cliCommand("""a.Instance(name='Fibre-1', part=p, dependent=ON)""")
#: mdb.models['Model-1'].rootAssembly.instances['Fibre-1']
cliCommand("""p = mdb.models['Model-1'].parts['Matrix']""")
cliCommand("""a.Instance(name='Matrix-1', part=p, dependent=ON)""")
#: mdb.models['Model-1'].rootAssembly.instances['Matrix-1']
cliCommand("""a = mdb.models['Model-1'].rootAssembly""")
cliCommand("""a.InstanceFromBooleanMerge(name='Union_part', instances=(a.instances['Fibre-1'], 
    a.instances['Matrix-1'], ), keepIntersections=ON, originalInstances=DELETE, 
    domain=GEOMETRY)""")
#: mdb.models['Model-1'].rootAssembly.instances['Union_part-1']
cliCommand("""#p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""###################### Material properties ##########################""")
cliCommand("""################ ~~~~~~ Fibre ~~~~~~~~~ ##########################""")
cliCommand("""mdb.models['Model-1'].Material(name='Fibre')""")
#: mdb.models['Model-1'].materials['Fibre']
cliCommand("""mdb.models['Model-1'].materials['Fibre'].Elastic(table=((379.3*10**3.0, 0.1), ))""")
#: mdb.models['Model-1'].materials['Fibre'].elastic
cliCommand("""# mdb.models['Model-1'].materials['Fibre'].Elastic(type=ENGINEERING_CONSTANTS, """)
cliCommand("""#     table=((231000.0, 13000.0, 13000.0, 0.3, 0.46, 0.46, 11300.0, 4450.0, """)
cliCommand("""#     4450.0), ))""")
cliCommand("""################ ~~~~~~ Fibre ~~~~~~~~~ ##########################""")
cliCommand("""mdb.models['Model-1'].Material(name='Matrix')""")
#: mdb.models['Model-1'].materials['Matrix']
cliCommand("""mdb.models['Model-1'].materials['Matrix'].Elastic(table=((68.3*10**3, 0.3), ))""")
#: mdb.models['Model-1'].materials['Matrix'].elastic
cliCommand("""# mdb.models['Model-1'].materials['Matrix'].ConcreteDamagedPlasticity(table=((""")
cliCommand("""#     29.0, 0.1, 1.29, 1.0, 0.0001), ))""")
cliCommand("""# mdb.models['Model-1'].materials['Matrix'].concreteDamagedPlasticity.ConcreteCompressionHardening(""")
cliCommand("""#     table=((176.0, 0.0), (176.0, 0.32), (17.6, 0.64), (1.76, 3.2)))""")
cliCommand("""# mdb.models['Model-1'].materials['Matrix'].concreteDamagedPlasticity.ConcreteTensionStiffening(""")
cliCommand("""#     table=((121.0, 0.0), (1.21, 0.001652893)))""")
cliCommand("""# mdb.models['Model-1'].materials['Matrix'].concreteDamagedPlasticity.ConcreteCompressionDamage(""")
cliCommand("""#     table=((0.0, 0.0), (0.0, 0.32), (0.8, 0.64), (0.9, 3.2)))""")
cliCommand("""###################### Create Section ##########################""")
cliCommand("""mdb.models['Model-1'].HomogeneousSolidSection(name='Fibre section', 
    material='Fibre', thickness=None)""")
#: mdb.models['Model-1'].sections['Fibre section']
cliCommand("""mdb.models['Model-1'].HomogeneousSolidSection(name='Matrix section', 
    material='Matrix', thickness=None)""")
#: mdb.models['Model-1'].sections['Matrix section']
cliCommand("""p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""###################### Create Sets ##########################""")
cliCommand("""p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""c = p.cells""")
cliCommand("""cells = c.findAt(((0,0,0), ))""")
cliCommand("""p.Set(cells=cells, name='Fibre cell')""")
#: mdb.models['Model-1'].parts['Union_part'].sets['Fibre cell']
cliCommand("""p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""c = p.cells""")
cliCommand("""cells = c.findAt(((matrix_dimensions/2,matrix_dimensions/2,0), ))""")
cliCommand("""p.Set(cells=cells, name='Matrix cell')""")
#: mdb.models['Model-1'].parts['Union_part'].sets['Matrix cell']
cliCommand("""###################### Assign Section ##########################""")
cliCommand("""p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""region = p.sets['Fibre cell']""")
cliCommand("""p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""p.SectionAssignment(region=region, sectionName='Fibre section', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)""")
#: mdb.models['Model-1'].parts['Union_part'].sectionAssignments[0]
cliCommand("""p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""region = p.sets['Matrix cell']""")
cliCommand("""p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""p.SectionAssignment(region=region, sectionName='Matrix section', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)    """)
#: mdb.models['Model-1'].parts['Union_part'].sectionAssignments[1]
cliCommand("""###################### Assign Material orientation ##########################""")
cliCommand("""p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""region = p.sets['Fibre cell']""")
cliCommand("""mdb.models['Model-1'].parts['Union_part'].MaterialOrientation(region=region, 
    orientationType=DISCRETE, axis=AXIS_3, normalAxisDefinition=VECTOR, 
    normalAxisVector=(0.0, 1.0, 0.0), flipNormalDirection=False, 
    normalAxisDirection=AXIS_3, primaryAxisDefinition=VECTOR, 
    primaryAxisVector=(0.0, 0.0, 1.0), primaryAxisDirection=AXIS_1, 
    flipPrimaryDirection=False, additionalRotationType=ROTATION_NONE, 
    angle=0.0, additionalRotationField='', stackDirection=STACK_3)""")
cliCommand("""###################### Assign Mesh ##########################""")
cliCommand("""p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, 
    secondOrderAccuracy=OFF, distortionControl=DEFAULT)""")
cliCommand("""elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)""")
cliCommand("""elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)""")
cliCommand("""p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""region1 = p.sets['Fibre cell']""")
cliCommand("""p.setElementType(regions=region, elemTypes=(elemType1, elemType2, 
    elemType3))""")
cliCommand("""p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""c = p.cells""")
cliCommand("""pickedRegions = c.getSequenceFromMask(mask=('[#1 ]', ), )""")
cliCommand("""p.setMeshControls(regions=pickedRegions, elemShape=WEDGE)""")
cliCommand("""p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, 
    secondOrderAccuracy=OFF, distortionControl=DEFAULT)""")
cliCommand("""elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)""")
cliCommand("""elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)""")
cliCommand("""p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""region = p.sets['Matrix cell']""")
cliCommand("""p.setElementType(regions=region, elemTypes=(elemType1, elemType2, 
    elemType3))""")
cliCommand("""p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""p.seedPart(size=0.0005, deviationFactor=0.1, minSizeFactor=0.1)""")
cliCommand("""p.generateMesh()""")
cliCommand("""###################### Create Steps ##########################""")
cliCommand("""mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial', 
    maxNumInc=1000, stabilizationMagnitude=0.0002, 
    stabilizationMethod=DISSIPATED_ENERGY_FRACTION, 
    continueDampingFactors=False, adaptiveDampingRatio=0.05, initialInc=0.1, 
    minInc=1e-15, maxInc=0.1, nlgeom=ON)""")
#: mdb.models['Model-1'].steps['Step-1']
cliCommand("""###################### Output History ##########################""")
cliCommand("""mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(
    variables=('S', 'PE', 'PEEQ', 'PEMAG', 'LE', 'U', 'RF', 'CF', 'CSTRESS', 
    'CDISP', 'IVOL'))""")
cliCommand("""###################### Create inp file ##########################""")
cliCommand("""mdb.Job(name='RVE_single_fibre', model='Model-1', description='', 
    type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, 
    memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
    numGPUs=0)""")
#: mdb.jobs['RVE_single_fibre']
cliCommand("""###################### Write inp file ##########################""")
cliCommand("""mdb.jobs['RVE_single_fibre'].writeInput(consistencyChecking=OFF)""")
cliCommand("""###################### PBC Surface Set ##########################""")
cliCommand("""from Python-scripts.Find_opposite_nodes import *""")
#*     from Python-scripts.Find_opposite_nodes import *
#*                ^
#* SyntaxError: invalid syntax
cliCommand("""from abaqus import *""")
cliCommand("""from abaqusConstants import *""")
cliCommand("""from caeModules import *""")
cliCommand("""from driverUtils import executeOnCaeStartup""")
cliCommand("""fibre_diametre = 0.0062 #mm #(7 micron)""")
cliCommand("""matrix_dimensions = 0.008 #mm""")
cliCommand("""extrude_depth = 0.008 #mm""")
cliCommand("""########### CREATE FIBRE #################""")
cliCommand("""s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)""")
cliCommand("""g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints""")
cliCommand("""s.setPrimaryObject(option=STANDALONE)""")
cliCommand("""s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(fibre_diametre/2, 0))""")
#: mdb.models['Model-1'].sketches['__profile__'].geometry[2]
cliCommand("""p = mdb.models['Model-1'].Part(name='Fibre', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)""")
cliCommand("""p = mdb.models['Model-1'].parts['Fibre']""")
cliCommand("""p.BaseSolidExtrude(sketch=s, depth=extrude_depth)""")
#: mdb.models['Model-1'].parts['Fibre'].features['Solid extrude-1']
cliCommand("""s.unsetPrimaryObject()""")
cliCommand("""p = mdb.models['Model-1'].parts['Fibre']""")
cliCommand("""del mdb.models['Model-1'].sketches['__profile__']""")
cliCommand("""s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)""")
cliCommand("""g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints""")
cliCommand("""s.setPrimaryObject(option=STANDALONE)""")
cliCommand("""s.rectangle(point1=(-matrix_dimensions/2,matrix_dimensions/2), point2=(matrix_dimensions/2,-matrix_dimensions/2))""")
cliCommand("""p = mdb.models['Model-1'].Part(name='Matrix', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)""")
cliCommand("""p = mdb.models['Model-1'].parts['Matrix']""")
cliCommand("""p.BaseSolidExtrude(sketch=s, depth=extrude_depth)""")
#: mdb.models['Model-1'].parts['Matrix'].features['Solid extrude-1']
cliCommand("""s.unsetPrimaryObject()""")
cliCommand("""p = mdb.models['Model-1'].parts['Matrix']""")
cliCommand("""del mdb.models['Model-1'].sketches['__profile__']""")
cliCommand("""a = mdb.models['Model-1'].rootAssembly""")
cliCommand("""p = mdb.models['Model-1'].parts['Fibre']""")
cliCommand("""a.Instance(name='Fibre-1', part=p, dependent=ON)""")
#: mdb.models['Model-1'].rootAssembly.instances['Fibre-1']
cliCommand("""p = mdb.models['Model-1'].parts['Matrix']""")
cliCommand("""a.Instance(name='Matrix-1', part=p, dependent=ON)""")
#: mdb.models['Model-1'].rootAssembly.instances['Matrix-1']
cliCommand("""a = mdb.models['Model-1'].rootAssembly""")
cliCommand("""a.InstanceFromBooleanMerge(name='Union_part', instances=(a.instances['Fibre-1'], 
    a.instances['Matrix-1'], ), keepIntersections=ON, originalInstances=DELETE, 
    domain=GEOMETRY)""")
#: mdb.models['Model-1'].rootAssembly.instances['Union_part-2']
cliCommand("""#p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""###################### Material properties ##########################""")
cliCommand("""################ ~~~~~~ Fibre ~~~~~~~~~ ##########################""")
cliCommand("""mdb.models['Model-1'].Material(name='Fibre')""")
#: mdb.models['Model-1'].materials['Fibre']
cliCommand("""mdb.models['Model-1'].materials['Fibre'].Elastic(table=((379.3*10**3.0, 0.1), ))""")
#: mdb.models['Model-1'].materials['Fibre'].elastic
cliCommand("""# mdb.models['Model-1'].materials['Fibre'].Elastic(type=ENGINEERING_CONSTANTS, """)
cliCommand("""#     table=((231000.0, 13000.0, 13000.0, 0.3, 0.46, 0.46, 11300.0, 4450.0, """)
cliCommand("""#     4450.0), ))""")
cliCommand("""################ ~~~~~~ Fibre ~~~~~~~~~ ##########################""")
cliCommand("""mdb.models['Model-1'].Material(name='Matrix')""")
#: mdb.models['Model-1'].materials['Matrix']
cliCommand("""mdb.models['Model-1'].materials['Matrix'].Elastic(table=((68.3*10**3, 0.3), ))""")
#: mdb.models['Model-1'].materials['Matrix'].elastic
cliCommand("""# mdb.models['Model-1'].materials['Matrix'].ConcreteDamagedPlasticity(table=((""")
cliCommand("""#     29.0, 0.1, 1.29, 1.0, 0.0001), ))""")
cliCommand("""# mdb.models['Model-1'].materials['Matrix'].concreteDamagedPlasticity.ConcreteCompressionHardening(""")
cliCommand("""#     table=((176.0, 0.0), (176.0, 0.32), (17.6, 0.64), (1.76, 3.2)))""")
cliCommand("""# mdb.models['Model-1'].materials['Matrix'].concreteDamagedPlasticity.ConcreteTensionStiffening(""")
cliCommand("""#     table=((121.0, 0.0), (1.21, 0.001652893)))""")
cliCommand("""# mdb.models['Model-1'].materials['Matrix'].concreteDamagedPlasticity.ConcreteCompressionDamage(""")
cliCommand("""#     table=((0.0, 0.0), (0.0, 0.32), (0.8, 0.64), (0.9, 3.2)))""")
cliCommand("""###################### Create Section ##########################""")
cliCommand("""mdb.models['Model-1'].HomogeneousSolidSection(name='Fibre section', 
    material='Fibre', thickness=None)""")
#: mdb.models['Model-1'].sections['Fibre section']
cliCommand("""mdb.models['Model-1'].HomogeneousSolidSection(name='Matrix section', 
    material='Matrix', thickness=None)""")
#: mdb.models['Model-1'].sections['Matrix section']
cliCommand("""p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""###################### Create Sets ##########################""")
cliCommand("""p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""c = p.cells""")
cliCommand("""cells = c.findAt(((0,0,0), ))""")
cliCommand("""p.Set(cells=cells, name='Fibre cell')""")
#: mdb.models['Model-1'].parts['Union_part'].sets['Fibre cell']
cliCommand("""p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""c = p.cells""")
cliCommand("""cells = c.findAt(((matrix_dimensions/2,matrix_dimensions/2,0), ))""")
cliCommand("""p.Set(cells=cells, name='Matrix cell')""")
#: mdb.models['Model-1'].parts['Union_part'].sets['Matrix cell']
cliCommand("""###################### Assign Section ##########################""")
cliCommand("""p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""region = p.sets['Fibre cell']""")
cliCommand("""p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""p.SectionAssignment(region=region, sectionName='Fibre section', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)""")
#: mdb.models['Model-1'].parts['Union_part'].sectionAssignments[0]
cliCommand("""p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""region = p.sets['Matrix cell']""")
cliCommand("""p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""p.SectionAssignment(region=region, sectionName='Matrix section', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)    """)
#: mdb.models['Model-1'].parts['Union_part'].sectionAssignments[1]
cliCommand("""###################### Assign Material orientation ##########################""")
cliCommand("""p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""region = p.sets['Fibre cell']""")
cliCommand("""mdb.models['Model-1'].parts['Union_part'].MaterialOrientation(region=region, 
    orientationType=DISCRETE, axis=AXIS_3, normalAxisDefinition=VECTOR, 
    normalAxisVector=(0.0, 1.0, 0.0), flipNormalDirection=False, 
    normalAxisDirection=AXIS_3, primaryAxisDefinition=VECTOR, 
    primaryAxisVector=(0.0, 0.0, 1.0), primaryAxisDirection=AXIS_1, 
    flipPrimaryDirection=False, additionalRotationType=ROTATION_NONE, 
    angle=0.0, additionalRotationField='', stackDirection=STACK_3)""")
cliCommand("""###################### Assign Mesh ##########################""")
cliCommand("""p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, 
    secondOrderAccuracy=OFF, distortionControl=DEFAULT)""")
cliCommand("""elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)""")
cliCommand("""elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)""")
cliCommand("""p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""region1 = p.sets['Fibre cell']""")
cliCommand("""p.setElementType(regions=region, elemTypes=(elemType1, elemType2, 
    elemType3))""")
cliCommand("""p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""c = p.cells""")
cliCommand("""pickedRegions = c.getSequenceFromMask(mask=('[#1 ]', ), )""")
cliCommand("""p.setMeshControls(regions=pickedRegions, elemShape=WEDGE)""")
cliCommand("""p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, 
    secondOrderAccuracy=OFF, distortionControl=DEFAULT)""")
cliCommand("""elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)""")
cliCommand("""elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)""")
cliCommand("""p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""region = p.sets['Matrix cell']""")
cliCommand("""p.setElementType(regions=region, elemTypes=(elemType1, elemType2, 
    elemType3))""")
cliCommand("""p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""p.seedPart(size=0.0005, deviationFactor=0.1, minSizeFactor=0.1)""")
cliCommand("""p.generateMesh()""")
cliCommand("""###################### Create Steps ##########################""")
cliCommand("""mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial', 
    maxNumInc=1000, stabilizationMagnitude=0.0002, 
    stabilizationMethod=DISSIPATED_ENERGY_FRACTION, 
    continueDampingFactors=False, adaptiveDampingRatio=0.05, initialInc=0.1, 
    minInc=1e-15, maxInc=0.1, nlgeom=ON)""")
#: mdb.models['Model-1'].steps['Step-1']
cliCommand("""###################### Output History ##########################""")
cliCommand("""mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(
    variables=('S', 'PE', 'PEEQ', 'PEMAG', 'LE', 'U', 'RF', 'CF', 'CSTRESS', 
    'CDISP', 'IVOL'))""")
cliCommand("""###################### Create inp file ##########################""")
cliCommand("""mdb.Job(name='RVE_single_fibre', model='Model-1', description='', 
    type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, 
    memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
    numGPUs=0)""")
#: mdb.jobs['RVE_single_fibre']
cliCommand("""###################### Write inp file ##########################""")
cliCommand("""mdb.jobs['RVE_single_fibre'].writeInput(consistencyChecking=OFF)""")
cliCommand("""###################### PBC Surface Set ##########################""")
cliCommand("""from Python_scripts.Find_opposite_nodes import *""")
#* ImportError: No module named Python_scripts.Find_opposite_nodes
cliCommand("""from abaqus import *""")
cliCommand("""from abaqusConstants import *""")
cliCommand("""from caeModules import *""")
cliCommand("""from driverUtils import executeOnCaeStartup""")
cliCommand("""fibre_diametre = 0.0062 #mm #(7 micron)""")
cliCommand("""matrix_dimensions = 0.008 #mm""")
cliCommand("""extrude_depth = 0.008 #mm""")
cliCommand("""########### CREATE FIBRE #################""")
cliCommand("""s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)""")
cliCommand("""g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints""")
cliCommand("""s.setPrimaryObject(option=STANDALONE)""")
cliCommand("""s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(fibre_diametre/2, 0))""")
#: mdb.models['Model-1'].sketches['__profile__'].geometry[2]
cliCommand("""p = mdb.models['Model-1'].Part(name='Fibre', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)""")
cliCommand("""p = mdb.models['Model-1'].parts['Fibre']""")
cliCommand("""p.BaseSolidExtrude(sketch=s, depth=extrude_depth)""")
#: mdb.models['Model-1'].parts['Fibre'].features['Solid extrude-1']
cliCommand("""s.unsetPrimaryObject()""")
cliCommand("""p = mdb.models['Model-1'].parts['Fibre']""")
cliCommand("""del mdb.models['Model-1'].sketches['__profile__']""")
cliCommand("""s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)""")
cliCommand("""g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints""")
cliCommand("""s.setPrimaryObject(option=STANDALONE)""")
cliCommand("""s.rectangle(point1=(-matrix_dimensions/2,matrix_dimensions/2), point2=(matrix_dimensions/2,-matrix_dimensions/2))""")
cliCommand("""p = mdb.models['Model-1'].Part(name='Matrix', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)""")
cliCommand("""p = mdb.models['Model-1'].parts['Matrix']""")
cliCommand("""p.BaseSolidExtrude(sketch=s, depth=extrude_depth)""")
#: mdb.models['Model-1'].parts['Matrix'].features['Solid extrude-1']
cliCommand("""s.unsetPrimaryObject()""")
cliCommand("""p = mdb.models['Model-1'].parts['Matrix']""")
cliCommand("""del mdb.models['Model-1'].sketches['__profile__']""")
cliCommand("""a = mdb.models['Model-1'].rootAssembly""")
cliCommand("""p = mdb.models['Model-1'].parts['Fibre']""")
cliCommand("""a.Instance(name='Fibre-1', part=p, dependent=ON)""")
#: mdb.models['Model-1'].rootAssembly.instances['Fibre-1']
cliCommand("""p = mdb.models['Model-1'].parts['Matrix']""")
cliCommand("""a.Instance(name='Matrix-1', part=p, dependent=ON)""")
#: mdb.models['Model-1'].rootAssembly.instances['Matrix-1']
cliCommand("""a = mdb.models['Model-1'].rootAssembly""")
cliCommand("""a.InstanceFromBooleanMerge(name='Union_part', instances=(a.instances['Fibre-1'], 
    a.instances['Matrix-1'], ), keepIntersections=ON, originalInstances=DELETE, 
    domain=GEOMETRY)""")
#: mdb.models['Model-1'].rootAssembly.instances['Union_part-3']
cliCommand("""#p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""###################### Material properties ##########################""")
cliCommand("""################ ~~~~~~ Fibre ~~~~~~~~~ ##########################""")
cliCommand("""mdb.models['Model-1'].Material(name='Fibre')""")
#: mdb.models['Model-1'].materials['Fibre']
cliCommand("""mdb.models['Model-1'].materials['Fibre'].Elastic(table=((379.3*10**3.0, 0.1), ))""")
#: mdb.models['Model-1'].materials['Fibre'].elastic
cliCommand("""# mdb.models['Model-1'].materials['Fibre'].Elastic(type=ENGINEERING_CONSTANTS, """)
cliCommand("""#     table=((231000.0, 13000.0, 13000.0, 0.3, 0.46, 0.46, 11300.0, 4450.0, """)
cliCommand("""#     4450.0), ))""")
cliCommand("""################ ~~~~~~ Fibre ~~~~~~~~~ ##########################""")
cliCommand("""mdb.models['Model-1'].Material(name='Matrix')""")
#: mdb.models['Model-1'].materials['Matrix']
cliCommand("""mdb.models['Model-1'].materials['Matrix'].Elastic(table=((68.3*10**3, 0.3), ))""")
#: mdb.models['Model-1'].materials['Matrix'].elastic
cliCommand("""# mdb.models['Model-1'].materials['Matrix'].ConcreteDamagedPlasticity(table=((""")
cliCommand("""#     29.0, 0.1, 1.29, 1.0, 0.0001), ))""")
cliCommand("""# mdb.models['Model-1'].materials['Matrix'].concreteDamagedPlasticity.ConcreteCompressionHardening(""")
cliCommand("""#     table=((176.0, 0.0), (176.0, 0.32), (17.6, 0.64), (1.76, 3.2)))""")
cliCommand("""# mdb.models['Model-1'].materials['Matrix'].concreteDamagedPlasticity.ConcreteTensionStiffening(""")
cliCommand("""#     table=((121.0, 0.0), (1.21, 0.001652893)))""")
cliCommand("""# mdb.models['Model-1'].materials['Matrix'].concreteDamagedPlasticity.ConcreteCompressionDamage(""")
cliCommand("""#     table=((0.0, 0.0), (0.0, 0.32), (0.8, 0.64), (0.9, 3.2)))""")
cliCommand("""###################### Create Section ##########################""")
cliCommand("""mdb.models['Model-1'].HomogeneousSolidSection(name='Fibre section', 
    material='Fibre', thickness=None)""")
#: mdb.models['Model-1'].sections['Fibre section']
cliCommand("""mdb.models['Model-1'].HomogeneousSolidSection(name='Matrix section', 
    material='Matrix', thickness=None)""")
#: mdb.models['Model-1'].sections['Matrix section']
cliCommand("""p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""###################### Create Sets ##########################""")
cliCommand("""p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""c = p.cells""")
cliCommand("""cells = c.findAt(((0,0,0), ))""")
cliCommand("""p.Set(cells=cells, name='Fibre cell')""")
#: mdb.models['Model-1'].parts['Union_part'].sets['Fibre cell']
cliCommand("""p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""c = p.cells""")
cliCommand("""cells = c.findAt(((matrix_dimensions/2,matrix_dimensions/2,0), ))""")
cliCommand("""p.Set(cells=cells, name='Matrix cell')""")
#: mdb.models['Model-1'].parts['Union_part'].sets['Matrix cell']
cliCommand("""###################### Assign Section ##########################""")
cliCommand("""p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""region = p.sets['Fibre cell']""")
cliCommand("""p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""p.SectionAssignment(region=region, sectionName='Fibre section', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)""")
#: mdb.models['Model-1'].parts['Union_part'].sectionAssignments[0]
cliCommand("""p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""region = p.sets['Matrix cell']""")
cliCommand("""p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""p.SectionAssignment(region=region, sectionName='Matrix section', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)    """)
#: mdb.models['Model-1'].parts['Union_part'].sectionAssignments[1]
cliCommand("""###################### Assign Material orientation ##########################""")
cliCommand("""p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""region = p.sets['Fibre cell']""")
cliCommand("""mdb.models['Model-1'].parts['Union_part'].MaterialOrientation(region=region, 
    orientationType=DISCRETE, axis=AXIS_3, normalAxisDefinition=VECTOR, 
    normalAxisVector=(0.0, 1.0, 0.0), flipNormalDirection=False, 
    normalAxisDirection=AXIS_3, primaryAxisDefinition=VECTOR, 
    primaryAxisVector=(0.0, 0.0, 1.0), primaryAxisDirection=AXIS_1, 
    flipPrimaryDirection=False, additionalRotationType=ROTATION_NONE, 
    angle=0.0, additionalRotationField='', stackDirection=STACK_3)""")
cliCommand("""###################### Assign Mesh ##########################""")
cliCommand("""p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, 
    secondOrderAccuracy=OFF, distortionControl=DEFAULT)""")
cliCommand("""elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)""")
cliCommand("""elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)""")
cliCommand("""p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""region1 = p.sets['Fibre cell']""")
cliCommand("""p.setElementType(regions=region, elemTypes=(elemType1, elemType2, 
    elemType3))""")
cliCommand("""p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""c = p.cells""")
cliCommand("""pickedRegions = c.getSequenceFromMask(mask=('[#1 ]', ), )""")
cliCommand("""p.setMeshControls(regions=pickedRegions, elemShape=WEDGE)""")
cliCommand("""p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""elemType1 = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD, 
    secondOrderAccuracy=OFF, distortionControl=DEFAULT)""")
cliCommand("""elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)""")
cliCommand("""elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)""")
cliCommand("""p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""region = p.sets['Matrix cell']""")
cliCommand("""p.setElementType(regions=region, elemTypes=(elemType1, elemType2, 
    elemType3))""")
cliCommand("""p = mdb.models['Model-1'].parts['Union_part']""")
cliCommand("""p.seedPart(size=0.0005, deviationFactor=0.1, minSizeFactor=0.1)""")
cliCommand("""p.generateMesh()""")
cliCommand("""###################### Create Steps ##########################""")
cliCommand("""mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial', 
    maxNumInc=1000, stabilizationMagnitude=0.0002, 
    stabilizationMethod=DISSIPATED_ENERGY_FRACTION, 
    continueDampingFactors=False, adaptiveDampingRatio=0.05, initialInc=0.1, 
    minInc=1e-15, maxInc=0.1, nlgeom=ON)""")
#: mdb.models['Model-1'].steps['Step-1']
cliCommand("""###################### Output History ##########################""")
cliCommand("""mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(
    variables=('S', 'PE', 'PEEQ', 'PEMAG', 'LE', 'U', 'RF', 'CF', 'CSTRESS', 
    'CDISP', 'IVOL'))""")
cliCommand("""###################### Create inp file ##########################""")
cliCommand("""mdb.Job(name='RVE_single_fibre', model='Model-1', description='', 
    type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, 
    memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
    numGPUs=0)""")
#: mdb.jobs['RVE_single_fibre']
cliCommand("""###################### Write inp file ##########################""")
cliCommand("""mdb.jobs['RVE_single_fibre'].writeInput(consistencyChecking=OFF)""")
cliCommand("""###################### PBC Surface Set ##########################""")
cliCommand("""from Python_scripts.Find_opposite_nodes import *""")
#* ImportError: No module named Python_scripts.Find_opposite_nodes
cliCommand("""import sys""")
cliCommand("""print(sys.path)""")
#: ['C:\\SIMULIA\\EstProducts\\2020\\win_b64\\code\\python2.7\\lib', 'C:\\SIMULIA\\EstProducts\\2020\\win_b64\\tools\\SMApy\\python2.7\\lib', 'C:\\SIMULIA\\EstProducts\\2020\\win_b64\\tools\\SMApy\\python2.7\\lib\\lib-tk', 'C:\\SIMULIA\\EstProducts\\2020\\win_b64\\tools\\SMApy\\python2.7\\lib\\site-packages', 'C:\\SIMULIA\\EstProducts\\2020\\win_b64\\tools\\SMApy\\python2.7\\lib\\site-packages\\win32', 'C:\\SIMULIA\\EstProducts\\2020\\win_b64\\tools\\SMApy\\python2.7\\lib\\site-packages\\win32\\lib', 'C:\\SIMULIA\\EstProducts\\2020\\win_b64\\tools\\SMApy\\python2.7\\lib\\site-packages\\Pythonwin', 'C:\\SIMULIA\\EstProducts\\2020\\win_b64\\tools\\SMApy\\python2.7\\DLLs', 'C:\\RVE-single-fibre', 'C:\\SIMULIA\\EstProducts\\2020', 'C:\\SIMULIA\\EstProducts\\2020\\win_b64', 'C:\\SIMULIA\\EstProducts\\2020\\win_b64\\code', 'C:\\SIMULIA\\EstProducts\\2020\\win_b64\\code\\bin', 'C:\\SIMULIA\\EstProducts\\2020\\win_b64\\code\\bin\\SMAExternal', 'C:\\SIMULIA\\EstProducts\\2020\\win_b64\\CAEresources', 'C:\\SIMULIA\\EstProducts\\2020\\win_b64\\SMA', 'C:\\SIMULIA\\EstProducts\\2020\\win_b64\\code\\bin\\python27.zip', 'C:\\SIMULIA\\EstProducts\\2020\\win_b64\\tools\\SMApy\\python2.7', 'C:\\SIMULIA\\EstProducts\\2020\\win_b64\\tools\\SMApy\\python2.7\\lib\\site-packages\\win32', 'C:\\SIMULIA\\EstProducts\\2020\\win_b64\\tools\\SMApy\\python2.7\\lib\\site-packages\\win32\\lib', 'C:\\SIMULIA\\EstProducts\\2020\\win_b64\\tools\\SMApy\\python2.7\\lib\\site-packages\\Pythonwin', 'C:\\SIMULIA\\EstProducts\\2020\\win_b64\\code\\bin', '.']
