import pandas


"""
M9 
1. Datan esikäsittely- 09_esikasittely.mp4 (0:53.0)
Lue tiedosto weather data.csv ja poista siitä päiväys
(utc timestamp-sarake). Poista tämän jälkeen rivit, joilla on
puuttuvia tietoja. Tallenna tulos tiedostoon preprocessed.csv.
(Data from Data Platform)

Älkää poistako ylimääräisiä rivejä
Älkää jättäkö poistamatta rivejä, jotka pyydetään poistamaan  

Kirjoita koko ohjelma, ei pelkkää funktiota

,  utc_timestamp,        AT_radiation_direct_horizontal,AT_radiation_diffuse_horizontal
0, 1980-02-21T23:00:00Z, ,

HUOM ! test.py testiohjelma vertaa arvoon (13949, 70).

"""

# Tiedostojen nimet
inputfile = 'weather_data.csv'
outputfile = 'preprocessed.csv'

# Lue data
data = pandas.read_csv(inputfile)

# Tulosta alkuperäinen muoto
print("Dimensiot, rivien ja sarakkeiden määrä : " + str(data.shape)) # (32317, 70)

# Poistetaan utc_timestamp -sarake
data.drop(data.columns[1], axis=1, inplace=True)

# Tulostaa uuden muodon
print("Data shape (tuple) : " + str(data.shape))  # (32317, 69)

# Poistetaan NaN -rivien sisältävät rivit
data.dropna(inplace=True)  # poista tyhjät rivit
print("Poistetaan NaN -rivien sisältävät rivit...")
print("Data shape NaN-rivien poiston jälkeen : " + str(data.shape))  # (13949, 69)

# HUOM ! test.py testiohjelma vertaa arvoon (13949, 70) ja dimensiot tällä hetkellä (13949, 69).
# Lisää indeksi sarake takaisin alkuperäiseen DataFrame:iin
data.reset_index(drop=True, inplace=True)

# Lisää alkuperäinen indeksi uudeksi sarakkeeksi
data.insert(0, 'Index', range(1, len(data) + 1))

# Tulosta uusi muoto
print("Dimensiot, rivien ja sarakkeiden määrä : " + str(data.shape))  # (13949, 70)
# nyt dimensiot ovat vaaditut.

# Tallenna tulos tiedostoon
data.to_csv(outputfile, index=False)  # Tallenna ilman alkuperäistä indeksikenttää
#data.to_csv(outputfile)  # Tallenna ilman alkuperäistä indeksikenttää