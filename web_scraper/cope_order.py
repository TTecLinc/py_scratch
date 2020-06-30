# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 08:11:52 2020

@author: Peilin Yang
"""

import numpy as np
import pandas as pd
import os

# NOTE: the first step have to delete the un-formal data!

def getfile():

    filenames = os.listdir('.')

    mf = []

    for filename in filenames:

        if 'xlsx' in filename:

            mf.append(filename)

    return mf
    
NAME=
#
#  

data= pd.read_csv('CGG_'+NAME+'.csv')

#data.sort_values(by='web-scraper-order')

# num name num_give peo_name cop first year

# the position of the last completed page
numpage=int(max(data['xu_hao']))
left=np.mod(numpage,20)
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

#num=(numpage-left)*(num_col-3)

#'''
for col in range(3,num_col):
    num=numpage-left
    for j in range(left):
        #p1=20*(num_col-3)*i+j+20*(col-3)
        p1=(numpage-left)*(num_col-3)+j+left*(col-3)
        if p1>data.shape[0]-1:
            break
        data.iloc[num,col]=data.iloc[p1,col]
        #print(p1)
        num=num+1
data=data.iloc[:numpage,:]
#data.to_excel('20200629_'+NAME+'.xlsx')
#os.startfile(r'20200629_'+NAME+'.xlsx')
#'''