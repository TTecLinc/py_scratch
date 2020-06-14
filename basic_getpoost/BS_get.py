# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 15:35:08 2020

@author: Peilin Yang
"""

from bs4 import BeautifulSoup
import requests

url='http://www.cntour.cn'
strhtml=requests.get(url)

soup=BeautifulSoup(strhtml.text,'lxml')
# The first message :
##main > div > div.mtop.firstMod.clearfix > div.centerBox > ul.newsList > li:nth-child(1) > a

data=soup.select('#main > div > div.mtop.firstMod.clearfix > div.centerBox > ul.newsList > li > a')

for item in data:
    result={
        'title':item.get_text(),
        'link':item.get('href')
        }
    print(result)

import re

# \d is num + is several times
for item in data:
    result_ID={
        'ID':re.findall('\d+', item.get('href'))
        }
    print(result_ID)
    
    