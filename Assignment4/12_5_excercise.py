# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 22:07:17 2019

@author: akmil
"""

'''
Exercise 5: (Advanced) Change the socket program so that it only shows
data after the headers and a blank line have been received. Remember
that recv receives characters (newlines and all), not lines.
'''

import socket

url_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url_socket.connect(('data.pr4e.org', 80))
url_cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
url_socket.send(url_cmd)


url_data = url_socket.recv(512)
url_message = url_data.decode()
url_header = url_message.find('\r\n\r\n') + 4

print(url_message[url_header:])

while True:
    url_data = url_socket.recv(512)
    if not url_data: break
    print(url_data.decode())

url_socket.close()