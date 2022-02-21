# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 17:22:25 2022

@author: User
"""

def fibonacci(n):
    sonlar = []
    for x in range(n):
        if x == 0 or x == 1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x - 1] + sonlar[x - 2])
    return sonlar


print(fibonacci(777))