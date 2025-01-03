"""
lue taulukko tiedostosta m2in.npy ja aseta indexin (0,0) arvoksi 1
ja oikeaan alakulmaan arvo -1. Talleta muokattu taulukko m2out.npy
[[1. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
 3 x 4
 """
import numpy as np

file_load='m2in.npy'
file_save='m2out.npy'

a1=np.load(file_load)
#a1=np.array([1, 2, 3])

#print(a1)
rivi = a1.shape[0]
sarake = a1.shape[1]
#print(f"rivi x sarake : {rivi} x {sarake}")
a1[0,0]=1
a1[rivi-1,sarake-1]=-1  # oikea alakulma 3 x 4 matriisissa
#print(a1)
np.save(file_save, a1)

"""
a1=np.array([[0.1,  0.4,  0.4],
             [0.0,  1.0, -1.0]], dtype=np.float64)

print('Vasen ylakulma on', a1[0, 0])
print('Oikea alakulma on', a1[1, 2])
print('Ensimmainen sarake', a1[:, 0])
print('Toinen rivi', a1[1, :])
"""
