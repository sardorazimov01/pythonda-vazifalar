# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 14:48:47 2022

@author: User
"""

odamlar =[]

a =int(input("Bugun nechta odam bilan suxbatlashdiz?: "))
for n in range(a):
    odamlar.append(input(f"{n+1}-suhbatllashgan odamingiz?:"))
print("Siz bugun "  ,odamlar ,"blan gaplashdingiz")    
        