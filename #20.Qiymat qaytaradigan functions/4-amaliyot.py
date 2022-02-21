# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 17:19:36 2022

@author: User
"""

def aylana_info(radius, pi=3.14159):
    aylana = {
        "radius": radius,
        "diametr": 2 * radius,
        "perimetr": 2 * radius * pi,
        "yuza": pi * radius ** 2,
    }
    return aylana

a =aylana_info(4)
print(a)