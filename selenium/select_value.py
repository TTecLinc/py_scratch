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
from selenium.webdriver.support.select import Select
# Dom
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chrome_driver_path = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
driver = webdriver.Chrome(executable_path = chrome_driver_path)
driver.get("http://www.wanfangdata.com.cn/searchResult/getAdvancedSearch.do?searchType=all")


# Clear all the contents that are put into the box
# years options
#options=driver.find_element_by_xpath("//*[@id='advanced_search_publshdate_start']")

# Three ways to select

# 　 new Select(driver.findElement(By.id(“AAA”))).selectByVisibleText(“”);

#　　new Select(driver.findElement(By.id(“AAA”))).selectByValue(“”);

#　　new Select(driver.findElement(By.id(“AAA”))).selectByIndex(“”);

Select(driver.find_element_by_xpath("//*[@id='advanced_search_publshdate_start']")).select_by_value('2012')    
