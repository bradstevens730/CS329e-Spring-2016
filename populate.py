import pymysql

conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='none', passwd=None, db='mysql')
cursor=conn.cursor()

class Item():
	category = "Item"
	with open("items.txt", "r") as dangus:
    	lines = dangus.readlines()

	for line in lines:
    	data = line.strip().split(", ")
    	name = data[0]
    	quant = data[1]
    	price = data[2]
    	cat_id = data[3]

    	cursor.execute("INSERT INTO items (person_id, category, type) VALUES(%s, %s, %s, %s)", (name, quant, price, cat_id))
