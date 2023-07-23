# install mysql
# pip isntall mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = os.getenv("MYSQL_PASSWORD")
    
    )

# prepare a cursor object, for search create obtain data
cursorObject = dataBase.cursor()

# Create a database 
cursorObject.execute("CREATE DATABASE crm_data")

print("Successful create database name : crm_data !")

