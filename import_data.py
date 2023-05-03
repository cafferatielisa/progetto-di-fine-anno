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

mycursor.execute("DROP TABLE FORMULA1.piloti")

mycursor.execute("""
  CREATE TABLE IF NOT EXISTS FORMULA1.piloti (
    driverId INTEGER,
    driverRef VARCHAR(30) NOT NULL,
    number VARCHAR(30),
    code VARCHAR(30),
    forename VARCHAR(30),
    surname VARCHAR(30),
    dob DATE,
    nationality VARCHAR(30)
  );""")


mycursor.execute("DELETE FROM FORMULA1.piloti")
mydb.commit()

#Read data from a csv file
formula_data = pd.read_csv('./drivers.csv', index_col=False, delimiter = ',')
formula_data = formula_data.fillna('Null')
formula_data.drop(formula_data.columns[len(formula_data.columns)-1], axis=1, inplace=True)
print(formula_data.head(20))


for i,row in formula_data.iterrows():
    cursor = mydb.cursor()
    #here %S means string values 
    sql = "INSERT INTO FORMULA1.piloti VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, tuple(row))
    print("Record inserted")
    # the connection is not auto committed by default, so we must commit to save our changes
    mydb.commit()


mycursor.execute("SELECT * FROM FORMULA1.piloti")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)