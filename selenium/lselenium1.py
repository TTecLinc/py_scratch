# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 15:23:39 2020

@author: Peilin Yang
"""


import requests
import urllib
import time
import random
from selenium import webdriver
# Dom
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chrome_driver_path = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
driver = webdriver.Chrome(executable_path = chrome_driver_path)
driver.get("https://fh.dujia.qunar.com/?tf=package")

destination="北京"
arrive="上海"

# Clear all the contents that are put into the box
driver.find_element_by_xpath("//*[@id='depCity']").clear()
driver.find_element_by_xpath("//*[@id='depCity']").send_keys(destination)
driver.find_element_by_xpath("//*[@id='arrCity']").send_keys(arrive)

driver.find_element_by_xpath("page_button").click()
pageBtns=driver.find_element_by_xpath("page_button")
if pageBtns==[]:
    break

results=[]
for i in range(1,10):
    routes=driver.find_element_by_xpath("//*[@id='app']/div/main/div[1]/div["+str(i)+"]")
    results.append(routes.text)
    
