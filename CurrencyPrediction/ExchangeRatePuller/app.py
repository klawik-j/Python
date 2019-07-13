import requests
import json

response = requests.get('http://api.nbp.pl/api/exchangerates/rates/A/USD/last/60/')

# ##########NOTATKI###########
#plik = open('data.py', 'w')
#plik.write(str(r.json()))
#plik.close()

#print(r.json())

#print(data['rates'][59]['effectiveDate'])

##########################################

######################################
# Plik zawiera metode wyciagajaca informacje o kursie z ostatnich 60dni
# zapisuje je do dict data
# dodatkowo zapisuje do .txt dla mojej lepszej wizualizacji tego jak sa reprezentowane poszczegolne dane
########################################

data = json.loads(response.text)

plik = open("data.txt",'w')
i=int(0)
for day in data['rates']:
    plik.write(str(data['rates'][i])+"\n")
    i=i+1
plik.close()
