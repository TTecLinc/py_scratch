# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 12:03:40 2020

@author: Peilin Yang
"""
import json
import codecs
import re
import sys

from collections import OrderedDict
from bs4 import BeautifulSoup
from selenium import webdriver

from selenium.webdriver.common.by import By
from datetime import datetime
from time import sleep
import random
from selenium.webdriver.chrome.options import Options


#Save and Load
import pickle

url="http://xz.offcn.com/zw/shannan/2013/"
url='http://xz.offcn.com/zw/naqu/2013/'
chromeOptions = webdriver.ChromeOptions()


sum_contain=0

list_of_dict_={}

# Get the list of the data
def get_dept_list():
    row=driver.find_elements_by_tag_name('tr')
    dict_={}
    for i in row:
        thname=i.find_elements_by_tag_name('th')
        tdname=i.find_elements_by_tag_name('td')
        if len(tdname)!=2:
           continue
            
        for i in range(2):
        #for item1 in tdname:
            text_sub=tdname[i].text
            if text_sub=='':
                break
            dict_[thname[i].text]=text_sub
            #print(dict_)
    return dict_




driver = webdriver.Chrome(options=chromeOptions)
driver.get(url)

strat_first=True
#---------------------------------------------------------------------------------------------
    ## Strat from 1 and Set the Password
    
if strat_first:
    contains = driver.find_elements_by_xpath("//*[contains(text(),'公安')]")
    range_num=len(contains)
    contains[0].click()
    driver.switch_to.window(driver.window_handles[-1])
    jobs_details = driver.find_elements_by_xpath("//*[contains(text(),'职位详情')]")
    # The first element is not button
    del jobs_details[0]
    
    jobs_details[0].click()
    driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[8]/div/a[1]").click()
    driver.find_element_by_xpath("//*[@id='phone']").send_keys('15500086359')
    driver.find_element_by_xpath("//*[@id='password']").send_keys('666666')
    driver.find_element_by_xpath("//*[@id='sh-login']/ul/li[3]/input").click()
    strat_first=False
    #chandles = driver.current_window_handle
    driver.switch_to.window(driver.window_handles[-1])
    driver.close()

for i in range(range_num):    
    print("next")
#---------------------------------------------------------------------------------------------


    driver.switch_to.window(driver.window_handles[-1])
    contains = driver.find_elements_by_xpath("//*[contains(text(),'公安')]")
    contains[i].click()
    driver.switch_to.window(driver.window_handles[-1])
    
    position_of_the_job='山南'
    

    local_table = driver.find_elements_by_xpath('/html/body/div[4]/div[2]/table')
    table_rows = local_table[0].find_elements_by_tag_name('tr')
    del table_rows[0]
    len_sub=len(table_rows)
#---------------------------------------------------------------------------------------------
    
    for i_jobs in range(len_sub):
        driver.switch_to.window(driver.window_handles[-1])
        # Select if it is for us
        rows_name=table_rows[i_jobs].find_elements_by_tag_name('td')
        if rows_name[0].text==position_of_the_job:
            rows_name[-2].click()
        
            sleep(1)
            # The first time needs to input password
            
            driver.switch_to.window(driver.window_handles[-1])
            
            lists=get_dept_list()
            list_of_dict_[str(i)+","+str(i_jobs)]=lists
            
            driver.close()
        
    
    # CLose Current Page
    driver.switch_to.window(driver.window_handles[-1])  
    driver.close()
    
    
driver.quit()



with open('1.pkl', 'wb') as f:
    pickle.dump(list_of_dict_, f, pickle.HIGHEST_PROTOCOL)


#with open('1.pkl', 'rb') as f:
#    pickle.load(f)

    

