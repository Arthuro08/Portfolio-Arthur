
CREATE DATABASE FEDERACAO_BD
GO
USE FEDERACAO_BD

CREATE TABLE Federacao(
    ID_Federacao int primary key,
    Nome varchar(50) not null,
    Sigla varchar(2) not null,
    Estado varchar(50)
);

CREATE TABLE Clube(
    ID_Clube int primary key,
    Nome varchar(50) not null,
    Cidade varchar(50),
    FK_ID_Federacao int foreign key references Federacao(ID_Federacao)
);

CREATE TABLE Jogador(
    ID_Jogador int primary key,
    Nome varchar(50) not null,
    Posicao varchar(3) not null,
    DataNascimento date not null,
    FK_ID_Clube int foreign key references Clube(ID_Clube)
);

select * from SYS.tables -- seleciona todas as tabelas do banco de dados

INSERT INTO Federacao (id_Federacao,Nome, Sigla, Estado) VALUES 
(1,'Federação Paulista de Futebol', 'SP', 'São Paulo'),
(2,'Federação de Futebol do Rio de Janeiro', 'RJ', 'Rio de Janeiro'),
(3,'Federação Mineira de Futebol', 'MG', 'Minas Gerais'),
(4,'Federação Gaúcha de Futebol', 'RS', 'Rio Grande do Sul');

select * from Federacao

INSERT INTO Clube (id_clube, Nome, Cidade, FK_ID_Federacao) VALUES
(6,'Corinthians', 'São Paulo', 1),
(7,'Vasco da Gama', 'Rio de Janeiro', 2),
(8,'Cruzeiro', 'Belo Horizonte', 3),
(9,'Internacional', 'Porto Alegre', 4),
(1,'Palmeiras', 'São Paulo', 1),
(2,'Flamengo', 'Rio de Janeiro', 2),
(3,'Atlético Mineiro', 'Belo Horizonte', 3),
(4,'Grêmio', 'Porto Alegre', 4),
(5, 'São Paulo', 'São Paulo', 1);


select * from Clube

INSERT INTO Jogador (id_jogador, Nome, Posicao, DataNascimento, FK_ID_Clube) VALUES 
(1,'Raphael Veiga', 'MEI', '1995-06-19', 1),
(2,'Giorgian De Arrascaeta', 'MEI', '1994-06-01', 2),
(3,'Hulk', 'ATA', '1986-07-25', 3),
(4,'Yeferson Soteldo', 'ATA', '1997-06-30', 4),
(5,'Gustavo Gómez', 'ZAG', '1993-05-06', 1),
(6,'Rodrigo Caio', 'ZAG', '1993-02-17', 2),
(7,'Junior Alonso', 'ZAG', '1991-08-19', 3),
(8,'Walter Kannemann', 'ZAG', '1987-03-22', 4),
(9,'Dudu', 'ATA', '1992-12-07', 1),
(10,'Bruno Henrique', 'ATA', '1989-06-30', 2),
(11,'Eduardo Vargas', 'ATA', '1989-11-20', 3),
(12,'Diego Souza', 'ATA', '1985-06-22', 4),
(13,'Gustavo Scarpa', 'MEI', '1994-01-05', 1),
(14,'Arrascaeta', 'MEI', '1994-06-01', 2),
(15,'Nacho Fernández', 'MEI', '1988-01-12', 3),
(16,'Jean Pyerre', 'MEI', '1998-02-07', 4),
(17,'Rony', 'ATA', '1995-05-11', 1),
(18,'Michael', 'ATA', '1996-04-08', 2),
(19,'Keno', 'ATA', '1989-09-10', 3),
(20,'Ferreira', 'ATA', '1997-03-15', 4),
(21,'Luan', 'MEI', '1993-03-05', 1),
(22,'Gerson', 'MEI', '1992-05-20', 2),
(23,'Edenílson', 'MEI', '1989-02-18', 3),
(24,'Matheus Henrique', 'MEI', '1997-04-19', 4),
(25, 'Luciano', 'ATA', '1990-10-10', 5),
(26, 'Calleri', 'ATA', '1988-09-19', 5),
(27, 'Reinaldo', 'ZAG', '1989-11-11', 5),
(28, 'Arboleda', 'ZAG', '1986-01-14', 5),
(30, 'Memphis Depay', 'ATA', '1994-02-13', 6),
(31, 'Yuri Alberto', 'ATA', '1999-03-10', 6),
(32, 'Cássio', 'GOL', '1987-06-06', 8),
(33, 'Philippe Coutinho', 'MEI', '1992-06-12', 7),
(34, 'Lucas Piton', 'LAT', '1999-01-01', 7),
(35, 'Rafael Borré', 'ATA', '1995-01-01', 9),
(36, 'Alan Patrick', 'MEI', '1991-01-01', 9),
(37, 'Léo Jardim', 'GOL', '1995-01-01', 7);


-- ##### COMANDOS DE CONSULTA ##### 

select * from Jogador -- select * é basicamente selecionar TUDO

select id_jogador, nome, posicao from jogador -- seleciona apenas determinados campos

select * from Jogador where posicao = 'MEI' -- seleciona apenas jogadores cuja posição é MEI

select * from Jogador where posicao <> 'MEI' -- seleciona apenas jogadores cuja posição é diferente de MEI

select * from Jogador ORDER by Nome asc -- seleciona todos os jogadores em ordem alfabética (asc (crescente) ou desc (decrescente))

select * from Federacao where sigla = 'SP' -- seleciona todas as federações cuja sigla é SP

select * from Federacao where Nome like '%FEDERAÇÃO%' -- seleciona todas as federações que possuem "Federação" no nome

select * from Federacao where Nome not like '%MINEIRA%' -- seleciona todas as federações que NÃO possuem "Mineira" no nome

select * from Jogador where Posicao like 'ATA' -- seleciona todos os jogadores cuja posição é ATA

select * from Jogador join CLube on Jogador.FK_ID_Clube = Clube.ID_Clube 

select * from Jogador where Posicao not like 'MEI' -- seleciona todos os jogadores cuja posição NÃO é MEI

select * from Jogador join CLube on Jogador.FK_ID_Clube = Clube.ID_Clube ORDER by Clube.Nome asc
