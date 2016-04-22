import requests
from bs4 import BeautifulSoup

'''
Make a 2D list of items, each item has (name, price, store_id,category_id)

Store: GEAR-1  MOPAC-2  LENSPRO-3

Category: LIGHTS-1   GRIP-2    CAMERA-3


'''

def gearLightInfo(listy):
	
	
	gearLight = requests.get("http://www.hdgear.tv/LIGHTING")
	soupGearLight = BeautifulSoup(gearLight.content,"html.parser")

	pricelist = []
	gLightProdPrice = soupGearLight.find_all("div",{"class":"priceBox"})
	for item in gLightProdPrice:
		stripper=item.text
		stripper=stripper[34:]
		stripper=stripper.strip()
		pricelist.append(stripper)
	
	gLightProdName = soupGearLight.find_all("div",{"class":"listText"})
	
	for item in gLightProdName:
		lilList=[]
		lilList.append(item.text)
		lilList.append(pricelist.pop(0))
		lilList.append(1)
		lilList.append(1)
		listy.append(lilList)
		
def gearGripInfo(listy):
	
	gearGrip = requests.get("http://www.hdgear.tv/GRIP")
	soupGearGrip = BeautifulSoup(gearGrip.content,"html.parser")

	pricelist = []
	
	gGripProdPrice = soupGearGrip.find_all("div",{"class":"priceBox"})
	for item in gGripProdPrice:
		stripper=item.text
		stripper=stripper[34:]
		stripper=stripper.strip()
		pricelist.append(stripper)
	
	gGripProdName = soupGearGrip.find_all("div",{"class":"listText"})
	for item in gGripProdName:
		lilList=[]
		lilList.append(item.text)
		lilList.append(pricelist.pop(0))
		lilList.append(1)
		lilList.append(2)
		listy.append(lilList)
		
def gearCamInfo(listy):
	
	gearCam = requests.get("http://www.hdgear.tv/CAMERA")
	soupGearCam = BeautifulSoup(gearCam.content,"html.parser")

	pricelist = []
	
	gCamProdPrice = soupGearCam.find_all("div",{"class":"priceBox"})
	for item in gCamProdPrice:
		stripper=item.text
		stripper=stripper[34:]
		stripper=stripper.strip()
		pricelist.append(stripper)
	
	gCamProdName = soupGearCam.find_all("div",{"class":"listText"})
	for item in gCamProdName:
		lilList=[]
		lilList.append(item.text)
		lilList.append(pricelist.pop(0))
		lilList.append(1)
		lilList.append(3)
		listy.append(lilList)
		
def MOPLightInfo(listy):
	mopInfoKITS = requests.get("https://www.mopacmedia.com/inventory/categories/30/items")
	soupMOPinfoKITS = BeautifulSoup(mopInfoKITS.content,"html.parser")
	priceList=[]
	mopKitPrice = soupMOPinfoKITS.find_all("dl",{"class":"prices"})
	for item in mopKitPrice:
		buzz=item.text
		buzz=buzz[10:-37]
		buzz=buzz.strip()
		priceList.append(buzz)
		
	
	mopKitName = soupMOPinfoKITS.find_all("p",{"class":"vendor-name"})
	for item in mopKitName:
		lilList=[]
		lilList.append(item.text)
		lilList.append(priceList.pop(0))
		lilList.append(2)
		lilList.append(1)
		listy.append(lilList)
		
	mopInfoTung = requests.get("https://www.mopacmedia.com/inventory/categories/27/items")
	soupMOPinfoTung = BeautifulSoup(mopInfoTung.content,"html.parser")
	priceList=[]
	mopTungPrice = soupMOPinfoTung.find_all("dl",{"class":"prices"})
	for item in mopTungPrice:
		buzz=item.text
		buzz=buzz[10:-37]
		buzz=buzz.rstrip("\n")
		priceList.append(buzz)
		
	
	mopTungName = soupMOPinfoTung.find_all("p",{"class":"vendor-name"})
	for item in mopTungName:
		lilList=[]
		lilList.append(item.text)
		lilList.append(priceList.pop(0))
		lilList.append(2)
		lilList.append(1)
		listy.append(lilList)
		
