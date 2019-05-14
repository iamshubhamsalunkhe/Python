# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 14:55:19 2019

@author: Shubham
"""

import re
input_str = "Box A contains 3 red and 5 White balls, Box B contains 3 red and 8 blue balls"

result = re.sub(r'\d+' , '',input_str)

print(result)
