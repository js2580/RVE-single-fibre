# RVE-single-fibre

Generate_Single_fibre_RVE.py ---> Generate model and .inp file ::: abaqus cae -noGUI Single_fibre_RVE.py

Find_opposite_nodes.py ---> Find pair nodes at the opposite surfaces

Write_PBC_input.py ---> Generate a text file writing linear equations of each pair node

Write_Disp_boundary.py ---> Generate a text file writing a displacement boundary of a reference point
 
Run Job ---> (.bat need to be developed)abaqus job=PBC_RVE_single_fibre_case1 input=PBC_RVE_single_fibre_case1.inp interactive ask_delete=NO

Post-processing_Homogenisation.py ---> Calcualte homogenisation moduli ::: abaqus python Post-processing_Homogenisation.py
