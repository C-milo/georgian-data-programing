# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 18:41:57 2019

@author: akmil
"""

'''
To complete this question create an iPython notebook solve the problem and upload the notebook. 

Attached to this question is a text file containing a single sentence string. Import the text file and print 
its contents.Then you need to reverse the order of characters in each word within the sentence while still preserving 
whitespace and initial word order. String.txt 

Example 1:
Input: "Let's take the programming midterm"
Output: "s'teL ekat eht gnimmargorp mretdim "

Note: In the string, each word is separated by single space and there will not be any extra space in the string.
'''

import re

reverse = str()

with open('String.txt') as f:
    for line in f:
        string = re.findall('[A-Za-z]+', line)
        for w in string:
            reverse += (w[::-1]+ ' ')