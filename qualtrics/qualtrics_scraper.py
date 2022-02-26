# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 21:05:12 2022

@author: Peilin Yang
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

import os




#url = 'https://stanforduniversity.qualtrics.com/jfe/form/SV_bgbAhGJZwv5Shr8'

url = "https://stanforduniversity.qualtrics.com/jfe/form/SV_9nyx2VHoas9YqcC"

chrome_options = Options()


# switch to iframe
#driver.find_element_by_xpath('//*[@id="NextButton"]').click()
#driver.find_element_by_xpath('/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[2]/input').click()
#sleep(1.4)



def page_scrape(driver):
    
    global current_index
    global current_file
    global record_list
    
    data = pd.read_excel("data_rep.xlsx", engine = "openpyxl")
    
    driver.switch_to.default_content()    
    #driver.switch_to.frame("preview-view")
    xpath = '//*[@id="Questions"]'
    problem_text = driver.find_element_by_xpath(xpath).text
    #problem_text = driver.find_element_by_xpath('/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/div/div[1]').text
    problem_text = problem_text.split("\n")
    # match id : problem_text[0]
    
    current_index = int(problem_text[0])
    record_list = os.listdir("record_rep")
    
    
    
    current_file = str(problem_text[0])+"_1.record"
    
    if current_file in record_list:
        current_file = str(problem_text[0])+"_2.record"
        if current_file in record_list:
            driver.quit()
        else:
            filename = open("record_rep/"+current_file, "w")
            filename.write(current_file)
            filename.close()
    else:
        filename = open("record_rep/"+current_file, "w")
        filename.write(current_file)
        filename.close()
    
    # Select 1 or 2
    data_id = data[data["block"]==current_index].iloc[int(current_file[-8])-1]
    
    # End of the page
    js = "var q=document.documentElement.scrollTop=100000"
    driver.execute_script(js)
    sleep(1.4)
    driver.find_element_by_xpath('//*[@id="NextButton"]').click()
    sleep(6)
       
    # Page 2: P1
    xpath_local = '//*[@id="QID644-'+str(data_id["rep11"])+'-label"]'
    driver.find_element_by_xpath(xpath_local).click()
    sleep(1.4)

    # Page 3: P2
    
    xpath_local = '//*[@id="QID646-'+str(data_id["rep12"])+'-label"]'
    driver.find_element_by_xpath(xpath_local).click()
    sleep(1.4)

    # Page 4: rep13 
    xpath_local = '//*[@id="QID647-'+str(data_id["rep13"])+'-label"]'
    driver.find_element_by_xpath(xpath_local).click()
    sleep(1.4)

    # status11
    xpath_local = '//*[@id="QID648-'+str(data_id["status11"])+'-label"]'
    driver.find_element_by_xpath(xpath_local).click()
    sleep(1.4)

    # status12 
    xpath_local = '//*[@id="QID649-'+str(data_id["status11"])+'-label"]'
    driver.find_element_by_xpath(xpath_local).click()
    sleep(1.4)

    # stigma11
    xpath_local = '//*[@id="QID650-'+str(data_id["stigma11"])+'-label"]'
    driver.find_element_by_xpath(xpath_local).click()
    sleep(1.4)

    # stigma12
    xpath_local = '//*[@id="QID651-'+str(data_id["stigma12"])+'-label"]'
    driver.find_element_by_xpath(xpath_local).click()
    sleep(1.4)

    # celebrity11
    xpath_local = '//*[@id="QID652-'+str(data_id["celebrity11"])+'-label"]'
    driver.find_element_by_xpath(xpath_local).click()
    sleep(1.4)

    # celebrity12
    xpath_local = '//*[@id="QID653-'+str(data_id["celebrity12"])+'-label"]'
    driver.find_element_by_xpath(xpath_local).click()
    sleep(1.4)

    # rep21
    xpath_local = '//*[@id="QID655-'+str(data_id["rep21"])+'-label"]'
    driver.find_element_by_xpath(xpath_local).click()
    sleep(1.4)

    # rep22 
    xpath_local = '//*[@id="QID656-'+str(data_id["rep22"])+'-label"]'
    driver.find_element_by_xpath(xpath_local).click()
    sleep(1.4)

    # rep23
    xpath_local = '//*[@id="QID657-'+str(data_id["rep23"])+'-label"]'
    driver.find_element_by_xpath(xpath_local).click()
    sleep(1.4)

    # status21
    xpath_local = '//*[@id="QID658-'+str(data_id["status21"])+'-label"]'
    driver.find_element_by_xpath(xpath_local).click()
    sleep(1.4)

    # status22
    xpath_local = '//*[@id="QID659-'+str(data_id["status22"])+'-label"]'
    driver.find_element_by_xpath(xpath_local).click()
    sleep(1.4)

    # stigma21
    xpath_local = '//*[@id="QID660-'+str(data_id["stigma21"])+'-label"]'
    driver.find_element_by_xpath(xpath_local).click()
    sleep(1.4)

    # stigma22
    xpath_local = '//*[@id="QID661-'+str(data_id["stigma22"])+'-label"]'
    driver.find_element_by_xpath(xpath_local).click()
    sleep(1.4)

    # celebrity21  
    xpath_local = '//*[@id="QID662-'+str(data_id["celebrity21"])+'-label"]'
    driver.find_element_by_xpath(xpath_local).click()
    sleep(1.4)

    # celebrity22
    xpath_local = '//*[@id="QID663-'+str(data_id["celebrity22"])+'-label"]'
    driver.find_element_by_xpath(xpath_local).click()
    sleep(1.4)

    # BLM 
    xpath_local = '//*[@id="QID630-'+str(data_id["blm"])+'-label"]'
    driver.find_element_by_xpath(xpath_local).click()
    sleep(1.4)

    # past 
    xpath_local = '//*[@id="QID631-'+str(data_id["past1_4"])+'-label"]'
    driver.find_element_by_xpath(xpath_local).click()
    sleep(1.4)

    
    # percent
    xpath_local = '//*[@id="QR~QID641"]'
    driver.find_element_by_xpath(xpath_local).send_keys(str(data_id["percent"]))
    #driver.find_element_by_xpath('//*[@id="QID641"]/div[3]/div/fieldset/div').click()
    driver.find_element_by_xpath(xpath_local).send_keys(Keys.ENTER)
    sleep(1.4)
    
    # support
    xpath_local = '//*[@id="QID625-'+str(7+int(data_id["support"]))+'-label"]'
    driver.find_element_by_xpath(xpath_local).click()
    sleep(1.4)

    
    # letter 
    xpath_local = '//*[@id="QR~QID610"]'
    driver.find_element_by_xpath(xpath_local).send_keys(str(data_id["letter"]))
    driver.find_element_by_xpath(xpath_local).send_keys(Keys.ENTER)
    sleep(1.4)
    # donate 
    xpath_local = '//*[@id="QR~QID626"]'
    driver.find_element_by_xpath(xpath_local).send_keys(str(data_id["donate"]))
    driver.find_element_by_xpath(xpath_local).send_keys(Keys.ENTER)
    sleep(1.4)
    
    # hypo1
    xpath_local = '//*[@id="QID665-'+str(data_id["hypo1"])+'-label"]'
    driver.find_element_by_xpath(xpath_local).click()
    sleep(1.4)

    # hypo2
    xpath_local = '//*[@id="QID666-'+str(data_id["hypo2"])+'-label"]'
    driver.find_element_by_xpath(xpath_local).click()
    sleep(1.4)

    # hypo3
    xpath_local = '//*[@id="QID667-'+str(data_id["hypo3"])+'-label"]'
    driver.find_element_by_xpath(xpath_local).click()
    sleep(1.4)

    # action
    xpath_local = '//*[@id="QID668-'+str(data_id["action"])+'-label"]'
    driver.find_element_by_xpath(xpath_local).click()
    sleep(1.4)

    # self
    xpath_local = '//*[@id="QID669-'+str(data_id["self"])+'-label"]'
    driver.find_element_by_xpath(xpath_local).click()
    sleep(1.4)

    # judge
    xpath_local = '//*[@id="QID670-'+str(data_id["judge"])+'-label"]'
    driver.find_element_by_xpath(xpath_local).click()
    sleep(1.4)

    # competent
    xpath_local = '//*[@id="QID671-'+str(data_id["competent"])+'-label"]'
    driver.find_element_by_xpath(xpath_local).click()
    sleep(1.4)

    # Info1
    xpath_local = '//*[@id="QID672-'+str(data_id["info1"])+'-label"]'
    driver.find_element_by_xpath(xpath_local).click()
    sleep(1.4)

    # Info2
    xpath_local = '//*[@id="QID673-'+str(data_id["info2"])+'-label"]'
    driver.find_element_by_xpath(xpath_local).click()
    sleep(1.4)

    # age 1
    xpath_local = '//*[@id="QID612-'+str(data_id["age"])+'-label"]'
    driver.find_element_by_xpath(xpath_local).click()
    sleep(1.4)

    # gender 2
    if int(data_id["gender"])==3:
        data_id["gender"] = 7
    xpath_local = '//*[@id="QID613-'+str(data_id["gender"])+'-label"]'
    driver.find_element_by_xpath(xpath_local).click()
    sleep(1.4)

    # race 3
    
    if int(data_id["race"])==2:
        data_id["race"] = 8
    if int(data_id["race"])==3:
        data_id["race"] = 2       
    if int(data_id["race"])==5:
        data_id["race"] = 3      
    if int(data_id["race"])==6:
        data_id["race"] = 7   
    xpath_local = '//*[@id="QID614-'+str(data_id["race"])+'-label"]'
    driver.find_element_by_xpath(xpath_local).click()

    sleep(1.4)

    # edu 4
    if int(data_id["edu"])==3:
        data_id["edu"] = 7
    if int(data_id["edu"])==4:
        data_id["edu"] = 8   
    xpath_local = '//*[@id="QID615-'+str(data_id["edu"])+'-label"]'
    driver.find_element_by_xpath(xpath_local).click()
    sleep(1.4)

    # job 5
    xpath_local = '//*[@id="QID616-'+str(data_id["job"])+'-label"]'
    driver.find_element_by_xpath(xpath_local).click()
    sleep(1.4)

    # income 6
    xpath_local = '//*[@id="QID617-'+str(int(data_id["income"]))+'-label"]'
    driver.find_element_by_xpath(xpath_local).click()
    sleep(1.4)

    # marry 7
    xpath_local = '//*[@id="QID618-'+str(data_id["marry"])+'-label"]'
    driver.find_element_by_xpath(xpath_local).click()
    sleep(1.4)

    # ideology 8
    xpath_local = '//*[@id="QID619-'+str(data_id["ideology"])+'-label"]'
    driver.find_element_by_xpath(xpath_local).click()
    sleep(1.4)

    # smo 9
    xpath_local = '//*[@id="QID620-'+str(int(data_id["smo"])+6)+'-label"]'
    driver.find_element_by_xpath(xpath_local).click()
    sleep(1.4)

    # journalist 10
    xpath_local = '//*[@id="QID636-'+str(int(data_id["journalist"])+6)+'-label"]'
    driver.find_element_by_xpath(xpath_local).click()
    sleep(1.4)

    # policymaker 11
    xpath_local = '//*[@id="QID637-'+str(int(data_id["policymaker"])+6)+'-label"]'
    driver.find_element_by_xpath(xpath_local).click()
    sleep(1.4)

    
    # csr
    xpath_local = '//*[@id="QID638-'+str(int(data_id["csr"])+6)+'-label"]'
    driver.find_element_by_xpath(xpath_local).click()
    sleep(1.4)

    # reason
    if int(data_id["reason"])==3:
        data_id["reason"]=6
    if int(data_id["reason"])==4:
        data_id["reason"]=5
    if int(data_id["reason"])==5:
        data_id["reason"]=7

    xpath_local = '//*[@id="QID621-'+str(data_id["reason"])+'-label"]'
    driver.find_element_by_xpath(xpath_local).click()
    sleep(1.4)

    # read
    xpath_local = '//*[@id="QID642-'+str(data_id["read"])+'-label"]'
    driver.find_element_by_xpath(xpath_local).click()
    sleep(1.4)
    #driver.find_element_by_xpath('//*[@id="NextButton"]').click()
    #sleep(2)
     
    # Answered
    #data['answer'].iloc[current_index] = 1
    #data.to_excel("data_rep.xlsx",index=False)
    driver.refresh()
    sleep(1.4)

#driver = webdriver.Chrome(options=chrome_options,executable_path=r"C:\Program Files\Google\Chrome\Application\chromedriver.exe")
driver = webdriver.Chrome(options=chrome_options)

driver.get(url)
sleep(1.4)



for i in range(1500):
    #try:
    page_scrape(driver)
    '''    
    except Exception as e:
        print(e)
        #os.remove("record_rep/"+current_file)
        #driver.refresh()
        driver.quit()
        driver = webdriver.Chrome(options=chrome_options,executable_path=r"C:\Program Files\Google\Chrome\Application\chromedriver.exe")
        #driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        #sleep(1.4) 
    '''
