import requests
from bs4 import BeautifulSoup
import pymysql

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

'''
Create SQL tables
Use 2D List to create compare_item table
'''

def Items(cursor):
	cursor.execute("CREATE TABLE item(item_id int NOT NULL AUTO_INCREMENT, item_name varchar(255) NOT NULL, total_quantity int, item_price int, category_id int, PRIMARY KEY (item_id))")
	
	with open("items.txt", "r") as dangus
    	lines = dangus.readlines()

	for line in lines:
    	data = line.strip().split(", ")
    	name = data[0]
    	quant = data[1]
    	price = data[2]
    	cat_id = data[3]

    	cursor.execute("INSERT INTO item (item_name, total_quantity, item_price, category_id) VALUES(%s, %s, %s, %s)", (name, quant, price, cat_id))

def CompItems(cursor, mainList):
	cursor.execute("CREATE TABLE comparison_item(compare_id int NOT NULL AUTO_INCREMENT, compare_name varchar(255) NOT NULL, compare_price int, store_id int, category_id int, PRIMARY KEY (item_id))")

	for i in range(len(mainList)):
		cursor.execute("INSERT INTO comparison_item (compare_name, store_id, compare_price, category_id) VALUES(%s, %s, %s, %s)", (mainList[i][0], mainList[i][1], mainList[i][2], mainList[i][3]))

def Categories(cursor):
	cursor.execute("CREATE TABLE categories(category_id int NOT NULL, category_name varchar(20))")
	cats = ['lighting', 'grip', 'camera']
	for i in range(len cats):
		cursor.execute("INSERT INTO categories (cat_id, cat_name) VALUES(%s, %s)", (i, cats[i]))

def Stores(cursor):
	cursor.execute("CREATE TABLE store(store_id int NOT NULL, store_name varchar(255))")
	stoats = ['store a', 'store b', 'store c']
	for i in range(len stoats):
		cursor.execute("INSERT INTO store (store_id, store_name) VALUES(%s, %s)", (i, stoats[i]))

def Customers(cursor):
	cursor.execute("CREATE TABLE customer(customer_id int NOT NULL AUTO_INCREMENT, first_name varchar(100), last_name varchar(100), phone varchar(20), email varchar(255), company varchar(255))")
	cats = ['lighting', 'grip', 'camera']
	with open("customers.txt", "r") as dangus
    	lines = dangus.readlines()

	for line in lines:
    	data = line.strip().split(", ")
    	fname = data[0]
    	lname = data[1]
    	phone = data[2]
    	email = data[3]
    	company = data[4]

		cursor.execute("INSERT INTO customer (first_name, last_name, phone, email, company) VALUES(%s, %s, %s, %s, %s)", (fname, lname, phone, email, company))
			
def main():
	conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='none', passwd=None, db='mysql')
	cursor=conn.cursor()

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