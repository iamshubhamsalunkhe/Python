# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 14:52:56 2019

@author: Shubham
"""
#nested functions
def gm():
    print("Good Morning")
def hello():
    gm()
    print("HELLO")
def welcome():
    hello()
    print("Welcome")
welcome()