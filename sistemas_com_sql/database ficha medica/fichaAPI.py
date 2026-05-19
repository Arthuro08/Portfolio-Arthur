import pyodbc
from flask import Flask, jsonify, request

app = Flask(__name__)
app.secret_key = 'ArthurAlmeidaFichaAPI'

config = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=DESKTOP-MLFI9DN;'
    'Database=Users_Sistema;'
    'Trusted_Connection=yes;'
)

cursor = config.cursor()

@app.route('/receber', methods=['GET'])
def receber():
    pass

