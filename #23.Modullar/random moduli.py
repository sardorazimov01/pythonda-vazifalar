# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 12:32:53 2022

@author: Sardorbek

     random moduli
     
"""

import random as r # random modulini r deb chaqirayapmiz

son = r.randint(0,100) # 0 va 100 oralig'ida tasodifiy son
print(son)


ismlar = ['olim','anvar','hasan','husan']
ism = r.choice(ismlar) # ismlar dan tasodifiy ism tanlaymiz
print(ism)
print(r.choice(ism)) # ismdan tasodifiy harf tanlaymiz

x = list(range(0,51,5))
print(x)
print(r.choice(x))


x = list(range(11))
print(x)
r.shuffle(x)
print(x)