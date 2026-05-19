CREATE DATABASE Ficha_Medica
GO 
USE Ficha_Medica


CREATE TABLE Paciente(
  num_paciente int primary key IDENTITY(0,1) NOT NULL,
  nome_paciente varchar(255) NOT NULL,
  data_nasc date,
  sexo varchar(20),
  convenio varchar(50) NOT NULL,
  est_civil varchar(50),
  RG varchar(30) unique NOT NULL
)

CREATE TABLE Endereco(
  cod_endereco int primary key IDENTITY(0,1) NOT NULL,
  endereco varchar(255) NOT NULL,
  fk_paciente int foreign key REFERENCES Paciente(num_paciente)
)

CREATE TABLE Telefone(
  cod_telefone int primary key IDENTITY(0,1) NOT NULL,
  telefone varchar(15) NOT NULL,
  fk_paciente int foreign key REFERENCES Paciente(num_paciente)
)

CREATE TABLE Consulta(
  num_consulta int primary key IDENTITY(0,1) NOT NULL,
  data_consulta date,
  medico varchar(255) NOT NULL,
  diagnostico varchar(255) NOT NULL,
  fk_paciente int foreign key REFERENCES Paciente(num_paciente) 
)

CREATE TABLE Exame(
  num_exame int primary key IDENTITY(0,1) NOT NULL,
  nome varchar(255) NOT NULL,
  data_exame date,
  fk_consulta int foreign key REFERENCES Consulta(num_consulta)
)

EXEC sp_rename 'Paciente.nome', 'nome_paciente', 'COLUMN';