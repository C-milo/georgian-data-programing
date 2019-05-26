# -*- coding: utf-8 -*-
"""
Created on Fri May 24 16:31:39 2019

@author: akmil
"""

'''
Exercise 1: Write a program which repeatedly reads numbers until the
user enters “done”. Once “done” is entered, print out the total, count,
and average of the numbers. If the user enters anything other than a
number, detect their mistake using try and except and print an error
message and skip to the next number.
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
average = total/count
print(f"average = {average}")
