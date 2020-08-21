# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 14:31:42 2020

@author: Andy Zhao, Peilin Yang 

NOTE:
    
This part is for leaders, not for university 
"""


#coding=utf-8
from selenium import webdriver
import time
import random
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException,TimeoutException
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import datetime
from selenium.webdriver.support.select import Select

class university():
    def __init__(self, univ_name,leader_name,start_year='1990',end_year='2020'):
        chrome_option = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2, 'profile.default_content_settings.popups': 0}
        #"download.default_directory": "\\WanfangDownload\\"+ univ_name}
        #"/Users/andyzhao/Downloads/"+univ_name
        #"/home/ec2-user"+univ_name
        #above line for AWS
        self.univ_name = univ_name
        chrome_option.add_experimental_option('prefs', prefs)
        chrome_option.add_argument("start-maximized")

        chrome_option.add_argument('--disable-extensions') # 禁止扩展加载
        #chrome_option.add_argument('--headless')
        
        #Set the Path of Chrome Driver
        chrome_driver_path = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
        self.webdriver = webdriver.Chrome(executable_path = chrome_driver_path)
        '''
        chrome_option.headless = True
        

        # add missing support for chrome "send_command"  to selenium webdriver
        #params = {'behavior': 'allow', 'downloadPath': "/home/ec2-user"+univ_name}
        #self.webdriver.execute_cdp_cmd('Page.setDownloadBehavior', params)
        self.webdriver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
        params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath':univ_name}}
        self.webdriver.execute("send_command", params)
        '''

        
        url = '''http://www.wanfangdata.com.cn/searchResult/getAdvancedSearch.do?searchType=all'''
        self.webdriver.get(url)
        self.webdriver.implicitly_wait(1)
        # Click 排除"学位论文"
        self.webdriver.find_element_by_xpath('//span[@value="degree-degree_artical"]').click() 
        
        self.webdriver.find_element_by_xpath("//*[contains(text(), '{}')]".format('作者单位')).click()
        
        ## Name of University 
        self.webdriver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[2]/div[2]/div[1]/div/div[3]/input").send_keys(univ_name)
        
        ## Name of Leader
        self.webdriver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/div[2]/div[2]/div/div[3]/input').send_keys(leader_name)
        
        ## Select the start and end year
        Select(self.webdriver.find_element_by_xpath("//*[@id='advanced_search_publshdate_start']")).select_by_value(start_year)
        Select(self.webdriver.find_element_by_xpath("//*[@id='advanced_search_publshdate_end']")).select_by_value(end_year)
        
        self.webdriver.find_element_by_xpath('//*[@name="vague_accurate"]/option[2]').click()  # 精准检索
        time.sleep(random.uniform(0,1))
        self.webdriver.find_element_by_xpath('//*[@id="set_advanced_search_btn"]').click()
        self.wait = WebDriverWait(self.GetDriver(), 1)

    def GetDriver(self):
        return self.webdriver

    # 将每页文章数设为50
    def shortify(self):
        self.webdriver.find_element_by_xpath('//*[@id="select4"]/option[3]').click()
        

    # 实现翻页，如果页面没有“下一页”说明到了最后一页
    def Goto_next(self):
        while True:
            try:
                self.webdriver.find_element_by_link_text("下一页").click()
                time.sleep(1)
                break
            except StaleElementReferenceException:
                print('StaleElementReferenceException')
                time.sleep(1)


    # 运行js代码
    def Restrict_Subject(self, subject):
        self.webdriver.execute_script("searchByFacetNav('{}','$subject_classcode_level','{}');".format(subject[0],subject[1]))

    # Restrict_Year
    def Restrict_Year(self, year):
        self.webdriver.execute_script("searchByFacetNav('{}','$common_year','{}');".format(year,year))

    # 获取总文章数信息
    def GetTotalNum(self):
        old_element = self.webdriver.find_element_by_xpath('//*[@id="result_stati_date_count_1"]/div/strong')
        try:
            start_time = datetime.datetime.now()
            WebDriverWait(self.webdriver, 1).until(EC.staleness_of(old_element))
            end_time = datetime.datetime.now()
            print("Explicit wait in GetTotalNum, waited {}".format(end_time-start_time))
            return int(self.webdriver.find_element_by_xpath('//*[@id="result_stati_date_count_1"]/div/strong').text)
        except TimeoutException:
            return(int(old_element.text))

    def DeleteRestriction(self, restriction):
        restriction = str(restriction)
        while True:
            try:
                self.webdriver.find_element_by_xpath('//div[@class="FilerItem"]/span[contains(text(), "{}")]/i'.format(restriction)).click()
                print('Delete',restriction)
                #time.sleep(1)
                break
            except StaleElementReferenceException:
                time.sleep(0)

    def haveresult(self):
        '''
        If a certain subject has result in one year?
        :return:
        '''
        try:
            self.webdriver.find_element_by_class_name("mod-results-list-empty")
            print('No result in this subject')
            return False
        except:
            return True
        
    def GetData_byperson(self, total_num):
        '''
        Choose all and move to next page. Download every 10 pages.
        :return: void.
        '''
        page_num = 0
        #page_limit=min(100, math.ceil(total_num/50))
        page_limit=math.ceil(total_num/50)
        print('Page Limit:', page_limit)
        previous_element = None

        while page_num < page_limit:
            try:
                print(self.univ_name, 'Page', page_num + 1)
                if page_num == 0:
                    time.sleep(0)
                else:
                    self.wait.until(EC.staleness_of(previous_element))
                    
                self.webdriver.find_element_by_xpath('//*[@name="checkAll"]').click()  # 全选所有文献

                # 如果第一篇文章仍然未被选中，则重新选一次
                #try:
                #    checkbox = self.webdriver.find_element_by_id('label_1_1')
                #except NoSuchElementException:
                #    break
                #if not checkbox.is_selected():
                #    self.webdriver.find_element_by_xpath('//*[@name="checkAll"]').click()

                page_num += 1
                previous_element = self.webdriver.find_element_by_id("list_div_aa_1")
                #if page_num%10==0 and page_num!=0: #每十页导出一次
                #    self.ExplorePub()
                if page_num<page_limit:
                    try:
                        self.Goto_next()
                    except NoSuchElementException:
                        self.ExplorePub()
                        break

            except StaleElementReferenceException:
                print('stale')
                

        
    def YearRoll(self, total_num):
        '''
        Choose all and move to next page. Download every 10 pages.
        :return: void.
        '''
        page_num = 0
        page_limit=min(100, math.ceil(total_num/50))
        print('Page Limit:', page_limit)
        previous_element = None

        while page_num < page_limit:
            try:
                print(self.univ_name, 'Page', page_num + 1)
                if page_num == 0:
                    time.sleep(0)
                else:
                    self.wait.until(EC.staleness_of(previous_element))
                
                # Key
                time.sleep(1)
                self.webdriver.find_element_by_xpath('//*[@name="checkAll"]').click()  # 全选所有文献

                # 如果第一篇文章仍然未被选中，则重新选一次
                try:
                    checkbox = self.webdriver.find_element_by_id('label_1_1')
                except NoSuchElementException:
                    break
                if not checkbox.is_selected():
                    self.webdriver.find_element_by_xpath('//*[@name="checkAll"]').click()

                page_num += 1
                previous_element = self.webdriver.find_element_by_id("list_div_aa_1")
                if page_num%10==0 and page_num!=0: #每十页导出一次
                    self.ExplorePub()
                if page_num<page_limit:
                    try:
                        self.Goto_next()
                    except NoSuchElementException:
                        self.ExplorePub()
                        break

            except StaleElementReferenceException:
                print('stale')
                time.sleep(2)

        if page_limit%10!=0:#最末页导出一次
            self.ExplorePub()

    
    def ExplorePub(self):
        '''
        Download metadata in NoteExpress or RefWorks.
        :return:
        '''
        while True:
            try:
                self.webdriver.find_element_by_xpath('//*[@onclick="exportMore(this)"]').click()  # 导出文献

                try:
                    self.webdriver.switch_to.window(self.webdriver.window_handles[1])  # 切换到新窗口
                except IndexError:
                    self.webdriver.find_element_by_xpath('//*[@id="tooltip_001"]/span').click()
                    break

                old_element = self.webdriver.find_element_by_xpath('//*[@id="tagContent0"]/p[1]')
                self.webdriver.find_element_by_link_text("RefWorks").click()  # 选择下载格式
                self.wait.until(EC.invisibility_of_element(old_element))
                self.webdriver.find_element_by_xpath('//*[@onclick="exportTxt();"]').click()  # 下载数据
                self.webdriver.close()#关闭当前窗口
                self.webdriver.switch_to.window(self.webdriver.window_handles[0])
                self.webdriver.find_element_by_xpath('//*[@name="deleteAll"]').click()  # 清楚所有文献记录
                break
            except TimeoutException:
                self.webdriver.close()  # 关闭当前窗口
                self.webdriver.switch_to.window(self.webdriver.window_handles[0])
                print('TimeoutException')
                