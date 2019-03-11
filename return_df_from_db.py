# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 10:43:39 2019

PURPOSE: Return the result of Oracle DB query to a pandas DataFrame
 
INPUT:
    cursor: query result
    columns: list
        name of columns for data returned from the database query
        
OUTPUT: 
    table: pandas DataFrame
        data returned from DB query

@author: duchezbr
"""

def return_df_from_db(cursor, columns):
    data=list()
    for row in cursor:
        data.append(row)
    table = pd.DataFrame(data=data, columns=columns)
    
    return table

