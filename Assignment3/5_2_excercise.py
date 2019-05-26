# -*- coding: utf-8 -*-
"""
Created on Fri May 24 17:50:19 2019

@author: akmil
"""

'''
Exercise 2: Write another program that prompts for a list of numbers
as above and at the end prints out both the maximum and minimum of
the numbers instead of the average.
'''

numbers = []
total = 0
while True:
    try:
        line = input("Enter a number: ")
        if line == 'done':
            break
        else:
            line = float(line)
            numbers.append(line)
    except:
        print("Invalid data.")
        continue

for i in numbers:
    total += i

print(numbers)
print(f"total =  {total}")
count = len(numbers)
print(f"count = {count}")
minimum = min(numbers)
print(f"min = {minimum}")
maximum = max(numbers)
print(f"max = {maximum}")