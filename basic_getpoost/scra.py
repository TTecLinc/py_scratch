# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 14:54:24 2020

@author: Peilin Yang
"""


import requests
import json
'''
url='http://www.cntour.cn'
strhtml=requests.get(url)
print(strhtml.text)
'''
def get_translate_date(word=None):
    url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    Form_data={'i': word,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '15921185535633',
    'sign': 'd62089936d95873d314079947fd7c348',
    'ts': '1592118553563',
    'bv': 'b286f0a34340b928819a6f64492585e8',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_CLICKBUTTON'}
    response = requests.post(url,data=Form_data)
    content = json.loads(response.text)
    print(content)
    print(content['translateResult'][0][0]['tgt'])
    return 0
get_translate_date('-')




