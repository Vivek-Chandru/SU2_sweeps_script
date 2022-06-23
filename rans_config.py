#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 00:25:09 2020

@author: vivek
"""



def Rans(path, filename, template_path, template_name, alpha, beta):
    filename = filename
    path = path
    template = template_path+"/"+template_name
    file = path+"/"+filename

    #input file
    fin = open(template, "rt")    
    #output file to write the result to
    fout = open(file,"wt")
    
    #for each line in the input file
    # modfies the included fields in the template file and returns a new file
    # add or remove fields as required
    # make sure to give a default value for the field to be modified in the template
    # and use that default value in the if else condition to replace
    for line in fin:
        if('AOA=0' in line):
        	fout.write(line.replace('0', str(alpha)))
        elif('MESH_FILENAME=xxx' in line):    
            fout.write(line.replace('xxx', mesh))
        elif('SIDESLIP_ANGLE= 0.0' in line):
            fout.write(line.replace('0.0', str(beta)))
        else:
            fout.write(line)
    #close input and output files
    fin.close()
    fout.close()
    