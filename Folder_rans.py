#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 11:17:03 2020

@author: vivek
"""

import os
from rans_config import Rans

def work(mach,path,template_name,template_path,alpha,beta):
                
    #Give your bash file name here used to execute the sweep sequentially
    sh_name = 'rans_sweep_'+str(int(mach*100))+'.sh' # example for M = 0.7 creates - rans_sweep_M70.sh
    sh_path = path + '/' + sh_name
    sh= open(sh_path,"w+")
    
    #creating folder structure for the Mach sweep
    folder_1 = 'M' + str(mach)
    path_1 = path + '/' +folder_1
    os.mkdir(path_1)
    
    sh.write('#!/bin/bash \n\n')
    sh.write('cd ')
    sh.write(folder_1)
    sh.write('\n')

    # creating folders for alpha sweeps within the Mach folder
    for x in alpha:
        path_2 = path_1 + '/' + "alpha_" + str(x)
        os.mkdir(path_2)
        
        sh.write('cd alpha_')
        sh.write(str(x))
        sh.write('\n')
        
        #creating folders for beta sweeps within the alpha folders
        for item in beta:
            path_3 = path_2+'/'+"beta_"+str(item)
            os.mkdir(path_3)
            
            sh.write('cd beta_')
            sh.write(str(item))
            sh.write('\n') 
            
            #file name for configuration file
            file_name = 'Alpha'+'_'+str(x)+'_beta_'+str(item)+'.cfg'
            #function call to create configuration file
            Rans(path_3,file_name,template_path,template_name,x,item) 
            
            #command to run SU2 in parallel; change number from 14 to your choice of cores
            command = "mpiexec -np 72 SU2_CFD "+file_name
            sh.write(command)
            sh.write('\n')
            sh.write('cd ..\n')
            sh.write('\n')
        sh.write('cd ..\n')
        sh.write('\n')
    sh.close()

#Mach value for sweep
mach = 0.7
# path to be created
path = "/home/vivek/Hiwi/phase_4/New_scripts/test"
os.mkdir(path)
#template name
template_name = 'Template.cfg'
#template path
template_path = "/home/vivek/Hiwi/phase_4/New_scripts"

#alpha sweep values
alpha = [-8,-6,-4,-2,0,2,4,6,8,10,11,12,13]
#beta sweep values
beta = [0,2,4,6,8,10]


#creates necessary folder and files for given mach sweep
#for multiple mach sweeps make a for loop iterating over a list of mach values
work(mach,path,template_name,template_path,alpha,beta)
    
    
