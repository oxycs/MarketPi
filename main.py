import random
import os
import subprocess
import time
import mysql.connector

db_address = "ADDRESS"
db_port = "1234"
db_user = "USER"
db_password = "PASSWORD"

db_name = "marketpi_data"
db_table = "marketplace_table"

count = subprocess.Popen(["timeout", "--preserve-status", "5", "tcpdump", "-i", "bluetooth0"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
initial = count.stdout.read().decode("utf-8").split("\n")[4].split(" ")[0]
time.sleep(10)
count2 = subprocess.Popen(["timeout", "--preserve-status", "5", "tcpdump", "-i", "bluetooth0"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
final = count2.stdout.read().decode("utf-8").split("\n")[4].split(" ")[0]
print(int(final) - int(initial))

db = mysql.connector.connect(user=db_user, password=db_password, host=db_address, database=db_name, port=db_port)
cursor = db.cursor()
cursor.execute("INSERT INTO " + db_table + " (packets, timestamp) VALUES (" + str(int(final) - int(initial)) + ", NOW());")
db.commit()
cursor.close()