# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:06:54 2019

@author: akmil
"""

'''
Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving
the document from a URL, (2) displaying up to 3000 characters, and
(3) counting the overall number of characters in the document. Don’t
worry about the headers for this exercise, simply show the first 3000
characters of the document contents.
'''


import urllib
import re

def get_url(userurl):    
    clean_url = list.pop(re.findall('^http://(.+)/',userurl))
    return clean_url

userurl = input('Enter a URL to connect: ')

try:
    clean_url = get_url(userurl)
except:
    print('This is not a valid URL it must start with http://')

info = urllib.request.urlopen(userurl).read(3000)
print(info.decode())
print(f'\n\n{len(info)} characters were printed.')