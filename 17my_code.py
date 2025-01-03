"""
M17 Tiedostossa painteddata.csv on pisteiden x- ja
y-koordinaatteja. Kirjoita ohjelma, joka tulosta montako
klusteria pisteet muodostavat. (Tehtäväpohjassa olevassa datassa klustereita on 6)

Ei ole sanottua, että lopullisissa olisi 6. Tulostamalla vain numeron 6 ei saa 
tehtävää läpi.
Saa tulostaa vain jonkun numeron.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt


data = pd.read_csv("painteddata.csv")

#Your code here

"""
Tiedosto sisältää 'x' ja 'y'-sarakkeet
x,y
0.2373360442242931,0.8294257848165333
0.23209703238787727,0.7914790239908847
"""

X = data[['x', 'y']]

# Alustetaan muuttujat klustereiden määrän arvioimiseen
# kts luento 0:17
# JOS ei tiedetä klustereiden lukumäärää etukäteen -> silhouette_scores
# eli kuinka hyvä kulsterointi on ja ettei niitä ole liikaa
silhouette_scores = []
cluster_range = range(2, 7)  # Oletetaan klustereiden määrä 2-9

# Etsi optimaalinen klustereiden määrä koko taulukosta
for n_clusters in cluster_range:
    #Asetetaan klustereiden määrä tämänhetkiselle iteraatiolle.
    kmeans = KMeans(n_clusters=n_clusters, random_state=42) 
    # Palauttaa ennustetut klusteritunnisteet (predict), eli jokaiselle pisteelle, mihin klusteriin se kuuluu.
    cluster_labels = kmeans.fit_predict(X)
    silhouette_avg = silhouette_score(X, cluster_labels) # 
    silhouette_scores.append(silhouette_avg)

# Valitaan klustereiden määrä, joka maksimoi Silhouette-metriikan
# Kuinka lähellä kukin piste on omassa klusterissaan (tiiviys).
# Kuinka kaukana se on lähimmästä muusta klusterista (erillisyys).
# Palauttaa arvon välillä -1 ja 1, jossa korkeampi arvo tarkoittaa parempaa klusterointia.
optimal_n_clusters = cluster_range[np.argmax(silhouette_scores)]

# Tulosta optimaalinen klustereiden määrä


print(n_clusters)

# Piirrä kuva
"""
plt.figure(figsize=(15, 10))
plt.plot(list(cluster_range), silhouette_scores, marker='o', linestyle='-', color='b', label='Silhouette Score')
plt.axvline(x=optimal_n_clusters, color='r', linestyle='--', label=f'Optimal clusters: {optimal_n_clusters}')
plt.title('Silhouette Score for Different Cluster Numbers')
plt.xlabel('Number of Clusters')
plt.ylabel('Silhouette Score')
plt.legend()
plt.grid(True)
plt.show()
"""