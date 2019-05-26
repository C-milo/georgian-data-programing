# -*- coding: utf-8 -*-
"""
Created on Sat May 25 17:04:09 2019

@author: akmil
"""
'''
Exercise 4: Add code to the above program to figure out who has the
most messages in the file. After all the data has been read and the dictionary has been created, 
look through the dictionary using a maximum
loop (see Chapter 5: Maximum and minimum loops) to find who has
the most messages and print how many messages the person has.
Enter a file name: mbox-short.txt
cwen@iupui.edu 5
Enter a file name: mbox.txt
zqian@umich.edu 195
'''

def maximum(d):
    count = 0
    for key in d:
        if  d[key] > count:
            count = d[key]
            name = key
    print(f"{name}: {count}")
    

filename = input('Enter a file name: ')
count = dict()

with open(filename, 'r') as f:
    for line in f:
        line.rstrip()
        if line.startswith('From '):
            word = line.split()
            if word[1] not in count:
                count[word[1]] = 1
            else:
                count[word[1]] += 1

print(count)
print('\nMost messages:')
maximum(count)