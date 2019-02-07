# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 16:18:19 2019

PURPOSE: Print a list of .csv source files from <hard_coded_directory>\<study> and return a list containing the file names

INPUT: 
    bdm_study_code: str
        
OUTPUT: list()
    list of the source files that are of file type .csv

@author: duchezbr
"""

from os import listdir

def list_src_files(bdm_study_code):

    file_type = '.csv'
    
    files = listdir(r"<hard_coded_directory>\<study> " + "\\" + bdm_study_code)
    
    lst_files = list()
    for file in files:
        if file.endswith(file_type):
            lst_files.append(file)
            
    for file in lst_files:
        print(file)
    
    return lst_files