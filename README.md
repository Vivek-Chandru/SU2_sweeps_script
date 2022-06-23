# Folder structure and configuration file generator for aerodynamic sweeps in SU2

Given a list of mach , AOA , side-slip angles and a cofiguration file template, the code generates a folder structure and creates a configuration file for each case within the respective folder. The script also generates a shell script to run the job files on HPC (here for slurm workload manager)

Here is an example for RANS simulations
>**Note:** for the code to be fully functional, a mesh file and its location are to also be specified. The bash script must be completed with details of number of nodes, tasks per node etc.. like given in the example.job file

## Code Functionality:

**Folder_rans.py:**
Takes the path , list of mach, AOA and side-slip angle values to create the folders. It also calls the **rans_config.py** script to create configuration files.

**rans_config.py:** Takes a template configuration file and modifies the required fields suitable for each case and saves in the specifed paths   

> More details of how to edit and modify the scripts for different use cases are given in the read_me.txt file





