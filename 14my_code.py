"""
M14 (0:28.35)
Muokkaa ohjelmaa, joka opettaa KNN-luokittimen tunnistamaan
käsinkirjoitettuja numeroita (MNIST-aineistosta). Tehtävänäsi
on pienentää aineiston dimensio 32:een. Tavoitteena on saada
vähintään 95% pakatun testiaineiston merkeistä tunnistettua.
Älä muokkaa ohjelmaa muualta kuin rivien 15. . . 25 välistä.
"""


import sys
import time
import numpy as np
from sklearn.decomposition import PCA
#from keras.datasets import mnist # alkuperäinen
from tensorflow.keras.datasets import mnist
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

(train_X, train_Y), (test_X, test_Y) = mnist.load_data()

reduced_N=32

########################################################
#Write your code here

#Set value range -1..1


#Convert figures to vectors

#Compute reduced PCA
#print(f"Train data shape: {train_X.shape}")  # Pitäisi tulostaa (60000, 28, 28)


# Muunna kuvat vektoreiksi (28x28 -> 784 ominaisuutta)
train_X_flattened = train_X.reshape(train_X.shape[0], -1)  # Muodostetaan 1D-vektoriksi jokainen kuva
test_X_flattened = test_X.reshape(test_X.shape[0], -1)  # Muodostetaan 1D-vektoriksi jokainen testikuva

# Normalisoi data [-1, 1] väliin
train_X_normalized = 2 * (train_X_flattened / 255.0) - 1  # Skalaus väliin [-1, 1]
test_X_normalized = 2 * (test_X_flattened / 255.0) - 1  # Skalaus väliin [-1, 1]

# Suorita PCA ja pienennä dimensio haluttuun kokoon (reduced_N)
pca = PCA(n_components=reduced_N)
train_X_packed = pca.fit_transform(train_X_normalized)  # Sovelletaan PCA:ta koulutusdataan
test_X_packed = pca.transform(test_X_normalized)  # Sovelletaan PCA:ta testidataan (käytetään samaa PCA-mallia)

# Tarkistetaan datan kokoonpano
print(f"Train data after PCA shape: {train_X_packed.shape}")
print(f"Test data after PCA shape: {test_X_packed.shape}")


##train_X_packed=... #reduced dimension
##test_X_packed=... #reduced dimension

#End of your code
########################################################
#Do not modify lines below this point!




#Save packed data
print('Save packed data')
np.save('packed_train.npy', train_X_packed)
np.save('packed_test.npy', test_X_packed)

if len(sys.argv)==1:
    #Test quality
    print('Train model')
    model = KNeighborsClassifier(n_neighbors = 11)
    model.fit(train_X_packed, train_Y)

    print('Compute predictions')
    pred = model.predict(test_X_packed)
    acc = accuracy_score(test_Y, pred)

    print('Accuracy =',acc)
