import mysql.connector
import pandas as pd

#Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS FORMULA1")

mycursor.execute("""
  CREATE TABLE IF NOT EXISTS FORMULA1.driver_standings (
    driverStandingsId INTEGER,
    raceId INTEGER,
    driverId INTEGER,
    points INTEGER,
    position INTEGER,
    positionText VARCHAR(30),
    wins INTEGER
  );""")

mydb.commit()

#Read data from a csv file
formula_data = pd.read_csv('./driver_standings.csv', index_col=False, delimiter = ',')
formula_data = formula_data.fillna('Null')
formula_data.drop(formula_data.columns[len(formula_data.columns)-1], axis=1, inplace=True)
print(formula_data.head(20))


for i,row in formula_data.iterrows():
    cursor = mydb.cursor()
    #here %S means string values 
    sql = "INSERT INTO FORMULA1.driver_standings VALUES (%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, tuple(row))
    print("Record inserted")
    # the connection is not auto committed by default, so we must commit to save our changes
    mydb.commit()


mycursor.execute("SELECT * FROM FORMULA1.driver_standings")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)