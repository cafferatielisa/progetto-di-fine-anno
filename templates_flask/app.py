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


@app.route('/circuiti')
def circuitiList():
        mycursor.execute("SELECT * FROM circuits")
        myresult = mycursor.fetchall()
        return render_template('circuits.html', table_list=myresult)

@app.route('/scuderie')
def scuderieList():
        mycursor.execute("SELECT * FROM constructors")
        myresult = mycursor.fetchall()
        return render_template('constructors.html', table_list=myresult)

@app.route('/stagioni')
def stagioniList():
        mycursor.execute("SELECT * FROM stagioni")
        myresult = mycursor.fetchall()
        return render_template('seasons.html', table_list=myresult)