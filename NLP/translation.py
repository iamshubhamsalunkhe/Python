# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 17:40:52 2019

@author: Shubham
"""

from translate import Translator


translator =Translator(to_lang="German")

translation = translator.translator("Good Morning!")

print(translation)