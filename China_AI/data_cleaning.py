# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 07:43:16 2020

@author: Peilin Yang
"""


import get_rawdata_class 
import pickle
import pandas as pd
import numpy as np
data = pd.read_excel('20200830_links.xlsx')
data = data[(data['found_table']>0) & (data['job_count']>0)]
url = list(data['url'])
citys = list(data['city_short'])
time=0

sum_df=pd.DataFrame()
for i in range(2144):
    try:
        print("next",i)
        with open(str(data.index[i])+".pkl", 'rb') as f:
            data1=pickle.load(f)
            df_sub=pd.DataFrame(data1).T
        sum_df=pd.concat([sum_df,df_sub])
    except:
        continue



sum_df.to_excel('sum_df.xlsx')
sum_df['page'], sum_df['position'] = sum_df.index.str.split(',', 1).str
sum_df['招考人数']=sum_df['招考人数'].astype("float")
sum_df.to_excel('police_panel.xlsx')

sum_people = sum_df.groupby(['page']).agg({'招考人数':'sum'})
