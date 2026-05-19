import pyodbc
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
app.secret_key = 'ArthurAlmeidaFichaAPI'

config = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=DESKTOP-MLFI9DN;'
    'Database=Ficha_Medica;'
    'Trusted_Connection=yes;'
)

cursor = config.cursor()

@app.route('/')
def home():
    return render_template('index.html')

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

    cursor.execute("SELECT * FROM Paciente WHERE RG = ?", (rg,))
    if cursor.fetchone():
        return "Paciente já cadastrado!"


    cursor.execute("INSERT INTO Paciente(nome_paciente, data_nasc, sexo, convenio, est_civil, RG) OUTPUT INSERTED.num_paciente VALUES (?, ?, ?, ?, ?, ?)", (nome_paciente, data_nasc, sexo, convenio, estado_civil, rg))
    num_paciente = cursor.fetchone()[0]
    cursor.execute("INSERT INTO Endereco(endereco, fk_paciente) VALUES(?, ?)", (endereco, num_paciente))
    cursor.execute("INSERT INTO Telefone(telefone, fk_paciente) VALUES(?, ?)", (telefone, num_paciente))
    cursor.execute("INSERT INTO Consulta(data_consulta, medico, diagnostico, fk_paciente) OUTPUT INSERTED.num_consulta VALUES(?, ?, ?, ?)", (data_consulta, medico, diagnostico, num_paciente))
    num_consulta = cursor.fetchone()[0]
    cursor.execute("INSERT INTO Exame(nome, data_exame, fk_consulta) VALUES(?, ?, ?)", (exame, data_exame, num_consulta))
    config.commit()

    return 'Cadastro realizado com sucesso!'

app.run(debug=True)



