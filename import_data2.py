import mysql.connector
import pandas as pd

#Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

#Create the DB (if not already exists)
mycursor.execute("CREATE DATABASE IF NOT EXISTS FORMULA1")

mycursor.execute("DROP TABLE IF EXISTS FORMULA1.circuits")

#Create the table for the csv data (if not exists)
mycursor.execute("""
  CREATE TABLE FORMULA1.circuits(
    circuitId INTEGER,
    circuitRef VARCHAR(30) NOT NULL,
    name TEXT,
    location VARCHAR(30),
    country VARCHAR(30),
    lat INTEGER,
    lng INTEGER,
    alt TEXT,
    url TEXT
  );""")

#Read data from a csv file
formula_data = pd.read_csv('./circuits.csv', index_col=False, delimiter = ',')
formula_data = formula_data.fillna('Null')
print(formula_data.head(20))

#Fill the table
for i,row in formula_data.iterrows():
    cursor = mydb.cursor()
    #here %S means string values 
    sql = "INSERT INTO FORMULA1.circuits VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, tuple(row))
    print("Record inserted")
    # the connection is not auto committed by default, so we must commit to save our changes
    mydb.commit()

#Check if the table has been filled
mycursor.execute("SELECT * FROM FORMULA1.circuits")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)