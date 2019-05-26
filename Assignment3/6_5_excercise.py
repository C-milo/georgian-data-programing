# -*- coding: utf-8 -*-
"""
Created on Fri May 24 17:54:02 2019

@author: akmil
"""

'''
Exercise 5: Take the following Python code that stores a string:
str = 'X-DSPAM-Confidence:0.8475'
Use find and string slicing to extract the portion of the string after the
colon character and then use the float function to convert the extracted
string into a floating point number.
'''

str = 'X-DSPAM-Confidence:0.8475'
index =  str.find(":")
number = float(str[index+1:])
print(number)
print(type(number))
