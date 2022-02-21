# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 17:31:00 2022

@author: User
"""


def bahola(ismlar):
    baholar = {}
    for ism in ismlar:
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism] = baho
    return baholar


baholar = bahola(talabalar)
print(baholar)
print(talabalar)