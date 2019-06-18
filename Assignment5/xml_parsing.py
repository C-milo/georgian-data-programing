# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 15:00:16 2019

@author: akmil
"""

'''
Assignment 5 Part 1
Click this link to get the XML and JSON files from Toronto Open Data for Festivals and Events 
link: https://www.toronto.ca/city-government/data-research-maps/open-data/open-data-catalogue/#21dd820d-dc7f-73d5-a6f0-6368b70a1b6f
For the XML file get a list of all data attributes and print them. Then print the first 5 calEvent Nodes
For the JSON file get a list of Keys and print them. Then print the last 5 JSON calEvent Objects 
'''

import xml.etree.ElementTree as ET


tree = ET.parse('Festivals_and_Events_v9_fromArchivedb.xml')
lst = tree.findall('viewentry/entrydata')
attributes = list()
count = 0

print('Attributes list: ')
for item in lst: 
    if item.get('name') not in attributes:
        attributes.append(item.get('name'))
    else:
        continue

for i in attributes:
    print(f'{i}')

print(f'Total attributes count = {len(attributes)}\n')
print('First 5 Event Nodes:\n')
for item in lst:
    if item.get('name') == 'EventName' and count <= 5:
        count += 1
        try:
            print('Event: ', item.find('text').text)
        except:
            print('No Available information for {item}')
    else:
        continue
#    print('Name', item.find('name').text)
#    print('Id', item.find('id').text)
#    print('Attribute', item.get("x"))    
#    print('Event name:', tree.find('EventName').text)
#print('Phone:', tree.find('phone').text)
#print('Attr:', tree.find('email').get('hide'))