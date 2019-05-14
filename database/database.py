# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 14:56:51 2019

@author: akshaf
"""

import sqlite3

con = sqlite3.connect("test.db") #connecting to test.db. If test.db is not present then it will create a db with that name.
cur = con.cursor() # storing data inside a cursor
cur.execute('create table emp(empno INTEGER, empname TEXT)')
cur.execute('insert into emp values(10,"Akshaf")')
cur.execute('insert into emp values(11,"Mulla")')
cur.execute('insert into emp values(12,"irfan")')

cur.execute('create table company(id INT PRIMARY KEY NOT NULL, dept CHAR(50), age INT NOT NULL, address char(50),salary real)')
cur.execute('insert into company values(10,"IT",28,"Thane",50000)')
cur.execute('insert into company values(11,"EX",24,"Mumbai",40000)')
cur.execute('insert into company values(12,"CS",26,"Pune",87000)')

cur.execute('create table department(id INT PRIMARY KEY NOT NULL, dept char(50) NOT NULL, emp_id int not null)')
cur.execute('insert into department values(1,"IT",10)')
cur.execute('insert into department values(2,"EX",11)')
cur.execute('insert into department values(3,"CS",12)')

con.commit()

cur.execute('select * from emp')
f1 = cur.fetchall() # fetching all data
f1

f2 = cur.fetchone() # fetching first row
f2

f3 = cur.fetchmany() # fetching 
f3

cur.execute('select * from company')
f4 = cur.fetchall()
f4

cur.execute('select * from department')
f5 = cur.fetchall()
f5




