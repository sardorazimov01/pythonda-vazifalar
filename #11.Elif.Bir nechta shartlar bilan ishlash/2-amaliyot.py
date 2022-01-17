# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 14:57:24 2022

@author: User
"""

yosh = int(input("yoshingizni kiriting: "))
if yosh >=4 or yosh >=60:
    narx = "bepul"
if yosh <=18 :
    narx= 5000
if yosh >18:
    narx=10000
print(f"sizga kirish {narx}")
