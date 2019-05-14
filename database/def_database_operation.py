# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 15:49:55 2019

@author: Shubham
"""

import sqlite3

def mycon(x):
    con3=sqlite3.connect(x)
    return con3
mycon('test2.db')

def create_table(x,y):
    m=mycon(x)
    cur=m.cursor()
    cur.execute('create table'+y+'(empno INTEGER, empname TEXT')
    return cur
create_table('test2.db','employee')

def insert(x,y,z):
    