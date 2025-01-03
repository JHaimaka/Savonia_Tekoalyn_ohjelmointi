"""
M16 
Tiedosto grading.csv sisältää tiedot opiskelijoiden 3 eri harjoituksesta
saamista pisteistä ja tiedon tentin läpäisemisestä.
- Kustakin harjoituksesta voi saada 0 . . . 6 pistettä.
- Mikäli jonkin sarakkeen arvo on tyhjä, opiskelija ei ole
osallistunut harjoitukseen tai tenttiin. Tällaista opiskelijaa ei tule
huomioida aineistossa.
Esikäsittele aineisto ja opeta sen perusteella SVM jakamaan opiskelijat
kahteen luokkaan tentin läpäisyn perusteella. Jaa aineisto opetus- ja
testiaineistoon haluamallasi tavalla.
Tiedostossa assignments.csv on opiskelijoiden harjoituspisteet.
Tehtävänäsi on ennustaa vähintään 80% opiskelijoista oikea
tenttitulos. Tallenna ennusteet tiedostoon prediction.csv, joka
sisältää opiskelijan nimen 1. sarakkeessa ja ennusteen 2. sarakkeessa.
"""

import pandas 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn import svm

filename1='grading.csv'
train_fraction = 0.8
Y_column='Passed'

#Load data
data=pandas.read_csv(filename1)
print("Read data shape = "+str(data.shape))
print(data)


#################################################
#Your code here
#
#Create a classifier that classifies students


#print("Rivit, joissa on NaN-arvoja:")
#print(data[data.isna().any(axis=1)])
#varmuudeksi poistetaan NaN:t
data = data.dropna()

# Erotetaan piirteet ja luokat
"""
Name,Assignment A,Assignment B,Assignment C,Passed
Karson Burt,1,4,5,TRUE
Izaac Macleod,3,5,0,TRUE
Usama Golden,0,1,0,FALSE
"""
X = data[['Assignment A', 'Assignment B', 'Assignment C']]  # Piirteet
y = data[Y_column]  # Luokat (Passed tai Failed), Y_column='Passed'

# Sekoitetaan data
"""
Ilman sekoitusta data voi olla järjestyksessä, esimerkiksi opiskelijat, 
joilla on korkeat pisteet, saattavat olla datan alussa ja opiskelijat 
vastaavasti joilla on alhaiset pisteet, lopussa. Tämä voi johtaa huonosti 
toimivaan malliin.
"""
X, y = shuffle(X, y, random_state=42)

# Jaetaan data opetus- ja testiaineistoon
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=train_fraction, random_state=42)

# Koulutetaan SVM-luokitin
classifier = svm.SVC(kernel='linear')  # Käytetään lineaarista ydinfunktiota
# SVM yrittää löytää suoran, joka erottaa datapisteet kahteen luokkaan (esim. "Passed" ja "Failed").

# Laske tukivektorit: datapisteet, jotka ovat lähimpänä erotuspintaa
classifier.fit(X_train, y_train)


#
#################################################

#Load real data
filename2='assignments.csv'
data=pandas.read_csv(filename2)
names=data['Name']

#Remove name column
for col in ["Name"]:
    print("Remove "+col)
    data.drop(col, axis=1, inplace=True)
print()

print("Read data shape = "+str(data.shape))
print(data)
predY=classifier.predict(data)

#Create dataframe from numpy data
df = pandas.DataFrame({'Name': names, 'Passed': predY})
print(df)
df.to_csv('prediction.csv', index=False)

