# -*- coding: utf-8 -*-
"""
Created on Fri May 24 18:11:24 2019

@author: akmil
"""
'''
Exercise 2: Write a program to prompt for a file name, and then read
through the file and look for lines of the form:
X-DSPAM-Confidence: 0.8475
When you encounter a line that starts with “X-DSPAM-Confidence:”
pull apart the line to extract the floating-point number on the line.
Count these lines and then compute the total of the spam confidence
values from these lines. When you reach the end of the file, print out
the average spam confidence.
90 CHAPTER 7. FILES
Enter the file name: mbox.txt
Average spam confidence: 0.894128046745
Enter the file name: mbox-short.txt
Average spam confidence: 0.750718518519
Test your file on the mbox.txt and mbox-short.txt files.
'''

def average(lst):
    total = 0
    for a in lst:
        a = float(a)
        total += a
    return total/len(lst)
    

filename = input('Enter exact name of the file: ')
confidence = []

try:
    with open(filename, 'r') as file:
        for l in file:
            l = l.rstrip()
            if l.find('X-DSPAM-Confidence:') == -1: 
                continue
            else:    
                index = l.find(':')
                confidence.append(l[index+2:])
        
except:
    print('Could not read or find the file.')

print(f'Count: {len(confidence)}')
print(f'Average span confidence: {average(confidence)}')
        
    