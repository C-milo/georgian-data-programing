# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 17:54:57 2019

@author: akmil
"""

'''
Create an iPython notebook, answer the following question and upload the notebook.
1)Using python and mySQL create database called World with one table called Countries.
2)The table will have 5 attributes, Name, Continent, Area, Population and GDP
3)Populate (manually is fine, you don't need to import it) the table with data in the text file sql.txt 
4) A country is big if it has an area of bigger than 3 million square km or a population of more than 25 
million. Write a SQL solution to output big countries' name, population and area.
'''

import sqlite3

conn = sqlite3.connect('World.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Countries')
cur.execute('CREATE TABLE Countries (name TEXT, continent TEXT, area, INTEGER, population INTEGER, gdp INTEGER)')

cur.execute('INSERT INTO Countries (name, continent, area, population, gdp) VALUES (?,?,?,?,?)', ('Afghanistan', 'Asia', 652230, 25500100, 20343000))