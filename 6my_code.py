"""
M6 Kirjoita funktio, joka palauttaa kahden vektorin välisen kulman
radiaaneina.

Kulma voidaan laskea vektorien pituuksien (normi, uusi kalvo 153) ja pistetulon avulla

cos f = [ (x.y) / (||x||*||y||) ] => f = acos[...]

"""

import sys
import time

import numpy as np

def angle_between(a, b):
    normi_a=np.linalg.norm(a)
    normi_b=np.linalg.norm(b)
    pistetulo = np.dot(a, b)
    # 5.385..  5.385..  25 
   # print(f"normi_a {normi_a} , normi_b {normi_b} , pistetulo {pistetulo}" )
    kulma_rad=np.arccos( (pistetulo) / (normi_a * normi_b)  )
    # 0.862..  0.5314.. (rad)
   # print(f"cos f {(pistetulo)/(normi_a*normi_b) } , kulma arcos f {kulma_rad} (rad)" )
    
    return kulma_rad

a=np.array([2,3,4]) 
b=np.array([4,3,2])

#a=np.array([1,2,3]) 
#b=np.array([-2,1,0])

#print("Kulma radiaaneina: ", angle_between(a,b))  # 0.5314 , n. 30 astetta