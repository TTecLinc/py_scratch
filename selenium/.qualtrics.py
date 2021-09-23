# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 16:22:33 2021

@author: Peilin Yang
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep


__name__=1
thread_number = 1
if __name__ == thread_number:

    url = 'https://stanforduniversity.ca1.qualtrics.com/surveys/SV_4ZQ78h5ICvvmPie/edit?Section=SV_4ZQ78h5ICvvmPie'
    
    
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    
    driver.find_element_by_xpath('//*[@id="Survey"]/div[3]/div[2]/button').click()
    
    ntotal = 6
    # Add a new question
    for n_q in range(ntotal):
        # Survey Block
        survey = driver.find_element_by_xpath('//*[@id="Survey"]')
        # Survey Block
        blocks=survey.find_elements_by_class_name('BlockOuter')
        # Block CLass
        buttons=blocks[-2].find_elements_by_class_name('_1_x8D')
        
        buttons[-1].click()    
        sleep(1)
        # text/graph
        driver.find_element_by_xpath('//*[@id="question-type-footer-dropdown-DB"]').click()
        sleep(1)
        # find text
        text_block = blocks[-2].find_elements_by_class_name('QuestionPreview')
        text_block[0].click()
        sleep(1)
        # clear
        driver.find_element_by_xpath('//*[@id="InlineEditorElement"]').clear()
        driver.find_element_by_xpath('//*[@id="InlineEditorElement"]').send_keys('A')
        if n_q<ntotal-1:
            # Add block
            driver.find_element_by_xpath('//*[@id="Survey"]/div['+str(n_q+3)+']/div[2]/button').click()
            sleep(1)
    

