(
cd C:\RVE-single-fibre
abaqus job=PBC_RVE_single_fibre_case1 input=PBC_RVE_single_fibre_case1.inp interactive ask_delete=NO 
cd C:\RVE-single-fibre
abaqus job=PBC_RVE_single_fibre_case2 input=PBC_RVE_single_fibre_case2.inp interactive ask_delete=NO
PAUSE
abaqus job=PBC_RVE_single_fibre_case3 input=PBC_RVE_single_fibre_case3.inp interactive ask_delete=NO
abaqus job=PBC_RVE_single_fibre_case4 input=PBC_RVE_single_fibre_case4.inp interactive ask_delete=NO
abaqus job=PBC_RVE_single_fibre_case5 input=PBC_RVE_single_fibre_case5.inp interactive ask_delete=NO
abaqus job=PBC_RVE_single_fibre_case6 input=PBC_RVE_single_fibre_case6.inp interactive ask_delete=NO
)