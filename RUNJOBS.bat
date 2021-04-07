@ECHO OFF
:: just the title of the window:
TITLE Running Abaqus now
:: we need to set the work folder
cd C:\RVE-single-fibre
ECHO This may take a while
:: in the next line we call abaqus, the job and, and (if needed) the user material (UMAT or VUMAT) writing user=whatever.for
abaqus inp=PBC_RVE_single_fibre_case1.inp job=PBC_RVE_single_fibre_case1 interactive ask_delete=NO
abaqus inp=PBC_RVE_single_fibre_case2.inp job=PBC_RVE_single_fibre_case2 interactive ask_delete=NO

:: the interactive order will show us more detail of the running ananalysis