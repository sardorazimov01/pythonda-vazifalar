# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 15:12:22 2022

@author: User
"""

mahsulotlar= ["olma" ,"o'rik", "shaftoli", "behi"," ananas ","un ","shakar"," yog'"," olxuri"," coca cola"]
savat=[]
for n in range(5):
    savat.append(input(f"{n+1}- mahsulotni kiriting: "))
    for s in savat:
        if s in mahsulotlar:
            print("bizda bu mahsulotlar bor")
        else:
            print('bizda mahsulotlar yo\'q')
            