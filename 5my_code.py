import sys
import time
import numpy as np


"""
Kirjoita funktio, joka tarkastaa onko kaksi vektoria toisiaan
vastaan kohtisuorassa. Funktio palauttaa True tai False.

Eli vektorien pistetulon tulee olla nolla x . y = 0
HUOM ! vektorien oltava saman kokoisia
a=[2,3,4], b=[5,6,7] ; a.b = 56
a=[1,2,3] ja b=[-2,1,0] ; a.b = 0
"""

def is_orthogonal(a, b):
    pistetulo = np.dot(a, b)
    if pistetulo == 0:
        return True
    return False

#a=np.array([2,3,4]) 
#b=np.array([5,6,7])

#a=np.array([1,2,3]) 
#b=np.array([-2,1,0])
#pistetulo = np.dot(a, b)
#print("Pistetulo: ", pistetulo)
#print("Pistetulo on = 0: ", is_orthogonal(a,b))