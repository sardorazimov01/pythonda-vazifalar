# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 11:11:41 2022

@author: NESTING

# =============================================================================
#            Azimov Sardorbek...           $
# =============================================================================
           
"""
# =============================================================================
#                                      # 1-amaliyot va 2-amaliyot          $
# =============================================================================
# # 1.Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi ma'lumotlarni lug'at
#  # ko'rinishida saqlang. Lug'atlarni bitta ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.
#                             


# ilm0={
#       'ism':'aburayhon beruniy',
#       'kasb':"Matematik",
#       "t_yil":1789,
#       'olgan_yil':2021,
#       }                             
# ilm1={
#       'ism':'azimov sardorbek',
#       'kasb':'buyuk programist',
#       't_yil':2007,
#       }
# ilm2 = {
#         'ism':'zahiriddin muhammad bobur',
#         'kasb':'astranom',
#         't_yil':1789,
#         'olgan_yil':2000,
#             }
# ilmlar=[ilm0,ilm1,ilm2]
# for ilm in ilmlar:
#     print(f"{ilm['ism'].title()}  kasbi  {ilm['kasb'].title()}   {ilm['t_yil']}-da tugilgan")
    

# =============================================================================
#                            # 2-amaliyot       $
# =============================================================================
# # 2.Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing.
# # For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring.


# ilm0={
#       'ism':'aburayhon beruniy',
#       'kasb':"Matematik",
#       "t_yil":1789,
#       'olgan_yil':2021,
#       'asar':'tibbiyot ilmi'
#       }                             
# ilm1={
#       'ism':'azimov sardorbek',
#       'kasb':'buyuk programist',
#       't_yil':2007,
#       'asar':'dasturlash asoslari     $'
#       }
# ilm2 = {
#         'ism':'zahiriddin muhammad bobur',
#         'kasb':'astranom',
#         't_yil':1789,
#         'olgan_yil':2000,
#         "asar":'astranom'
#             }
# ilmlar=[ilm0,ilm1,ilm2]
# for ilm in ilmlar:
#     print(f"{ilm['ism'].title()}ning  mashhur asari {ilm['asar'].title()}")

# =============================================================================
#                         # 3-amaliyot          $
# =============================================================================
# # 3.Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang. Do'stingiz ismi kalit, 
# # uning sevimli kinolarini esa ro'yxat ko'rinishida lug'artga saqlang.  Natijani konsolga chiqaring.
#                   
# kinolar = {
#     'umar': ['sayfuloo','buyuk devor'],
#     'sardor':['spyder no way home','qizil qoya'],
#     "nurbek":['tor5','avengers']
#     }

# for ism, kinolar in kinolar.items():
#     print(f"\n{ism.title()}ning sevimli kinolari:")
#     for kino in kinolar:
#         print(kino.title())
    
    
# =============================================================================
# #                      # 4-amaliyot             $
# =============================================================================
# # 4.Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida ma'lumotlarni 
# # lug'at ko'rinishida saqlang. Har bir davlat haqida ma'lumotni konsolga chiqaring.


# davlatlar = {
#     "o'zbekiston":{'poytaxt':"toshkent",
#                    'maydon':448978,
#                    'aholi':33_000_000,
#                    'pul birligi':"so'm"
#                    },
#     "rossiya":{'poytaxt':"moskva",
#                    'maydon':17_098_246,
#                    'aholi':144_000_000,
#                    'pul birligi':"rubl"
#                    },
#     "aqsh":{'poytaxt':"vashington",
#                    'maydon':9_631_418,
#                    'aholi':327_000_000,
#                    'pul birligi':"dollar"},
#     "malayziya":{'poytaxt':"kuala-lumpur",
#                    'maydon':329750,
#                    'aholi':25_000_000,
#                    'pul birligi':"rinngit"}
#     }

# for davlat, info in davlatlar.items():
#     if davlat.lower()=='aqsh':
#         davlat = davlat.upper()
#     else:
#         davlat = davlat.capitalize()
#     print(f"\n{davlat}ning poytaxti {info['poytaxt'].title()}"
#           f"\nHududi: {info['maydon']} kv.km"
#           f"\nAholisi: {info['aholi']}"
#           f"\nPul birligi: {info['pul birligi']}")


# =============================================================================
# #                                   # 5-amaliyot    $
# =============================================================================
# # 5.Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas, foydalanuvchi 
# # so'ragan davlat haqida ma'lumot bering. Agar davlat sizning lug'atingizda mavjud bo'lmasa,
#  # "Bizda bu davlat haqida ma'lumot yo'q" degan xabarni chiqaring.
 
 
 
 
# davlatlar = {
#     "o'zbekiston":{'poytaxt':"toshkent",
#                     'maydon':448978,
#                     'aholi':33_000_000,
#                     'pul birligi':"so'm"
#                     },
#     "rossiya":{'poytaxt':"moskva",
#                     'maydon':17_098_246,
#                     'aholi':144_000_000,
#                     'pul birligi':"rubl"
#                     },
#     "aqsh":{'poytaxt':"vashington",
#                     'maydon':9_631_418,
#                     'aholi':327_000_000,
#                     'pul birligi':"dollar"},
#     "malayziya":{'poytaxt':"kuala-lumpur",
#                     'maydon':329750,
#                     'aholi':25_000_000,
#                     'pul birligi':"rinngit"}
#     }

# davlat = input('Davlat nomini kiriting: ').lower()
# if davlat in davlatlar:
#     info = davlatlar[davlat]
#     print(f"\n{davlat.capitalize()}ning poytaxti {info['poytaxt'].title()}"
#           f"\nHududi: {info['maydon']} kv.km"
#           f"\nAholisi: {info['aholi']}"
#           f"\nPul birligi: {info['pul birligi']}")
# else:
#     print("Bizda bu davlat haqida ma'lumot mavjud emas")
 
 
 
 
 
 
 
 