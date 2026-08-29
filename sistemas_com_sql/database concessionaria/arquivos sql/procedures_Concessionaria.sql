USE Concessionaria

CREATE OR ALTER PROCEDURE sp_num_vendas 
AS
    BEGIN
        SELECT mar.Nome, COUNT(ven.ID_Venda) as 'Qtd de Vendas'
        FROM Marca mar 
        join Modelo mod on mod.FK_ID_Marca = mar.ID_Marca
        join Carro car on car.FK_ID_Modelo = mod.ID_Modelo
        join Venda ven on ven.FK_ID_Carro = car.ID_Carro
        group by mar.Nome
    END
GO
EXEC sp_num_vendas

CREATE OR ALTER PROCEDURE sp_media_preco(@marca varchar(255), @modelo varchar(255))
AS
DECLARE @media float
BEGIN
    IF EXISTS (SELECT 1 FROM Marca mar join Modelo mod on mod.FK_ID_Marca = mar.ID_Marca WHERE mar.Nome = @marca AND mod.Nome = @modelo)
        BEGIN 
            SELECT @media = AVG(ven.Valor_Venda)
            FROM Marca mar 
            join Modelo mod on mod.FK_ID_Marca = mar.ID_Marca
            join Carro car on car.FK_ID_Modelo = mod.ID_Modelo
            join Venda ven on ven.FK_ID_Carro = car.ID_Carro
            WHERE mar.Nome = @marca AND mod.Nome = @modelo
            PRINT 'Valor Médio do ' + CAST(@marca AS VARCHAR(255)) + ' ' + CAST(@modelo AS VARCHAR(255)) + ' = R$' + CAST(@media AS VARCHAR(255))
        END
    ELSE
        BEGIN
            PRINT 'ERRO: Esta marca e/ou modelo não existe no banco de dados! Favor tente novamente.'
            PRINT 'LEMBRETE: Coloque letra maiúscula no começo dos nomes!'
        END
END
GO
EXEC sp_media_preco 'Audi', 'Q3'