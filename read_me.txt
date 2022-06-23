Read me:

Steps:

1. update mesh path (location + name in configuration template file)

2. Update folder_rans.py script:
- update path variable with name of folder to be created
- update the template name and path variables
- add additional mach numbers as a list in the mach variable and create a for loop to call 'work' function while passing new amch values each time.

3. Update rans_config.py script:
- add required additonal fields or remove fields (for ex. add Mach field for Multiple mach sweeps and replace the default value with the mach variable value)

4. Run the Folder_rans script to create the fodler structure

5. To run on cluster:
- using contents of the bash file from the batch file(.sh file) and create a job file like the example job file for required number of nodes and cores 
