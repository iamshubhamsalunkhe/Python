# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:00:18 2019

@author: Shubham
"""
from string import maketrans

inttab="aeiou"
outtab="12345"

transtab=maketrans(inttab,outtab)

str1="this is string example...wow!!!"

print(str1.translate(transtab))