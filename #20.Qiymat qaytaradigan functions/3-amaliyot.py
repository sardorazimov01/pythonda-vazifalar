# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 17:14:19 2022

@author: functions

      Azimov_Sardorbek
      
"""

def kattasi(x, y, z):
    max = x
    if y >= max:
        max = y
    if z >= max:
        max = z
    return max


a= kattasi(23, 11, 346)
print(a)