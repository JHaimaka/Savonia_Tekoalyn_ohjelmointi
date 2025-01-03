"""
 Kirjoita funktio, joka palauttaa (x·y)/(y·y) * y , kun x ja y annetaan
funktion parametreina. Tätä kutsutaan vektorin x projektioksi
y:lle (suorassa kulmassa).
uusi kalvo s. 174
esim. x=[1 1/2], y=[2/3 3/2] => Pyx= -9/291[2/3 3/2]  = [0.35047548 0.7886487 ]
"""

import sys
import time
import numpy as np

def project(x, y):
    pistetulo_xy = np.dot(x, y)
    pistetulo_yy = np.dot(y, y)
    return (pistetulo_xy / pistetulo_yy * y) # palauttaa (x·y)/(y·y) * y


# x=np.array([1, 1/2])
# y=np.array([0.6666, 3/2])
# print(f"Projektio: Pyx {project(x,y)}") # [0.35047548 0.7886487 ]
