"""
TekoalynOhjelmointi.pdf sivu 67, 
luento s .73 tehtavaympariston_kaytto 3:16 

M1
luo taulukko a , 3 riviä, 4 saraketta , kaikkien arvoksi 0.
Tallenna taulukko a tiedostoon m1out.npy

\assignments\01_numpy
src -kansio
 * my_code.py , tehtäväpohja jota editoidaan
tests -kansio
test.py

1. Tallenna \01_numpy\src\my-code.py tiedostoon ratkaisu
2. aja terminaalissa \01_numpy\test.py
"""
import numpy as np
a=np.zeros((3, 4))
#print(a)
np.save('m1out.npy', a)

