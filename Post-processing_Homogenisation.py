from odbAccess import *
from abaqusConstants import *
import sys

#abaqus python Post-processing_Homogenisation.py

def compute_stiffness(name):
    #Open the output data
    #change path according to the file directory
    odb = openOdb(path='PBC_RVE_single_fibre_case' + name +'.odb') 
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
    list_macroscopic_energy = []

    list_stiffness_matrix = []
    list_energy = []
    currentFrame = step1.frames[1]
    #Looping for each time increment to obtain full meso-scale stress-strain
    #Subset region
    myregion = myAssembly.elementSets[' ALL ELEMENTS']
    #Output the STRESS FIELD
    save_macroscopic_stress = 0
    save_temp_vol = 0
    stressField = currentFrame.fieldOutputs['S']
    strainField = currentFrame.fieldOutputs['LE']
    ivolField = currentFrame.fieldOutputs['IVOL']
    energyField = currentFrame.fieldOutputs['SENER']
    field = stressField.getSubset(region = myregion, position = INTEGRATION_POINT)
    fieldValues_stress = field.values
    field = strainField.getSubset(region = myregion, position = INTEGRATION_POINT)
    fieldValues_strain = field.values
    field = ivolField.getSubset(region = myregion, position = INTEGRATION_POINT)
    fieldValues_ivol = field.values
    field = energyField.getSubset(region = myregion, position = INTEGRATION_POINT)
    fieldValues_energy = field.values
    for loadtype in loadlist:
        counter = 0                     # inegration point number
        temp_vol = 0                    # temporary_volume
        temp_stress_times_vol = 0       # temporary_stress
        temp_strain_times_vol = 0       # temporary_strain
        temp_energy = 0                 # temporary_strain
        for v in range(0,len(fieldValues_stress)):    # v = fieldValues_stress[counter] --> S11,S22,S33,...                    
            temp_vol = temp_vol + fieldValues_ivol[counter].data                                                         # sum of temp_vol   
            temp_stress_times_vol = temp_stress_times_vol + fieldValues_stress[counter].data[loadtype] * fieldValues_ivol[counter].data            # sum of stress per element volume
            temp_strain_times_vol = temp_strain_times_vol + fieldValues_strain[counter].data[loadtype] * fieldValues_ivol[counter].data            # sum of strain per element volume
            temp_energy = temp_energy + fieldValues_energy[counter].data * fieldValues_ivol[counter].data          # sum of energy
            counter = counter + 1
        macroscopic_stress = temp_stress_times_vol/temp_vol       # intergrate stress over the total volume
        macroscopic_strain = temp_strain_times_vol/temp_vol       # intergrate strain over the total volume
        stiffness_matrix = macroscopic_stress/macroscopic_strain  # Compute stiffness tensors
        total_energy = temp_energy                     # Total energy
        list_macroscopic_stress.append(macroscopic_stress)               
        list_macroscopic_strain.append(macroscopic_strain)   
        list_stiffness_matrix.append(stiffness_matrix)  
        list_energy.append(total_energy)  
                                                    
    output_file = open('homogenised_stress_output_case' + name + '.txt','w')
    output_file.write('  Macro-Stress \t     Macro-Strain \t    Stiffness matrix \t    Total Energy \t   Total Volume \n')
    for i in loadlist:
        output_file.write('%16.8E \t' % (list_macroscopic_stress[i]))
        output_file.write('%16.8E \t' % (list_macroscopic_strain[i]))
        output_file.write('%16.8E \t' % (list_stiffness_matrix[i]))
        output_file.write('%16.8E \t' % (list_energy[i]))
        output_file.write('%16.8E \n' % (temp_vol))
    output_file.close()

for case in range(1,10):
    compute_stiffness(str(case))
