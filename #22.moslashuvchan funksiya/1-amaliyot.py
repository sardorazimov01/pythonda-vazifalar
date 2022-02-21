# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 17:32:47 2022

@author: User
"""


def multiply(*sonlar):
    kopaytma = 1
    for son in sonlar:
        kopaytma *= son
    return kopaytma


print(multiply(4, 5, 6))