import requests
from bs4 import BeautifulSoup

gearLight = requests.get("http://www.hdgear.tv/LIGHTING")
soupGearLight = BeautifulSoup(gearLight.content)

pricelist = []
gLightProdPrice = soupGearLight.find_all("div",{"class":"priceBox"})
for item in gLightProdPrice:
	stripper=item.text
	stripper.strip("$")
	pricelist.append(stripper)
gLightProdName = soupGearLight.find_all("div",{"class":"listText"})

for item in gLightProdName:
	print (item.text, ":",pricelist.pop(0), "\n\n")
	
