# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 17:26:47 2022

@author: User
"""


def katta_harf(matnlar):
    for i in range(len(matnlar)):
        matnlar[i] = matnlar[i].title()


ismlar = ["ali", "vali", "hasan", "husan"]
katta_harf(ismlar)
print(ismlar)