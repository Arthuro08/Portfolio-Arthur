import pyodbc
from flask import Flask, jsonify, request

app = Flask(__name__)
app.secret_key = 'ArthurAlmeidaFichaAPI'

config = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=DESKTOP-MLFI9DN;'
    'Database=Ficha_Medica;'
    'Trusted_Connection=yes;'
)

cursor = config.cursor()

@app.route('/receber', methods=['POST'])
def receber():
    nome = request.form['nome_paciente']
    rg = request.form['RG']
    sexo = request.form['sexo']
    convenio = request.form['convenio']

