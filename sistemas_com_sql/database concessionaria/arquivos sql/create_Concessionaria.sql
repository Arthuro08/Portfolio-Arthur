CREATE DATABASE Concessionaria
GO
USE Concessionaria

CREATE TABLE Marca(
    ID_Marca int PRIMARY KEY IDENTITY(1,1) NOT NULL,
    Nome varchar(255) UNIQUE NOT NULL,
    Pais varchar(255) NOT NULL
)

CREATE TABLE Modelo(
    ID_Modelo int PRIMARY KEY IDENTITY(1,1) NOT NULL,
    Nome varchar(255) NOT NULL,
    Categoria varchar(255) NOT NULL,
    FK_ID_Marca int FOREIGN KEY REFERENCES Marca(ID_Marca) NOT NULL
)

CREATE TABLE Carro(
    ID_Carro int PRIMARY KEY IDENTITY(1,1) NOT NULL,
    Placa char(7) UNIQUE NOT NULL,
    Ano int NOT NULL,
    Cor varchar(255) NOT NULL,
    Valor decimal(10,2) NOT NULL,
    Quilometragem int NOT NULL,
    FK_ID_Modelo int FOREIGN KEY REFERENCES Modelo(ID_Modelo) NOT NULL
)

CREATE TABLE Venda(
    ID_Venda int PRIMARY KEY IDENTITY(1,1) NOT NULL,
    Data_Venda date NOT NULL, 
    Valor_Venda decimal(10,2) NOT NULL,
    FK_ID_Carro int FOREIGN KEY REFERENCES Carro(ID_Carro) NOT NULL
)