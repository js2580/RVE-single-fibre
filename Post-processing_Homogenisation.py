from odbAccess import *
from abaqusConstants import *
import sys

#abaqus python Post-processing_Homogenisation.py

extrude_dept = 0.008

def compute_stiffness(name,extrude_dept):
    E11 = []
    E22 = []
    E33 = []
    G12 = []
    G13 = []
    G23 = []
    v12 = []
    v13 = []
    v21 = []
    v23 = []
    v31 = []
    v32 = []
    #define parameters
    area = extrude_dept**2
    length = extrude_dept
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
    #
    step1 = odb.steps.values()[0]
    list_macroscopic_stress = []
    list_macroscopic_strain = []
    list_macroscopic_energy = []
    disp = []
    force = []
    disp_C1 = [] 
    disp_C2 = [] 
    disp_C3 = [] 
    disp_C4 = [] 
    disp_C5 = [] 
    disp_C6 = [] 
    disp_C7 = [] 
    disp_C8 = []
    #
    list_stiffness_matrix = []
    list_energy = []
    currentFrame = step1.frames[-1]
    #Looping for each time increment to obtain full meso-scale stress-strain
    #Subset region
    myregion = myAssembly.elementSets[' ALL ELEMENTS']
    #Output the STRESS FIELD
    save_macroscopic_stress = 0
    save_temp_vol = 0
    stressField = currentFrame.fieldOutputs['S']
    strainField = currentFrame.fieldOutputs['LE']
    #strainField = currentFrame.fieldOutputs['E']
    #
    ivolField = currentFrame.fieldOutputs['IVOL']
    energyField = currentFrame.fieldOutputs['SENER']
    #
    field = stressField.getSubset(region = myregion, position = INTEGRATION_POINT)
    fieldValues_stress = field.values
    field = strainField.getSubset(region = myregion, position = INTEGRATION_POINT)
    fieldValues_strain = field.values
    field = ivolField.getSubset(region = myregion, position = INTEGRATION_POINT)
    fieldValues_ivol = field.values
    field = energyField.getSubset(region = myregion, position = INTEGRATION_POINT)
    fieldValues_energy = field.values
    #
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
    #
    #
    #   C1 displacement
    myregion = odb.rootAssembly.instances['UNION_PART-1'].nodeSets['C1']
    dispField = currentFrame.fieldOutputs['U']
    field = dispField.getSubset(region = myregion)
    fieldValues_disp = field.values
    disp_C1 = fieldValues_disp[0].data
    #   C2 displacement
    myregion = odb.rootAssembly.instances['UNION_PART-1'].nodeSets['C2']
    dispField = currentFrame.fieldOutputs['U']
    field = dispField.getSubset(region = myregion)
    fieldValues_disp = field.values
    disp_C2 = fieldValues_disp[0].data
    #   C3 displacement
    myregion = odb.rootAssembly.instances['UNION_PART-1'].nodeSets['C3']
    dispField = currentFrame.fieldOutputs['U']
    field = dispField.getSubset(region = myregion)
    fieldValues_disp = field.values
    disp_C3 = fieldValues_disp[0].data
    #   C4 displacement
    myregion = odb.rootAssembly.instances['UNION_PART-1'].nodeSets['C4']
    dispField = currentFrame.fieldOutputs['U']
    field = dispField.getSubset(region = myregion)
    fieldValues_disp = field.values
    disp_C4 = fieldValues_disp[0].data
    #   C5 displacement
    myregion = odb.rootAssembly.instances['UNION_PART-1'].nodeSets['C5']
    dispField = currentFrame.fieldOutputs['U']
    field = dispField.getSubset(region = myregion)
    fieldValues_disp = field.values
    disp_C5 = fieldValues_disp[0].data
    #   C6 displacement
    myregion = odb.rootAssembly.instances['UNION_PART-1'].nodeSets['C6']
    dispField = currentFrame.fieldOutputs['U']
    field = dispField.getSubset(region = myregion)
    fieldValues_disp = field.values
    disp_C6 = fieldValues_disp[0].data
    #   C7 displacement
    myregion = odb.rootAssembly.instances['UNION_PART-1'].nodeSets['C7']
    dispField = currentFrame.fieldOutputs['U']
    field = dispField.getSubset(region = myregion)
    fieldValues_disp = field.values
    disp_C7 = fieldValues_disp[0].data
    #   C8 displacement
    myregion = odb.rootAssembly.instances['UNION_PART-1'].nodeSets['C8']
    dispField = currentFrame.fieldOutputs['U']
    field = dispField.getSubset(region = myregion)
    fieldValues_disp = field.values
    disp_C8 = fieldValues_disp[0].data
    #
    if name == str(1):
        myregion = myAssembly.nodeSets['RP6']
        dispField = currentFrame.fieldOutputs['U']
        forceField = currentFrame.fieldOutputs['RF']
        #
        field = dispField.getSubset(region = myregion)
        fieldValues_disp = field.values
        field = forceField.getSubset(region = myregion)
        fieldValues_force = field.values
        #
        disp = fieldValues_disp[0].data[0]
        force = fieldValues_force[0].data[0]
        #
        E11 = (force/area)/(disp/length)
        v12 = (abs(disp_C2[1]-disp_C6[1])/length) / (abs(disp_C1[0]-disp_C2[0])/length)
        v13 = (abs(disp_C2[2]-disp_C3[2])/length) / (abs(disp_C1[0]-disp_C2[0])/length)
        print('E11 =' + str(E11))
        print('v12 =' + str(v12))
        print('v13 =' + str(v13))
    elif name == str(2):
        myregion = myAssembly.nodeSets['RP5']
        dispField = currentFrame.fieldOutputs['U']
        forceField = currentFrame.fieldOutputs['RF']
        #
        field = dispField.getSubset(region = myregion)
        fieldValues_disp = field.values
        field = forceField.getSubset(region = myregion)
        fieldValues_force = field.values
        #
        disp = fieldValues_disp[0].data[1]
        force = fieldValues_force[0].data[1]
        #
        E22 = (force/area)/(disp/length)
        v21 = (abs(disp_C1[0]-disp_C2[0])/length) / (abs(disp_C2[1]-disp_C6[1])/length)
        v23 = (abs(disp_C2[2]-disp_C3[2])/length) / (abs(disp_C2[1]-disp_C6[1])/length)
        print('E22 =' + str(E22))
        print('v21 =' + str(v21))
        print('v23 =' + str(v23))
    elif name == str(3):
        myregion = myAssembly.nodeSets['RP4']
        dispField = currentFrame.fieldOutputs['U']
        forceField = currentFrame.fieldOutputs['RF']
        #
        field = dispField.getSubset(region = myregion)
        fieldValues_disp = field.values
        field = forceField.getSubset(region = myregion)
        fieldValues_force = field.values
        #
        disp = fieldValues_disp[0].data[2]
        force = fieldValues_force[0].data[2]
        #
        E33 = (force/area)/(disp/length)
        v31 = (abs(disp_C1[0]-disp_C2[0])/length) / (abs(disp_C2[2]-disp_C3[2])/length)
        v32 = (abs(disp_C2[1]-disp_C6[1])/length) / (abs(disp_C2[2]-disp_C3[2])/length)
        print('E33 =' + str(E33))
        print('v31 =' + str(v31))
        print('v32 =' + str(v32))
    elif name == str(4):
        myregion = myAssembly.nodeSets['RP5']
        dispField = currentFrame.fieldOutputs['U']
        forceField = currentFrame.fieldOutputs['RF']
        #
        field = dispField.getSubset(region = myregion)
        fieldValues_disp = field.values
        field = forceField.getSubset(region = myregion)
        fieldValues_force = field.values
        #
        disp = fieldValues_disp[0].data[0]                  
        force = fieldValues_force[0].data[0]
        #
        G12 = (force/area) / (disp/length + disp/length)    #NOTE: THIS ASSUMMED THAT DISPLACEMENT MAGNITUDE IS THE SAME
        print('G12 =' + str(G12))
    elif name == str(5):
        myregion = myAssembly.nodeSets['RP4']
        dispField = currentFrame.fieldOutputs['U']
        forceField = currentFrame.fieldOutputs['RF']
        #
        field = dispField.getSubset(region = myregion)
        fieldValues_disp = field.values
        field = forceField.getSubset(region = myregion)
        fieldValues_force = field.values
        #
        disp = fieldValues_disp[0].data[0]
        force = fieldValues_force[0].data[0]
        #
        G13 = (force/area) / (disp/length + disp/length)    #NOTE: THIS ASSUMMED THAT DISPLACEMENT MAGNITUDE IS THE SAME
        print('G13 =' + str(G13))
    elif name == str(6):
        myregion = myAssembly.nodeSets['RP4']
        dispField = currentFrame.fieldOutputs['U']
        forceField = currentFrame.fieldOutputs['RF']
        #
        field = dispField.getSubset(region = myregion)
        fieldValues_disp = field.values
        field = forceField.getSubset(region = myregion)
        fieldValues_force = field.values
        #
        disp = fieldValues_disp[0].data[1]
        force = fieldValues_force[0].data[1]
        #
        G23 = (force/area) / (disp/length + disp/length)    #NOTE: THIS ASSUMMED THAT DISPLACEMENT MAGNITUDE IS THE SAME
        print('G23 =' + str(G23))
    #
    #
    output_file = open('homogenised_stress_output_case' + name + '.txt','w')
    output_file.write('  Macro-Stress \t     Macro-Strain \t    Stiffness matrix \t    Total Energy \t   Total Volume \n')
    for i in loadlist:
        output_file.write('%16.8E \t' % (list_macroscopic_stress[i]))
        output_file.write('%16.8E \t' % (list_macroscopic_strain[i]))
        output_file.write('%16.8E \t' % (list_stiffness_matrix[i]))
        output_file.write('%16.8E \t' % (list_energy[i]))
        output_file.write('%16.8E \n' % (temp_vol))
    # output_file.write('disp = %16.8E \n' % (disp))
    # output_file.write('force = %16.8E \n' % (force))
    #
    output_file.close()
    return E11, E22, E33, G12, G13, G23, v12, v13, v21, v23, v31, v32

