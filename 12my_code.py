"""
M12 Konenäkölaitteisto mittaa kuulantyönnön harjoituksissa kuulan x- ja
y-koordinaattia 50 ms välein. y-koordinaatin 0-taso on kentän pinnan
tasolla. Yhden työnnön esikäsitellyt mittaustulokset on talletettu
tiedostoon mittaus.csv. Tehtävänäsi on ennustaa kuulan
laskeutumispaikan x-koordinaatti, eli työnnön pituus. Ilmanvastus
jätetään huomioimatta. Ohjelma tulostaa kuulan laskeutumispaikan
x-koordinaatin (metreissä, ilman yksikköä). (noin 14 m)
Ohjelma saa tulostaa vain yhden LUVUN, noin 14 
Saattaa joutua ratkaisemaan toisen asteen yhtälön juuren.
"""


import sys
import time
import pandas
import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt

inputfile='mittaus.csv'


data=pandas.read_csv(inputfile)


# Erottele x- ja y-koordinaatit
# iloc Pandasin indeksointi rivien ja sarakkeiden valitsemiseen
# reshape - matriisi vektoriksi, -1 skaalaa ulottuvuuden kokoa rivien mukaan
x = data.iloc[:, 0].values.reshape(-1, 1)  # sarakkeen (kaikki rivit) datasta, x-koordinaatit
y = data.iloc[:, 1].values.reshape(-1, 1)  # y-koordinaatit

#print("x",x)
#print("y",y)

# Polynomiregressio: määritä aste 2 polynomille
poly = PolynomialFeatures(degree=2)  # Käytetään polynomiregressiota asteen 2 polynomia varten
x_poly = poly.fit_transform(x)  # Muodostetaan polynomitausta x:lle

# Luo lineaarinen regressiomalli
model = linear_model.LinearRegression()  # Luodaan lineaarinen regressiomalli
model.fit(x_poly, y)  # sovitetaan malli datalle

# Ennustele y-arvot polynomisella regressiomallilla
y_ennuste = model.predict(x_poly)

# Etsi x-koordinaatti, jossa y = 0
coefficients = model.coef_[0]  # Mallin kertoimet
intercept = model.intercept_[0]  # Mallin kiinteä termi

# Polynomi on muotoa y = ax^2 + bx + c
# Ratkaise yhtälö y = 0
a = coefficients[2]  # a-kerroin
b = coefficients[1]  # b-kerroin
c = intercept  # c-kerroin

# Ratkaise toisen asteen yhtälö ax^2 + bx + c = 0
juuret = np.roots([a, b, c])  # Löytää juuret yhtälölle

# Valitse positiivinen juuri (koska x on positiivinen)
x_loppupiste = juuret[juuret > 0][0]  # Valitsee positiivisen juuren

# Tulosta ratkaisu muotoiltuna kahden desimaalin tarkkuudella
print(int(x_loppupiste))

# Piirrä alkuperäinen data ja polynomikä
#plt.scatter(x, y, color='blue', label='Datapisteet')  # Piirretään alkuperäiset datapisteet sinisinä
#plt.plot(x, y_pred, color='red', label='Polynomisovitus')  # Piirretään polynomikäyrä punaisena
#plt.xlabel('x-koordinaatti')  # x-akselin otsikko
#plt.ylabel('y-koordinaatti')  # y-akselin otsikko
#plt.legend()  # Näytä legenda
#plt.show()  # Näytä kuva