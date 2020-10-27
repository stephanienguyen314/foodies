import os
from flask import Flask, render_template, request, redirect, url_for, abort
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('uploadPage.html')

@app.route('/upload', methods= ['POST'])
def upload():
    file =request.files['file']
    database(name = file.filename, data= file.read())
    return file.filename
def database(name,data):
    conn = sqlite3.connect ("image.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS my_table (name TEXT, data BINARY)""")
    cursor.execute("""INSERT INTO my_table (name, data) VALUES (?,?) """,(name, data))
    conn.commit()
    cursor.close()
    conn.close()
    
if __name__== '__main__':
    app.run(debug=True)