def MOPGripInfo(listy):
	mopInfoGrip = requests.get("https://www.mopacmedia.com/inventory/categories/95/items")
	soupMOPinfoGrip = BeautifulSoup(mopInfoGrip.content,"html.parser")
	priceList=[]
	mopGripPrice = soupMOPinfoGrip.find_all("dl",{"class":"prices"})
	for item in mopGripPrice:
		buzz=item.text
		buzz=buzz[10:-35]
		buzz=buzz.strip("\n")
		priceList.append(buzz)
		
	
	mopGripName = soupMOPinfoGrip.find_all("p",{"class":"vendor-name"})
	for item in mopGripName:
		lilList=[]
		lilList.append(item.text)
		lilList.append(priceList.pop(0))
		lilList.append(2)
		lilList.append(2)
		listy.append(lilList)
		
def MOPCamInfo(listy):
	mopInfoCam = requests.get("https://www.mopacmedia.com/inventory/categories/127/items")
	soupMOPinfoCam = BeautifulSoup(mopInfoCam.content,"html.parser")
	priceList=[]
	mopCamPrice = soupMOPinfoCam.find_all("dl",{"class":"prices"})
	for item in mopCamPrice:
		buzz=item.text
		buzz=buzz[10:-39]
		buzz=buzz.rstrip("W")
		buzz=buzz.strip()
		priceList.append(buzz)
		
	
	mopCamName = soupMOPinfoCam.find_all("p",{"class":"vendor-name"})
	for item in mopCamName:
		lilList=[]
		lilList.append(item.text)
		lilList.append(priceList.pop(0))
		lilList.append(2)
		lilList.append(3)
		listy.append(lilList)
		
def PROLightInfo(listy):
	PROInfoLight = requests.get("https://www.lensprotogo.com/rent/category/lighting/continuous/")
	soupPROinfoLight = BeautifulSoup(PROInfoLight.content,"html.parser")
	priceList=[]
	PROLightPrice = soupPROinfoLight.find_all("p",{"class":"item-price"})
	for item in PROLightPrice:
		buzz=item.text
		buzz=buzz.strip()
		priceList.append(buzz)
		
	
	PROLightName = soupPROinfoLight.find_all("p",{"class":"item-description"})
	for item in PROLightName:
		lilList=[]
		lilList.append(item.text)
		lilList.append(priceList.pop(0))
		lilList.append(3)
		lilList.append(1)
		listy.append(lilList)
	


def PROGripInfo(listy):
	PROInfoGrip = requests.get("https://www.lensprotogo.com/rent/category/lighting/accessories/")
	soupPROinfoGrip = BeautifulSoup(PROInfoGrip.content,"html.parser")
	priceList=[]
	PROGripPrice = soupPROinfoGrip.find_all("p",{"class":"item-price"})
	for item in PROGripPrice:
		buzz=item.text
		buzz=buzz.strip()
		priceList.append(buzz)
		
	
	PROGripName = soupPROinfoGrip.find_all("p",{"class":"item-description"})
	for item in PROGripName:
		lilList=[]
		lilList.append(item.text)
		lilList.append(priceList.pop(0))
		lilList.append(3)
		lilList.append(2)
		listy.append(lilList)

def PROCamInfo(listy):
	PROInfoCam = requests.get("https://www.lensprotogo.com/rent/category/cameras/")
	soupPROinfoCam = BeautifulSoup(PROInfoCam.content,"html.parser")
	priceList=[]
	PROCamPrice = soupPROinfoCam.find_all("p",{"class":"item-price"})
	for item in PROCamPrice:
		buzz=item.text
		buzz=buzz.strip()
		priceList.append(buzz)
		
	
	PROCamName = soupPROinfoCam.find_all("p",{"class":"item-description"})
	for item in PROCamName:
		lilList=[]
		lilList.append(item.text)
		lilList.append(priceList.pop(0))
		lilList.append(3)
		lilList.append(3)
		listy.append(lilList)
			
def main():
	mainList=[]
	#gearLightInfo(mainList)
	#gearGripInfo(mainList)
	#gearCamInfo(mainList)
	
	
	#MOPLightInfo(mainList)
	
	#MOPGripInfo(mainList)
	
	#MOPCamInfo(mainList)
	
	PROLightInfo(mainList)
	PROGripInfo(mainList)
	PROCamInfo(mainList)
	
	print(mainList)
main()

