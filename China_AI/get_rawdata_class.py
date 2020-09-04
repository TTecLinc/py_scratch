# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 23:25:30 2020

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
from selenium.common.exceptions import TimeoutException
#Save and Load
import pickle


class Get_Raw_data:
    
    def __init__(self,url,citys):
        self.url=url
        #path='C:\Program Files\Google\Chrome\Application\chromedriver.exe'
        self.chromeOptions = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=self.chromeOptions)
        self.driver.set_page_load_timeout(3)
        self.citys=citys
    
    
    # Get the list of the data
    def get_dept_list(self,driver):
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



    def input_password(self):
        
        driver=self.driver
        contains = driver.find_elements_by_xpath("//*[contains(text(),'公安')]")
        range_num=len(contains)
        sleep(0.5)
        contains[0].click()
        
        driver.switch_to.window(driver.window_handles[-1])
        jobs_details = driver.find_elements_by_xpath("//*[contains(text(),'职位详情')]")
        # The first element is not button
        del jobs_details[0]
        
        jobs_details[0].click()
        #sleep(0.1)
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[8]/div/a[1]").click()
        driver.find_element_by_xpath("//*[@id='phone']").send_keys('15500086359')
        driver.find_element_by_xpath("//*[@id='password']").send_keys('666666')
        driver.find_element_by_xpath("//*[@id='sh-login']/ul/li[3]/input").click()
        
        #chandles = driver.current_window_handle
        driver.switch_to.window(driver.window_handles[-1])
        driver.close()
        return range_num
    
    def save_pkl(self,num,list_of_dict_):
        with open(str(num)+'.pkl', 'wb') as f:
            pickle.dump(list_of_dict_, f, pickle.HIGHEST_PROTOCOL)
            
    def get_sub_jobs(self,page_num,jobs,i_jobs,table_rows,position_of_the_job):

        driver = self.driver
        rows_name=table_rows[i_jobs].find_elements_by_tag_name('td')

        if rows_name[0].text==position_of_the_job:
            rows_name[-2].click()
        
            #sleep(0.5)
            # The first time needs to input password
            
            driver.switch_to.window(driver.window_handles[-1])
            
            lists=self.get_dept_list(driver)
        
            return lists
        else:
            return 'next'
    
    def get_jobs(self,page_num,i,list_of_dict_,position_of_the_job):
        driver=self.driver
        driver.switch_to.window(driver.window_handles[-1])
        contains = driver.find_elements_by_xpath("//*[contains(text(),'公安')]")
        #sleep(1)
        contains[i].click()
        #sleep(0.1)
        driver.switch_to.window(driver.window_handles[-1])

        # Select if it is for us
        
        local_table = driver.find_elements_by_xpath('/html/body/div[4]/div[2]/table')
        table_rows = local_table[0].find_elements_by_tag_name('tr')
        del table_rows[0]
        len_sub=len(table_rows)
        
        #---------------------------------------------------------------------------------------------
        # get sub jobs

        i_jobs=0
        while i_jobs<len_sub:
            driver.switch_to.window(driver.window_handles[-1])
            try:
                lists=self.get_sub_jobs(page_num,i,i_jobs,table_rows,position_of_the_job)
                if lists=='next':
                    i_jobs+=1
                    continue
                elif lists:
                    list_of_dict_[str(page_num)+","+str(i)+","+str(i_jobs)]=lists
                    i_jobs+=1
                    driver.close()
                else:
                    driver.close()
                    continue
            except:
                print('reload')
                driver.switch_to.window(driver.window_handles[-1])
                driver.close()
                driver.switch_to.window(driver.window_handles[-1])
                
                
        
        # CLose Current Page
        driver.switch_to.window(driver.window_handles[-1])  
        driver.close()
        return list_of_dict_

    def get_data(self,page_num):
        
        position_of_the_job=self.citys
        
        driver=self.driver
        
        driver.get(self.url)
        

        list_of_dict_={}
        strat_first=True
        #---------------------------------------------------------------------------------------------
            ## Strat from 1 and Set the Password
            
        if strat_first:
            range_num=self.input_password()
            strat_first=False
        
        #for i in range(range_num): 
        i=0
        while i<range_num:
            
            print("next")
            
            #---------------------------------------------------------------------------------------------
            
            try:
                self.get_jobs(page_num,i,list_of_dict_,position_of_the_job)
                i+=1
            except:
                driver.switch_to.window(driver.window_handles[-1])
                driver.close()
                driver.switch_to.window(driver.window_handles[-1])
                
                
        print('here')
        # Save the File
        self.save_pkl(page_num,list_of_dict_)
        
        driver.quit()
    def wrong_restart(self):
        self.driver.quit()
        

#with open('1.pkl', 'rb') as f:
#    pickle.load(f)

    
