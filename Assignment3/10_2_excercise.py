# -*- coding: utf-8 -*-
"""
Created on Mon May 27 11:50:40 2019

@author: akmil
"""

'''
Exercise 2: This program counts the distribution of the hour of the day
for each of the messages. You can pull the hour from the “From” line
by finding the time string and then splitting that string into parts using
the colon character. Once you have accumulated the counts for each
hour, print out the counts, one per line, sorted by hour as shown below.
python timeofday.py
Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
''' 

filename = input('Enter filename to read: ')
count = dict()

with open(filename, 'r') as f:
    for line in f:
        line.rstrip()
        if line.startswith('From '):
            word = line.split()[5]
            if word[:2] not in count:
                count[word[:2]] = 1
            else:
                count[word[:2]] += 1
        else:
            continue

lst = list()
for key, val in list(count.items()):
    lst.append((key, val))
    
lst.sort()

for key, val in lst:
    print(key, val)
