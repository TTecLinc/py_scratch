# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 14:31:42 2020

@author: Peilin Yang
"""


from university import *
import yaml
import os
import json
import pandas as pd
import time
import random

depkey_list=pd.read_excel("structure_key_main.xlsx")


'''
yaml_path=r"~\Wanfang\Scraping_Learders\leaders_detail.yaml"
file_yaml=open(yaml_path,'r',encoding='utf-8')
read_yaml=file_yaml.read()
dict_yaml=yaml.load(read_yaml)
leaders=list(dict_yaml.keys())

# Save the dict to file

s=str(dict_yaml)
f=open('dict.txt','w')
f.writelines(s)
f.close()
'''

# Read the list of leaders
file_dict = open('leaders_detail.txt', 'r')
# Return the value of string
dict_yaml = eval(file_dict.read()) 
file_dict.close()
leader_list=list(dict_yaml.keys())
#leader_list=leader_list[0:100]

# Switch to leaders
Current_Position=1093

# Save paper>50 for checking 
# DON'T FORGET TO CHECK THIS EVERY TIME EXIT!!!
Position_big2=[]

#Current_Position2=801

while True:
    try:
        # Double Keep
        for i in range(Current_Position,1479):
        #for i in range(Current_Position2,1479):
            Current_Position=i
            #Current_Position2=i
            # Report Error System
            leader_name=leader_list[i]
            print("Current Position: ",i)
            
            
            univ_name=dict_yaml[leader_name]['univ']
            year_list=dict_yaml[leader_name]['in_office']
            univ = university(univ_name,leader_name,str(year_list[0]),str(year_list[-1]))
            driver = univ.GetDriver()
            
            #time.sleep(random.uniform(1,2))
            if univ.haveresult():
                total = univ.GetTotalNum()
                
                subject_restrict = False
                
                if total>20:
                    univ.shortify()
                    # Save current position
                    if total>20:
                        Position_big2.append(i)
                        time.sleep(1)
                univ.YearRoll(total) # 按照既定的顺序爬，并且导出文献内容
                    
                #univ.DeleteRestriction(year)

            driver.close()
            #time.sleep(random.uniform(1,2))
            with open("log_wanfang.txt", 'a') as log:
                log.write(str(datetime.datetime.now()) + '    ' )
                log.write("Finished " + univ_name)
                log.write('\n')
                year_list=dict_yaml[leader_name]['in_office']
        break

    except:
        print("Error, trying to reboot...")
        continue
        #driver.close()

        # 写入log
        with open("log_wanfang.txt", 'a') as log:
            log.write(str(datetime.datetime.now()) + '    ')
            #if subject_restrict:
            #    log.write(str(year) + ' ' + univ_name + ' ' + subject[0])
            #else:
            log.write(str(i) + ' ' + univ_name + " only years")
            log.write('\n')
        
        #if subject_restrict:
        #    stop_subject_index = subject_list.index(subject)
        #    subject_list = subject_list[stop_subject_index:]


        #stop_year_index = year_list.index(i)
        #year_list = year_list[stop_year_index:]