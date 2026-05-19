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
    nome_paciente = request.form['nome_paciente']
    rg = request.form['RG']
    sexo = request.form['sexo']
    convenio = request.form['convenio']
    data_nasc = request.form['data_nasc']
    estado_civil = request.form['est_civil']

    endereco = request.form['endereco']
    telefone = request.form['telefone']

    data_consulta = request.form['data_consulta']
    medico = request.form['medico']
    diagnostico = request.form['diagnostico']

    exame = request.form['exame']
    data_exame = request.form['data_exame']



