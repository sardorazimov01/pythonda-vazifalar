# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 16:42:49 2022


@author: functions

Azimov_Sardorbek


"""


def kattasi_top(son1,son2):
    """2-ta sonning katta yoki tengligini topadigan funksiya"""
    if son1<son2:
        print(f"{son2} katta")
    elif son1>son2:
        print(f"{son1} katta")    
    else:
        print("teng")
        
        
kattasi_top(77, 77)
        


