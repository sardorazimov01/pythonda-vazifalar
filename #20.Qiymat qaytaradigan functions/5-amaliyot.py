# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 16:47:14 2022

@author: User
"""


def tub_sonlar_top(min, max):
    tub_sonlar = []
    for n in range(min, max + 1):
        tub = True
        if n == 1:
            tub = False
        elif n == 2:
            tub = True
        else:
            for x in range(2, n):
                if n % x == 0:
                    tub = False
        if tub:
            tub_sonlar.append(n)

    return tub_sonlar


a = tub_sonlar_top(7, 7777)
print(a)
