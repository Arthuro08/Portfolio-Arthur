USE Concessionaria


ALTER TABLE Marca ADD CONSTRAINT UQ_Marca_Nome UNIQUE (Nome) /* restrição (ou constraint) para a coluna Nome da tabela Marca (possuir apenas dados UNIQUE) */
ALTER TABLE Modelo ADD CONSTRAINT UQ_Modelo_Nome UNIQUE (Nome)
ALTER TABLE Venda ADD CONSTRAINT UQ_Venda_FK_ID_Carro UNIQUE (FK_ID_Carro) /* restrição na FK do Carro da tabela Venda para evitar que um carro seja vendido duas vezes */

select * from INFORMATION_SCHEMA.TABLE_CONSTRAINTS where TABLE_NAME = 'Marca' /* seleciona todas as constraints criadas na tabela 'Marca' (Ex: a PK e o UNIQUE) */
select * from INFORMATION_SCHEMA.TABLE_CONSTRAINTS where TABLE_NAME = 'Modelo' /* seleciona todas as constraints criadas na tabela 'Modelo' (Ex: a PK, a FK e o UNIQUE) */