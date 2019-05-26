# -*- coding: utf-8 -*-
"""
Created on Sat May 25 16:41:40 2019

@author: akmil
"""
'''
Exercise 5: Write a program to read through the mail box data and
when you find line that starts with “From”, you will split the line into
words using the split function. We are interested in who sent the
message, which is the second word on the From line.106 CHAPTER 8. LISTS
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
You will parse the From line and print out the second word for each
From line, then you will also count the number of From (not From:)
lines and print out a count at the end. This is a good sample output
with a few lines removed:
python fromcount.py
Enter a file name: mbox-short.txt
stephen.marquard@uct.ac.za
louis@media.berkeley.edu
zqian@umich.edu
[...some output removed...]
ray@media.berkeley.edu
cwen@iupui.edu
cwen@iupui.edu
cwen@iupui.edu
There were 27 lines in the file with From as the first word
'''
filename = input('Enter name of the file: ')
count = 0

with open(filename, 'r') as f:
    for line in f:
        line.rstrip()
        if line.startswith('From '):
            words = line.split()
            print(words[1])
            count += 1
        
print(f'There were {count} lines in the file with From as the first word.')
            
    