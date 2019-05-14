# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 15:33:59 2019

@author: Shubham
"""
import numpy as np
import pandas as pd

names=['United States','Austraila','Japan','INDIA','Russia','Morroco','Egypt']

dr=[True,False,True,False,True,False,False]

cpc=[111,55,444,666,88,11,25]


my_dict={"country":names,"driver_right":dr,"car_per_cap":cpc}

print(my_dict)
print(my_dict.keys())
print(my_dict.values())
print(pd.DataFrame(my_dict))

print(type(my_dict))

cars=pd.DataFrame(my_dict)

print(cars)
print(type(cars))


row_labels=['US','AUS','JAP',"IN",'RU','MOR','EG']

cars.index=row_labels

print(cars)

print(cars['country'][0])

print(cars[0:3])
print(cars[2:5])


sel =cars[cars['driver_right']==False]
print(sel)


sel3=cars['driver_right']==True #when true is not consider in list it will not take every column just specified one it will take
print(sel3)

sel1=cars['car_per_cap']>500
print(sel1)

sel2=cars[cars['car_per_cap']>500]
print(sel2)



medium=cars[np.logical_and(cars['car_per_cap']>=100,cars['car_per_cap']<=500)]
print(medium)
print(cars.shape)
print(cars.head(5))
print(cars.tail(3))
print(cars.describe())
print(cars.dtypes)
print(cars.info)













