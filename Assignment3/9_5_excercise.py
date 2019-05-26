# -*- coding: utf-8 -*-
"""
Created on Sat May 25 17:40:55 2019

@author: akmil
"""

'''
Exercise 5: This program records the domain name (instead of the
address) where the message was sent from instead of who the mail came
from (i.e., the whole email address). At the end of the program, print
out the contents of your dictionary.
python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
'''

filename = input('Enter a file name: ')
count = dict()

with open(filename, 'r') as f:
    for line in f:
        line.rstrip()
        if line.startswith('From '):
            word = line.split()
            wemail = word[1]
            index = word[1].find('@')
            domain = wemail[index+1:]
            if domain not in count:
                count[domain] = 1
            else:
                count[domain] += 1

print(count)