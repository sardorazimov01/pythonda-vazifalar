# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 17:03:37 2022

@author: functions

    Azimov_Sardorbek

"""

                # 7-amaliyot
def bolinish_alomatlari(son):
    for n in range(2, 11):
        if not son % n:
            print(f"{son} {n} ga qoldiqsiz bo'linadi")


bolinish_alomatlari(20)
