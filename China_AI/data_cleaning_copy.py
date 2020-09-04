# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 07:43:16 2020

@author: Peilin Yang
"""


import get_rawdata_class 
import pickle
import pandas as pd
import numpy as np

sum_df=pd.DataFrame()
for i in range(2144):
    try:
        print("next",i)
        with open(str(i)+".pkl", 'rb') as f:
            data=pickle.load(f)
            df_sub=pd.DataFrame(data).T
            sum_df=pd.concat([sum_df,df_sub])
    except:
        continue

sum_df['page'], sum_df['position'] = sum_df.index.str.split(',', 1).str
sum_df['招考人数']=sum_df['招考人数'].astype("float")
sum_df.to_excel('police_panel.xlsx')

sum_people = sum_df.groupby(['page']).agg({'招考人数':'sum'})
