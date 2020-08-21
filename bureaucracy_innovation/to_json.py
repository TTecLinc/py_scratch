# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 14:31:42 2020

@author: Andy Zhao, Peilin Yang 
"""

import re
import json
import os
import numpy as np

def json_data(univ):
    #text to json
    files = os.listdir('pub_data/'+univ)
    for file in files:

        if file != '.DS_Store':
            file_path = 'pub_data/'+univ + '/' + file
            print(file)
            pubs = pub_to_dict(file_path)
            file_name=re.sub(".txt",".json",file)

            file_path = 'pub_json/' + univ
            if not os.path.exists(file_path):
                os.makedirs(file_path)
            with open(file_path+'/'+file_name, 'w+') as f:
                json.dump(pubs, f)

def json_data_unknown(univs,path):
    files = os.listdir(path)
    for file in files:

        if file != '.DS_Store':
            file_path = path +file
            pubs=pub_to_dict(file_path)
            file_name=re.sub(".txt",".json",file)
            #print(file_name)
            file_path='pub_json/'+find_univ(univs,pubs)
            if not os.path.exists(file_path):
                os.makedirs(file_path)
            with open(file_path+'/'+file_name, 'w+') as f:
                json.dump(pubs, f)

def find_univ(univs,pubs):
    univ=[]
    for p in pubs:
        for u in univs:
            if u in p['AD']:
                univ.append(u)
        if len(univ)==1:
            break
    return univ[0]

def pub_to_dict(path):
    #convert each paper to json
    f = open(path, 'r')
    papers = re.split(r'\n\n', f.read())
    pubs=[]

    for paper in papers:
        pub = {}
        lines=re.split(r'\n',paper)
        for line in lines:
            try:
                var_search = re.search(r'(^[A-Z]\w) (.*)', line)
                variance = var_search.group(1)
                value = var_search.group(2)
            except:
                if line.startswith('基金项目'):
                    var_search = re.search(r'(.*):(.*)', line)
                    variance = var_search.group(1)
                    value = var_search.group(2)
                else:
                    if pub.__contains__(variance):
                        value=pub[variance]+line #上一个variance
                    else:
                        value=line

            pub[variance] = value

        if paper.__contains__('RT'):
            pubs.append(pub)
        else:
            pubs[-1].update(pub)

    return pubs

def add_wanfangid(univ):
    #extract WanFang ID and add it back to json
    files = os.listdir('pub_json/'+univ)
    for file in files:
        if file != '.DS_Store':
            with open('pub_json/'+univ+'/'+file, 'r') as f:
                data=json.load(f)

            for paper in data:
                try:
                    try:
                        link =paper['LK']
                    except:
                        link =paper['UL']

                    try:
                        get=re.search(r'http://www.wanfangdata.com.cn/details/detail.do(.*)_type=perio&id=(.*)', link)

                        wangfanid=get.group(2)
                    except:
                        get = re.search(r'http://www.wanfangdata.com.cn/details/detail.do(.*)_type=conference&id=(.*)', link)
                        wangfanid=get.group(2)
                    paper['wangfanid']=wangfanid
                except:
                    print(paper)
            with open('pub_json/'+univ+'/'+file, 'w') as f:
                json.dump(data, f)

def get_only_ids(univ):
    all_ids = {}
    files = os.listdir('pub_json/' + univ)
    duplicating_ids=[]
    for file in files:
        if file != '.DS_Store':
            with open('pub_json/' + univ + '/' + file, 'r') as f:
                data = json.load(f)
                wfid = []
                for paper in data:
                    try:
                        wfid.append(paper['wangfanid'])
                    except:
                        print(paper)
            all_ids[file] = wfid
            duplicating_ids.extend(wfid)
    print(univ,len(duplicating_ids),len(set(duplicating_ids)))
    np.save(univ+'_all_ids.npy', all_ids)

def get_unique(univ):
    files = os.listdir('pub_json/' + univ)
    for file in files:
        if file != '.DS_Store':
            with open('pub_json/' + univ + '/' + file, 'r') as f:
                data = json.load(f)

if __name__ == '__main__':
    univ= "南开大学"
    path="/Users/andyzhao/Downloads/NKU/"

    #json_data_unknown(univs,path)
    #add_wanfangid(univs)
    #get_only_ids(univs[0])
    #get_only_ids(univs[1])
    #get_only_ids(univs[2])


    json_data(univ)

    # convert to json format

    add_wanfangid(univ)
    #add Wanfang ID
    #get_only_ids(univ)

