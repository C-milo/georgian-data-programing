# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 13:59:51 2019

@author: akmil
"""
'''
Exercise 2: Change your socket program so that it counts the number
of characters it has received and stops displaying any text after it has
shown 3000 characters. The program should retrieve the entire document and count 
the total number of characters and display the count
of the number of characters at the end of the document.
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
count = 0

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    if (len(data) + count) > 3000:
        difference = (count + len(data)) - 3000
        count += len(data)-difference
        print(data[:len(data)-difference].decode(),end='')
        break

    count += len(data)
    print(f'\n{len(data)}, {count}')
    print(data.decode(),end='')
 
print(f"\n\nThe data received has {count} characters")

mysock.close()