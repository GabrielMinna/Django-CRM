import mysql.connector

dataBase=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",

)

#preparar el cursor de objetos

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE IF NOT EXISTS CRM_app")
print("Database Created")

