# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 14:53:55 2022

@author: Sardor

        List_bilan_ishlash.py
        
        
    
"""
## 1. Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. 
## Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring.
                          ## 1-amaliyot
# lugatlar = {
#     'for':"uchun",
#     'string':'matn',
#     'int':'butun son',
#     'float':"o'nlik son",
#     'if':'agar'}
# for lugat,q in sorted(lugatlar.items()):
#     print(lugat.title(),'-',q)
    


## 2. Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni,
## keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring.
               ## 2-amaliyot  va 3-amaliyot

# davlatlar = {
#     'aqsh':'washington',
#     'fransiya':'paris',
#     'angliya':'london',
#     'ozbekiston':'toshkent'
#     }

# # print("Dunyo davlatlari:")
# # for davlat in sorted(davlatlar):
# #     print(davlat.title())
    
# # print("Ularning poytaxtlari:")
# # for q in sorted(davlatlar.values()):
# #     print(q.title())
    
# d =input("istalgan davlat kiriting: ")
# a =d.lower()
# poytaxt = davlatlar.get(a)
# if poytaxt == None:
#     print("bizda bunday daflat yo'q")
# else:
#     print(f"{a.title()}-ning poytaxti {poytaxt.title()}")

#                      # 4-amaliyot
# taomlar = {
#     'osh':15000,
#     'somsa':5000,
#     'gril':20_000,
#     "salot":3000,
#     'manti':10_000
#     }
# print("3 ta taom kiriting")
# buyurtmalar = []
# for n in range(3):
#     buyurtmalar.append(input(f"{n+1}-taomni kiritng:").lower())
    
# for buyurtma in buyurtmalar:
#     if buyurtma in taomlar:
#         print(f"{buyurtma} narxi {taomlar[buyurtma]}")
#     else:
#         print(f"{buyurtma}- bizda bunday taom yuq")
    
      
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    