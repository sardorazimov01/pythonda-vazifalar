# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 16:15:17 2022

@author: User
"""

son=int(input("istalgan son kiriting: "))
for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bulinadi")
    