# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 14:24:45 2019

@author: akmil
"""

'''
Exercise 2: Write a program to look for lines of the form:
New Revision: 39772
Extract the number from each of the lines using a regular expression
and the findall() method. Compute the average of the numbers and
print out the average.
Enter file:mbox.txt
38444.0323119
Enter file:mbox-short.txt
39756.9259259
'''

import re

filename = input('Enter a filename: ')
count = 0
lst = list()
total = 0

with open(filename, 'r') as f:
    for line in f:
        line = line.rstrip()
        if re.search('New Revision: [0-9]+', line):
            total += int(list.pop(re.findall('New Revision: ([0-9]+)', line)))
            count += 1
        else :
            continue
print(f"Revision avg: {round(total/count, 7)}")
