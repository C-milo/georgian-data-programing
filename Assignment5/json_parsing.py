# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 11:16:11 2019

@author: akmil
"""

'''
Assignment 5 Part 1
Click this link to get the XML and JSON files from Toronto Open Data for Festivals and Events 
link: https://www.toronto.ca/city-government/data-research-maps/open-data/open-data-catalogue/#21dd820d-dc7f-73d5-a6f0-6368b70a1b6f
For the XML file get a list of all data attributes and print them. Then print the first 5 calEvent Nodes
For the JSON file get a list of Keys and print them. Then print the last 5 JSON calEvent Objects 
'''

import json

key_list = list()

with open('edc_eventcal_APR.json', 'r') as json_file:
    json_file = json.load(json_file)
    print('Total Nodes:', len(json_file))
    for item in json_file[-5:]:
        cal_ev = item['calEvent']
        for keys in cal_ev:
            if keys not in key_list:
                key_list.append(keys)
            if keys == 'eventName':
                print(cal_ev[keys])
            else:
                continue
    print('\nKeys List\n', key_list)
    
            
        
            