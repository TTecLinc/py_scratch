# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 21:05:12 2022

@author: Peilin Yang
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import pandas as pd


data = pd.read_excel("data_rep.xlsx", engine = "openpyxl")

url = 'https://stanforduniversity.qualtrics.com/jfe/preview/SV_8f5gkrYnIWRiKdU?Q_CHL=preview&Q_SurveyVersionID=current'

chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)
driver.maximize_window()
sleep(1)
# close phone panel
#driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/label[2]/span').click()

# switch to iframe
#driver.find_element_by_xpath('//*[@id="NextButton"]').click()
#driver.find_element_by_xpath('/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[2]/input').click()
#sleep(1)

# Page 1: find text
#driver.switch_to.default_content()
driver.switch_to.frame("preview-view")
problem_text = driver.find_element_by_xpath('/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/div/div[1]').text
problem_text = problem_text.split("\n")
# match id : problem_text[0]
data_id = data[data["block"]==int(problem_text[0])].iloc[0]

# End of the page
js = "var q=document.documentElement.scrollTop=100000"
driver.execute_script(js)

driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(5)

#driver.find_element_by_xpath('//*[@id="QID633"]/div[3]/div/fieldset/div/table').text

# Page 2: P1
xpath_local = '//*[@id="QID644"]/div[3]/div/fieldset/div/ul/li['+str(data_id["rep11"])+']/label'
driver.find_element_by_xpath(xpath_local).click()
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)
# Page 3: P2
xpath_local = '//*[@id="QID646"]/div[3]/div/fieldset/div/ul/li['+str(data_id["rep12"])+']/label'
driver.find_element_by_xpath(xpath_local).click()
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)
# Page 4: rep13 
xpath_local = '//*[@id="QID647"]/div[3]/div/fieldset/div/ul/li['+str(data_id["rep13"])+']/label'
driver.find_element_by_xpath(xpath_local).click()
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)
# status11
xpath_local = '//*[@id="QID648"]/div[3]/div/fieldset/div/ul/li['+str(data_id["status11"])+']/label'
driver.find_element_by_xpath(xpath_local).click()
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)
# status12 
xpath_local = '//*[@id="QID649"]/div[3]/div/fieldset/div/ul/li['+str(data_id["status11"])+']/label'
driver.find_element_by_xpath(xpath_local).click()
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)
# stigma11
xpath_local = '//*[@id="QID650"]/div[3]/div/fieldset/div/ul/li['+str(data_id["stigma11"])+']/label'
driver.find_element_by_xpath(xpath_local).click()
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)
# stigma12
xpath_local = '//*[@id="QID651"]/div[3]/div/fieldset/div/ul/li['+str(data_id["stigma12"])+']/label'
driver.find_element_by_xpath(xpath_local).click()
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)
# celebrity11
xpath_local = '//*[@id="QID652"]/div[3]/div/fieldset/div/ul/li['+str(data_id["celebrity11"])+']/label'
driver.find_element_by_xpath(xpath_local).click()
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)
# celebrity12
xpath_local = '//*[@id="QID653"]/div[3]/div/fieldset/div/ul/li['+str(data_id["celebrity12"])+']/label'
driver.find_element_by_xpath(xpath_local).click()
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)
# rep21
xpath_local = '//*[@id="QID655"]/div[3]/div/fieldset/div/ul/li['+str(data_id["rep21"])+']/label'
driver.find_element_by_xpath(xpath_local).click()
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)
# rep22 
xpath_local = '//*[@id="QID656"]/div[3]/div/fieldset/div/ul/li['+str(data_id["rep22"])+']/label'
driver.find_element_by_xpath(xpath_local).click()
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)
# rep23
xpath_local = '//*[@id="QID657"]/div[3]/div/fieldset/div/ul/li['+str(data_id["rep23"])+']/label'
driver.find_element_by_xpath(xpath_local).click()
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)
# status21
xpath_local = '//*[@id="QID658"]/div[3]/div/fieldset/div/ul/li['+str(data_id["status21"])+']/label'
driver.find_element_by_xpath(xpath_local).click()
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)
# status22
xpath_local = '//*[@id="QID659"]/div[3]/div/fieldset/div/ul/li['+str(data_id["status22"])+']/label'
driver.find_element_by_xpath(xpath_local).click()
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)
# stigma21
xpath_local = '//*[@id="QID660"]/div[3]/div/fieldset/div/ul/li['+str(data_id["stigma21"])+']/label'
driver.find_element_by_xpath(xpath_local).click()
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)
# stigma22
xpath_local = '//*[@id="QID661"]/div[3]/div/fieldset/div/ul/li['+str(data_id["stigma22"])+']/label'
driver.find_element_by_xpath(xpath_local).click()
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)
# celebrity21  
xpath_local = '//*[@id="QID662"]/div[3]/div/fieldset/div/ul/li['+str(data_id["celebrity21"])+']/label'
driver.find_element_by_xpath(xpath_local).click()
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)
# celebrity22
xpath_local = '//*[@id="QID663"]/div[3]/div/fieldset/div/ul/li['+str(data_id["celebrity22"])+']/label'
driver.find_element_by_xpath(xpath_local).click()
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)
# BLM 
xpath_local = '//*[@id="QID630"]/div[3]/div/fieldset/div/ul/li['+str(data_id["blm"])+']/label'
driver.find_element_by_xpath(xpath_local).click()
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)
# past 
xpath_local = '//*[@id="QID631"]/div[3]/div/fieldset/div/ul/li['+str(data_id["past1_4"])+']/label'
driver.find_element_by_xpath(xpath_local).click()
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)

