# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 15:26:54 2019

PURPOSE: Import source file from \\md1fs019\Ts\File_Transfer\BDM_SRC_DATA\<study> directory along with a number of libraries potentially useful for evaluating souce data.

INPUT: 
    bdm_study_code: str
    file_name: str
        in the format <file>.csv
        
OUTPUT: pandas DataFrame

@author: duchezbr
"""


def import_src_file(bdm_study_code, file_name):
    
    df = pd.read_csv(r"\\md1fs019\Ts\File_Transfer\BDM_SRC_DATA" + "\\" + bdm_study_code + "\\" + file_name, low_memory=False) 
    
    return df
