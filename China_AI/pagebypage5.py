# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 18:05:30 2020

@author: Peilin Yang
"""


import pandas as pd

import get_rawdata_class

data = pd.read_excel('20200830_links.xlsx')
data = data[(data['found_table']>0) & (data['job_count']>0)]
url = list(data['url'])
time=1000

wrong=0
#thread1
while time<1700:
    Get_raw=get_rawdata_class.Get_Raw_data(url[time])
    try:
         
        Get_raw.get_data(time)
        time+=1
    except:
        if wrong>3:
            time+=1
            continue
        
        print('Wrong, Again')
        Get_raw.wrong_restart()
        wrong+=1
        # Re try
        #time-=1
    
        