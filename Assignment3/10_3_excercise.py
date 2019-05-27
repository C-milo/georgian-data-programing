# -*- coding: utf-8 -*-
"""
Created on Mon May 27 11:59:40 2019

@author: akmil
"""

'''
Exercise 3: Write a program that reads a file and prints the letters
in decreasing order of frequency. Your program should convert all the
input to lower case and only count the letters a-z. Your program should
not count spaces, digits, punctuation, or anything other than the letters
a-z. Find text samples from several different languages and see how
letter frequency varies between languages. Compare your results with
the tables at https://wikipedia.org/wiki/Letter_frequencies.
'''

filename = input('Enter a filename: ')

abc = 'abcdefghijklmnopqrstuvwxyz'
alpha = dict()

with open(filename, 'r', encoding="utf8") as f:
    for line in f:
        line = line.lower()
        for letter in line:
            if letter in abc:
                if letter not in alpha:
                    alpha[letter] = 1
                else:
                    alpha[letter] += 1
            else:
                continue
lst = list()
for key, val in list(alpha.items()):
    lst.append((key, val))
    
lst.sort()

for key, val in lst:
    print(key, val)
                    
            
            