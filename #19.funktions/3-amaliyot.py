# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 16:37:53 2022

@author: User
"""



def juft_toq_info(son):
    """Kiritilgan son juft yoki toqligini konsolga chiqaruvchi funksiya"""
    if son % 2:
        print(f"{son}-toq son")
    else:
        print(f"{son}-juft son")

juft_toq_info(7)