from odbAccess import *
from abaqusConstants import *
import sys

#Open the output data
#change path according to the file directory
odb = openOdb(path='RVE_single_fibre.odb') 
myAssembly = odb.rootAssembly
elementType = ['C3D8','C3D6']
#Choose loading type 
# 0 for x direction
# 1 for y direction
# 2 for z direction
# 3 for xy direction
# 4 for yz direction
# 5 for xz direction
loadlist = [0,1,2,3,4,5]

step1 = odb.steps.values()[0]
list_macroscopic_stress = []
list_macroscopic_strain = []
currentFrame = step1.frames[-1]
#Looping for each time increment to obtain full meso-scale stress-strain
#Subset region
myregion = myAssembly.elementSets[' ALL ELEMENTS']
#Output the STRESS FIELD
save_macroscopic_stress = 0
save_temp_vol = 0
stressField = currentFrame.fieldOutputs['S']
ivolField = currentFrame.fieldOutputs['IVOL']
field = stressField.getSubset(region = myregion, position = INTEGRATION_POINT)
fieldValues_stress = field.values
field = ivolField.getSubset(region = myregion, position = INTEGRATION_POINT)
fieldValues_ivol = field.values

for loadtype in loadlist:
    counter = 0
    temp_vol = 0
    temp_stress_times_vol = 0
    for v in fieldValues_stress:
        temp_vol = temp_vol + fieldValues_ivol[counter].data
        temp_stress_times_vol = temp_stress_times_vol + v.data[loadtype] * fieldValues_stress[counter].data
        counter = counter + 1
    macroscopic_stress = temp_stress_times_vol/temp_vol
    list_macroscopic_stress.append(macroscopic_stress)

print(list_macroscopic_stress[1])
# output_file = open('homogenised_stress_output.txt','w')
# for i in loadlist:
#     output_file.write('%16.8E \n' % (list_macroscopic_stress[i]))
#output_file.close()