# percent
xpath_local = '//*[@id="QR~QID641"]'
driver.find_element_by_xpath(xpath_local).send_keys(str(data_id["percent"]))
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)
# support
xpath_local = '//*[@id="QID625"]/div[3]/div/fieldset/div/ul/li['+str(data_id["support"])+']/label'
driver.find_element_by_xpath(xpath_local).click()
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)

# letter 
xpath_local = '//*[@id="QR~QID610"]'
driver.find_element_by_xpath(xpath_local).send_keys(str(data_id["letter"]))
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)
# donate 
xpath_local = '//*[@id="QR~QID626"]'
driver.find_element_by_xpath(xpath_local).send_keys(str(data_id["donate"]))
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)
# hypo1
xpath_local = '//*[@id="QID665"]/div[3]/div/fieldset/div/ul/li['+str(data_id["hypo1"])+']/label'
driver.find_element_by_xpath(xpath_local).click()
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)
# hypo2
xpath_local = '//*[@id="QID666"]/div[3]/div/fieldset/div/ul/li['+str(data_id["hypo2"])+']/label'
driver.find_element_by_xpath(xpath_local).click()
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)
# hypo3
xpath_local = '//*[@id="QID667"]/div[3]/div/fieldset/div/ul/li['+str(data_id["hypo3"])+']/label'
driver.find_element_by_xpath(xpath_local).click()
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)
# action
xpath_local = '//*[@id="QID668"]/div[3]/div/fieldset/div/ul/li['+str(data_id["action"])+']/label'
driver.find_element_by_xpath(xpath_local).click()
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)
# self
xpath_local = '//*[@id="QID669"]/div[3]/div/fieldset/div/ul/li['+str(data_id["self"])+']/label'
driver.find_element_by_xpath(xpath_local).click()
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)
# judge
xpath_local = '//*[@id="QID670"]/div[3]/div/fieldset/div/ul/li['+str(data_id["judge"])+']/label'
driver.find_element_by_xpath(xpath_local).click()
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)
# competent
xpath_local = '//*[@id="QID671"]/div[3]/div/fieldset/div/ul/li['+str(data_id["competent"])+']/label'
driver.find_element_by_xpath(xpath_local).click()
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)
# Info1
xpath_local = '//*[@id="QID672"]/div[3]/div/fieldset/div/ul/li['+str(data_id["info1"])+']/label'
driver.find_element_by_xpath(xpath_local).click()
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)
# Info2
xpath_local = '//*[@id="QID673"]/div[3]/div/fieldset/div/ul/li['+str(data_id["info2"])+']/label'
driver.find_element_by_xpath(xpath_local).click()
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)
# age 1
xpath_local = '//*[@id="QID612"]/div[3]/div/fieldset/div/ul/li['+str(data_id["age"])+']/label'
driver.find_element_by_xpath(xpath_local).click()
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)
# gender 2
xpath_local = '//*[@id="QID613"]/div[3]/div/fieldset/div/ul/li['+str(data_id["gender"])+']/label'
driver.find_element_by_xpath(xpath_local).click()
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)
# race 3
xpath_local = '//*[@id="QID614"]/div[3]/div/fieldset/div/ul/li['+str(data_id["race"])+']/label'
driver.find_element_by_xpath(xpath_local).click()
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)
# edu 4
xpath_local = '//*[@id="QID615"]/div[3]/div/fieldset/div/ul/li['+str(data_id["edu"])+']/label'
driver.find_element_by_xpath(xpath_local).click()
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)
# job 5
xpath_local = '//*[@id="QID616"]/div[3]/div/fieldset/div/ul/li['+str(data_id["job"])+']/label'
driver.find_element_by_xpath(xpath_local).click()
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)
# income 6
xpath_local = '//*[@id="QID617"]/div[3]/div/fieldset/div/ul/li['+str(data_id["income"])+']/label'
driver.find_element_by_xpath(xpath_local).click()
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)
# marry 7
xpath_local = '//*[@id="QID618"]/div[3]/div/fieldset/div/ul/li['+str(data_id["marry"])+']/label'
driver.find_element_by_xpath(xpath_local).click()
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)
# ideology 8
xpath_local = '//*[@id="QID619"]/div[3]/div/fieldset/div/ul/li['+str(data_id["ideology"])+']/label'
driver.find_element_by_xpath(xpath_local).click()
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)
# smo 9
xpath_local = '//*[@id="QID620"]/div[3]/div/fieldset/div/ul/li['+str(data_id["smo"])+']/label'
driver.find_element_by_xpath(xpath_local).click()
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)
# journalist 10
xpath_local = '//*[@id="QID636"]/div[3]/div/fieldset/div/ul/li['+str(data_id["journalist"])+']/label'
driver.find_element_by_xpath(xpath_local).click()
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)
# policymaker 11
xpath_local = '//*[@id="QID637"]/div[3]/div/fieldset/div/ul/li['+str(data_id["policymaker"])+']/label'
driver.find_element_by_xpath(xpath_local).click()
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)

# csr
xpath_local = '//*[@id="QID638"]/div[3]/div/fieldset/div/ul/li['+str(data_id["csr"])+']/label'
driver.find_element_by_xpath(xpath_local).click()
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)
# reason
xpath_local = '//*[@id="QID621"]/div[3]/div/fieldset/div/ul/li['+str(data_id["reason"])+']/label'
driver.find_element_by_xpath(xpath_local).click()
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)
# read
xpath_local = '//*[@id="QID642"]/div[3]/div/fieldset/div/ul/li['+str(data_id["read"])+']/label'
driver.find_element_by_xpath(xpath_local).click()
driver.find_element_by_xpath('//*[@id="NextButton"]').click()
sleep(1)

