# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 11:03:23 2022

@author: Sardor__aZimov...           $

mavzu: while tsikle...            $

"""
# # =============================================================================
# #                                    # 1-amaliyot             $
# # =============================================================================
# # 1. Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. 
# #   Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating.
 
 
# kitob = "yaxshi ko'rgan kitoblaringizni kiriting"
# kitob +='(stop orqali toxtating): '

# qiymat = True
# while qiymat:
#     qiymat=input(kitob)
#     if qiymat =='stop':
#         qiymat =False
        
        
# # =============================================================================
# #                                       # 2-amaliyot           $
# # =============================================================================
# # 2.Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm,
# # 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va
# # chipta narhini chiqarsin. Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).     


# print("                      Muzey             ")
# yoshi= 'yoshingiz kiriting'
# yoshi +='(chiqish uchun exit yoki quit deb yozing):'

# while True:
#     qiymat=(input(yoshi))
#     if  qiymat== 'exit' or qiymat== 'quit':
#         break
#     yosh= int(qiymat)
#     if yosh<=7:
#         print('sizga kirish << 2000-som >>')
#     elif  7<yosh<=18:
#         print('sizga kirish << 3000-som >>')
#     elif  18<yosh<=65:
#         print("sizga kirish << 10000-so'm >>")
#     elif yosh>65:
#         print("sizga kirish be pul")
                       

                               
# =============================================================================
#                              # 3-amaliyot       $
# =============================================================================
#    # Quyidagi dasturda bir nechta mantiqiy xatolar bor. Jumladan, xusisiy holatlarda tsikl abadiy qaytarilib qolmoqda. 
#    # Xatolarni to'g'rilay olasizmi?
   
   
# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat=='exit':
#         break
#     elif float(qiymat)<0:
#         continue
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")

    
    
        
    
    

