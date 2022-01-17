# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 16:28:24 2022

@author: User
"""


mahsulotlar= ["olma" ,"o'rik", "shaftoli", "behi","ananas","un","shakar","yog'"," olxuri","coca cola"]
savat=[]
for n in range(5):
    savat.append(input(f"{n+1}- mahsulotni kiriting: "))
bor_mahsulotlar=[]
mavjud_emas=[]
for mahsulot in savat :
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)
if mavjud_emas:
    print("bizda bu mahsulotlar yo'q")
    for mahsulot in mavjud_emas:
        print(mahsulot)
else:
    print("bizdda bu mahsulotlar bor")
            