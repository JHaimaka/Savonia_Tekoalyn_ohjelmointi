"""
lue tiedosto m4in.npz ja talleta siitä taulukko b tiedostoon m4out.npy
"""

import numpy as np

#file_load_a='a.npy'
file_load_b='m4in.npz'
file_save='m4out.npy'

# a1=np.load(file_load_a)  # 3 x 4
b1_sisalto=np.load(file_load_b)  # 
#print(b1_sisalto['b']) # 3 x 4 matriisi
np.save(file_save, b1_sisalto['b'])

#np.savez(file_save, a=a1, b=b1)

#a1=np.array([1, 2, 3])

#print(a1)
#print("")
#rivi = a1.shape[0]
#sarake = a1.shape[1]
#print(f"rivi x sarake : {rivi} x {sarake}")
#a1[0,0]=1
#a1[rivi-1,sarake-1]=-1  # oikea alakulma 3 x 4 matriisissa
#print(a1)
#np.save(file_save, a1)

"""
filename='np_example_04.npz'

a1=np.array([0.1, 0.4, 0.4], dtype=np.float64)
a2=np.array(['a', 'b', 'c', 'd'])
z=np.array([0, 3, 8])
np.savez(filename, my_named_parameter=a1, a2=a2, z=z)


a1=np.array([[0.1,  0.4,  0.4],
             [0.0,  1.0, -1.0]], dtype=np.float64)

print('Vasen ylakulma on', a1[0, 0])
print('Oikea alakulma on', a1[1, 2])
print('Ensimmainen sarake', a1[:, 0])
print('Toinen rivi', a1[1, :])
"""