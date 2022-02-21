# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 17:35:59 2022

@author: functions

    Azimov_Sardorbek
    
"""

def talaba_info(ism, familiya, **kwargs):
    kwargs["ism"] = ism
    kwargs["familiya"] = familiya
    return kwargs


talaba = talaba_info("olim", "olimov", tyil=1995, fakultet="IT", yonalish="AT")

print(talaba)   