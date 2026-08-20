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

select * from Jogador where Posicao in ('ZAG', 'GOL')

select * from Federacao where Nome like '%FEDERAÇÃO%' -- seleciona todas as federações que possuem "Federação" no nome

select * from Federacao where Nome not like '%MINEIRA%' -- seleciona todas as federações que NÃO possuem "Mineira" no nome

select * from Jogador where Posicao like 'ATA' -- seleciona todos os jogadores cuja posição é ATA

select * from Jogador where Posicao not like 'MEI' -- seleciona todos os jogadores cuja posição NÃO é MEI

select * from Jogador join CLube on Jogador.FK_ID_Clube = Clube.ID_Clube 

select * from Jogador join CLube on Jogador.FK_ID_Clube = Clube.ID_Clube ORDER by Clube.Nome asc

select j.Nome as Jogador, j.Posicao, c.Nome as Clube from Jogador j join Clube c on j.FK_ID_Clube = c.ID_Clube order by c.Nome asc;

select Clube.Nome, Clube.Cidade, Federacao.Nome from Clube join Federacao on Clube.FK_ID_Federacao = Federacao.ID_Federacao order by Clube.Nome asc;

select c.Nome as Clube, c.Cidade, f.Nome as Nome_Federacao from Clube c join Federacao f on c.FK_ID_Federacao = f.ID_Federacao where f.Sigla not like 'SP' order by c.Nome desc;

select j.Nome as Jogador, j.Posicao, c.Nome as Clube, c.Cidade, f.Nome as Federacao from Jogador j join Clube c on j.FK_ID_Clube = c.ID_Clube join Federacao f on c.FK_ID_Federacao = f.ID_Federacao;

select * from Jogador where id_jogador between 10 and 30; -- seleciona todos os jogadores que possuem os ID entre 10 e 30

select * from Jogador where Nome like "%a"; -- seleciona os jogadores cujo nome TERMINA com a letra "a". OBS: o % substitui um ou mais caracteres

select * from Jogador where Nome like "a%"; -- seleciona os jogadores cujo nome COMEÇA com a letra "a". OBS: o % substitui um ou mais caracteres

select * from Jogador where FK_ID_Clube IN(2,3) -- seleciona todos os jogadores cuja FK_ID_Clube=2 ou FK_ID_Clube=3

select distinct(Posicao) from Jogador -- mostra apenas uma vez cada valor presente em uma coluna (nao repete mais de uma vez um valor no resultado)

-- #### COMANDOS DE EXCLUSAO DE DADOS ####

delete from Jogador where Nome = 'Reinaldo'; -- DELETE serve para dados (registros) // DROP serve para objetos (tabelas ou um banco de dados inteiro)

truncate table Jogador; -- deleta todos os registros de uma tabela

-- #### ATUALIZAR OS DADOS DE UM DETERMINADO REGISTRO NA TABELA ####

update Jogador set nome = 'Joaquim' where  ID_Jogador = 21;

--- #### CÁLCULOS MATEMÁTICOS EM SQL

select power(2,3) -- exponenciação
    
select abs(-13) -- módulo (valor absoluto)
    
select sqrt(49) -- raiz quadrada
    
select sum(15+50) -- soma
    
select price, round(price,1) as 'Preço com mais  ou menos casas decimais' from titles -- esse não vai funcionar nessa database pois nao tem nem sequer numero decimal, mas é basicamente: arredonda o valor de um número decimal ou especifica, tipo 9,99 arredondado com round(price,1) vai mostrar 10,00

-- #### MANIPULAÇÃO DE TEXTO

select lower(Sigla) as 'Siglas em minusculo' from Federacao -- converte todas as siglas em minúsculo
    
select upper(Nome) as 'Nomes de Jogador em maiusculo' from Jogador -- converte todos os nomes de jogador em maiusculo

select Nome, Estado + ',' + Sigla 'Estado | Sigla' from Federacao -- concatena duas colunas de strings

-- #### GROUP BY E FUNÇÕES DE AGREGAÇÃO

select Posicao, count(*) 'Qtd Jogadores' from Jogador group by Posicao -- conta a quantidade de jogadores por posicao. count(*) e group by Posicao

select Posicao, count(*) 'Qtd Jogadores' from Jogador group by Posicao having count(*) > 5 -- mostra apenas uma tabela cujas posições possuem mais de 5 jogadores. a condição 'Having' só funciona com funções de agregação: SUM(), COUNT(), MIN(), MAX(), etc

select max(DataNascimento) from Jogador -- mostra a data de nascimento do jogador mais novo no banco de dados

select min(DataNascimento) from Jogador -- mostra a data de nascimneto do jogador mais velho no banco de dados


-- #### LEFT JOIN

INSERT INTO Clube(id_clube, Nome, Cidade, FK_ID_Federacao) VALUES -- adiciona um novo clube para testar o left join
(10,'Santos', 'São Paulo', 1)
    
select * from Clube left join Jogador on ID_Clube = FK_ID_Clube -- se uma linha da tabela da esquerda não houver valores na direita, diferente do join comum, o select não excluirá essa linha, apenas adicionará null nos valores da tabela direita
-- Exemplo: Santos nesse contexto não possui nenhum jogador cadastrado. Os valores do Santos da Tabela Clube aparece no select, mas os valores da tabela Jogador nessa linha vai ser NULL, já que santos nao tem jogador cadastrado

