import requests
from bs4 import BeautifulSoup
outFile=open('mainFile','w')

outFile.close()
outFile=open('mainFile','a')

def gearLightInfo():
	

	gearLight = requests.get("http://www.hdgear.tv/LIGHTING")
	soupGearLight = BeautifulSoup(gearLight.content,"html.parser")

	pricelist = []
	gLightProdPrice = soupGearLight.find_all("div",{"class":"priceBox"})
	for item in gLightProdPrice:
		stripper=item.text
		stripper.strip("$")
		pricelist.append(stripper)
	gLightProdName = soupGearLight.find_all("div",{"class":"listText"})

	for item in gLightProdName:
		texto=item.text
		priceo=pricelist.pop(0)
		s=texto + ":" + priceo + "\n\n"
		outFile.write(s)
def amgLightInfo():
	'''amgLight = requests.get("http://austinmoviegear.com/")
	soupAMGLight = BeautifulSoup(amgLight.content,"html.parser")
	
	amgLightProdPrice = soupAMGLight.find_all("img",{"class":"grpelem"})
	for item in amgLightProdPrice:
		print(item.text)
		'''
		
	
def main():
	gearLightInfo()
	#amgLightInfo()

main()
outFile.close()
