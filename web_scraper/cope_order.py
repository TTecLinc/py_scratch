# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 08:11:52 2020

@author: Peilin Yang
"""

import numpy as np
import pandas as pd

# NOTE: the first step have to delete the un-formal data!

NAME='17_part2国家社会科学基金'
data= pd.read_csv('raw'+NAME+'.csv')



# num name num_give peo_name cop first year

# the position of the last completed page
numpage=1192
num_col=data.shape[1]
#'''
#0 140 280 
#20 160 
#5740 821
for col in range(3,num_col):
    num=0
    for i in range(203):
        for j in range(20):
            p1=20*(num_col-3)*i+j+20*(col-3)
            if p1>data.shape[0]-2:
                break
            data.iloc[num,col]=data.iloc[p1,col]
            #print(p1)
            num=num+1
    
data=data.iloc[:numpage,:]
data.to_excel(NAME+'.xlsx')
#'''
    
