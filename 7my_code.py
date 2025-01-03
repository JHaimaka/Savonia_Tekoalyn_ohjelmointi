"""
M7 
Kirjoita funktio, joka palauttaa annetun vektorin suuntaisen
yksikkövektorin. Eli normi (pituus) on 1 ja osoittaa samaan suuntaan.
Esim. uusi kalvo s. 159
x = [9 2 -7], ||x||=sqrt(16465)=128.31 , xh=1/sqrt(16465)*x = 

"""

import sys
import time
import numpy as np

def unit(a):
    normi_a=np.linalg.norm(a)
    #print(f"normi_a {normi_a}")  # 11.57..
    return a / normi_a


#a=np.array([9,2,-7])

#print(f"a: {a} yksikkövektori on {unit(a)}") # [0.777 0.172 -0.604]