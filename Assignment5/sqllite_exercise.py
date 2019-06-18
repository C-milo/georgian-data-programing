# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 19:39:15 2019

@author: Nuthan
"""

'''
Using Python and SQLite (or SQL server if you desire) create a groups database
Create two tables one that contains the names and IDs of your group members and one that contains course names and course IDs
Create a one to many relationship between the two tables that show which students are in each course
'''

import sqlite3

try:
    conn = sqlite3.connect('testdata.db')
    conn.execute("PRAGMA foreign_keys = ON")
except Error as e:
    print(e)
    exit()

cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS COURSE')
cur.execute('CREATE TABLE COURSE(\
                course_id integer PRIMARY KEY,\
                course_name text NOT NULL)')

cur.execute('DROP TABLE IF EXISTS STUDENT')
cur.execute('CREATE TABLE STUDENT(\
                student_id integer PRIMARY KEY,\
                Student_name text NOT NULL,\
                course1 integer,\
                course2 integer,\
                course3 integer,\
                course4 integer,\
                course5 integer,\
                course6 integer,\
                FOREIGN KEY (course1)\
                REFERENCES course(course_id) ON DELETE SET NULL ON UPDATE CASCADE\
                FOREIGN KEY (course2)\
                REFERENCES course(course_id) ON DELETE SET NULL ON UPDATE CASCADE\
                FOREIGN KEY (course3)\
                REFERENCES course(course_id) ON DELETE SET NULL ON UPDATE CASCADE\
                FOREIGN KEY (course4)\
                REFERENCES course(course_id) ON DELETE SET NULL ON UPDATE CASCADE\
                FOREIGN KEY (course5)\
                REFERENCES courses(course_id) ON DELETE SET NULL ON UPDATE CASCADE\
                FOREIGN KEY (course6)\
                REFERENCES course(course_id) ON DELETE SET NULL ON UPDATE CASCADE)')

cur.execute('INSERT INTO course (course_id, course_name) VALUES(?, ?)', (1, 'Data Programming'))
cur.execute('INSERT INTO course (course_id, course_name) VALUES(?, ?)', (2, 'Data Manipulation Techniques'))
cur.execute('INSERT INTO course (course_id, course_name) VALUES(?, ?)', (3, 'Data Systems Architecture'))
cur.execute('INSERT INTO course (course_id, course_name) VALUES(?, ?)', (4, 'Business Process'))
cur.execute('INSERT INTO course (course_id, course_name) VALUES(?, ?)', (5, 'Math for Data Analytics'))
cur.execute('INSERT INTO course (course_id, course_name) VALUES(?, ?)', (6, 'Information Encoding Standards'))

cur.execute('INSERT INTO student (student_id, student_name, course1, course2)\
                    VALUES (?, ?, ?, ?)', (1, 'Nuthan', 1, 2))
cur.execute('INSERT INTO student (student_id, student_name, course_id, course2)\
                    VALUES (?, ?, ?, ?)', (2, 'Reyhan', 3, 4))
cur.execute('INSERT INTO student (student_id, student_name, course_id)\
                    VALUES (?, ?, ?)', (3, 'Camilo', 5))

conn.commit()

cur.execute('SELECT course.name, student.student_id, student.student_name\
                FROM student\
                INNER JOIN course on course.course_id = student.course1 OR\
                                        course.course_id = student.course2 OR\
                                        course.course_id = student.course3 OR\
                                        course.course_id = student.course4 OR\
                                        course.course_id = student.course5 OR\
                                        course.course_id = student.course6\
                    ORDER BY course.course_name')

rows = cur.fetchall()
cur.close()

for row in rows:
    print(row)