# E11 = []
# E22 = []
# E33 = []
# G12 = []
# G13 = []
# G23 = []
# v12 = []
# v13 = []
# v21 = []
# v23 = []
# v31 = []
# v32 = []
material_output = open('Homogenised material properties output.txt','w')
for case in range(1,10):
    
    E11, E22, E33, G12, G13, G23, v12, v13, v21, v23, v31, v32 = compute_stiffness(str(case),extrude_dept)
    # if E11 is not None:
    #     material_output.write('E11 = %16.8E \n' % (E11))
    # elif E22 is not None:
    #     material_output.write('E22 = %16.8E \n' % (E22))
    # elif E33 is not None:
    #     material_output.write('E33 = %16.8E \n' % (E33))
    # elif G12 is not None:
    #     material_output.write('G12 = %16.8E \n' % (G12))
    # elif G13 is not None:
    #     material_output.write('G13 = %16.8E \n' % (G13))
    # elif G23 is not None:
    #     material_output.write('G23 = %16.8E \n' % (G23))
    # elif v12 is not None:
    #     material_output.write('v12 = %16.8E \n' % (v12))
    # elif E22 is not None:
    #     material_output.write('E22 = %16.8E \n' % (E22))
    # elif v13 is not None:
    #     material_output.write('v13 = %16.8E \n' % (v13))
    # elif v21 is not None:
    #     material_output.write('v21 = %16.8E \n' % (v21))
    # elif v23 is not None:
    #     material_output.write('v23 = %16.8E \n' % (v23))
    # elif v31 is not None:
    #     material_output.write('v31 = %16.8E \n' % (v31))
    # elif v32 is not None:
    #     material_output.write('v32 = %16.8E \n' % (v32))


material_output.close()



