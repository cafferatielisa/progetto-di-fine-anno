from flask import render_template
from flask import Flask
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="FORMULA1"
)
mycursor = mydb.cursor()

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('hello.html')


@app.route('/tuttipiloti')
def pilotiList():
        mycursor.execute("SELECT * FROM piloti")
        myresult = mycursor.fetchall()
        return render_template('piloti.html', table_list=myresult)
