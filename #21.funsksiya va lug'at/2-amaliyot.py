# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 17:27:10 2022

@author: User
"""

def katta_harf(matnlar):
    matnlar = matnlar[:]
    for i in range(len(matnlar)):
        matnlar[i] = matnlar[i].title()
    return matnlar


ismlar = ["ali", "vali", "hasan", "husan"]
yangi_ismlar = katta_harf(ismlar)
print(ismlar)
print(yangi_ismlar)