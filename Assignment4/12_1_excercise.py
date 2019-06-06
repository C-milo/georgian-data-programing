# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 11:40:07 2019

@author: akmil
"""

'''
Exercise 1: Change the socket program socket1.py to prompt the user
for the URL so it can read any web page. You can use split('/') to
break the URL into its component parts so you can extract the host
name for the socket connect call. Add error checking using try and
except to handle the condition where the user enters an improperly
formatted or non-existent URL.
'''

import socket
import re

def get_url(userurl):    
    clean_url = list.pop(re.findall('^http://(.+)/',userurl))
    return clean_url


userurl = input('Enter a URL to connect: ')

try:
    clean_url = get_url(userurl)
except:
    print('This is not a valid URL it must start with http://')

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((clean_url, 80))
cmd = 'GET '+userurl+' HTTP/1.0\r\n\r\n'
cmd = cmd.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()