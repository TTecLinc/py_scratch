# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 23:25:30 2020

@author: Peilin Yang
"""
import json
import codecs
import re


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
    
    def __init__(self,url):
        self.url=url
        self.chromeOptions = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=self.chromeOptions)
        self.driver.set_page_load_timeout(5)
    
    
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
        
        #chandles = driver.current_window_handle
        driver.switch_to.window(driver.window_handles[-1])
        driver.close()
        return range_num
    
    def save_pkl(self,list_of_dict_):
        with open('1.pkl', 'wb') as f:
            pickle.dump(list_of_dict_, f, pickle.HIGHEST_PROTOCOL)
            
    def get_sub_jobs(self,page_num,i_jobs,jobs_details,list_of_dict_):
        driver=self.driver
        
        driver.switch_to.window(driver.window_handles[-1])
        
        jobs_details[i_jobs].click()
        sleep(0.3)
        # The first time needs to input password
        
        driver.switch_to.window(driver.window_handles[-1])
        
        lists=self.get_dept_list(driver)
        list_of_dict_[str(page_num)+","+str(i_jobs)]=lists
        
        driver.close()
        return list_of_dict_
    
    def get_jobs(self,page_num,i,list_of_dict_):
        driver=self.driver
        driver.switch_to.window(driver.window_handles[-1])
        contains = driver.find_elements_by_xpath("//*[contains(text(),'公安')]")
        contains[i].click()
        driver.switch_to.window(driver.window_handles[-1])
        jobs_details = driver.find_elements_by_xpath("//*[contains(text(),'职位详情')]")
        del jobs_details[0]
        len_sub=len(jobs_details)
        
        #---------------------------------------------------------------------------------------------
        # get sub jobs
        i_jobs=0
        while i_jobs<len_sub:
            try:
                list_of_dict_=self.get_sub_jobs(page_num,i_jobs,jobs_details,list_of_dict_)     
                i_jobs+=1
            except:
                driver.switch_to.window(driver.window_handles[-1])
                driver.close()
                driver.switch_to.window(driver.window_handles[-1])
                
        
        # CLose Current Page
        driver.switch_to.window(driver.window_handles[-1])  
        driver.close()
        return list_of_dict_

    def get_data(self,page_num):
        
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
                self.get_jobs(page_num,i,list_of_dict_)
                i+=1
            except:
                driver.switch_to.window(driver.window_handles[-1])
                driver.close()
                driver.switch_to.window(driver.window_handles[-1])
                
        print('here')
        # Save the File
        self.save_pkl(list_of_dict_)
        
        driver.quit()
    def wrong_restart(self):
        self.driver.quit()
        

#with open('1.pkl', 'rb') as f:
#    pickle.load(f)

    
