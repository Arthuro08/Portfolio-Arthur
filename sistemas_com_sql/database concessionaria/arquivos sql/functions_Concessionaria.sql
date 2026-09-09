USE Concessionaria
GO


-- UDF ESCALAR (retorna valor único)
CREATE OR ALTER FUNCTION set_desconto_geral(@valor decimal(10,2), @desconto decimal(10,2))
RETURNS DECIMAL(10,2)
BEGIN
    RETURN @valor - @desconto
END
-- essa função vai receber dois parametros (o valor de venda do carro e o valor a ser descontado por carro) e realizar o calculo
GO
-- UDF Tabela (retorna tabela)
CREATE OR ALTER FUNCTION get_estoque_marca(@idmarca int)
RETURNS TABLE
AS
RETURN(
    SELECT car.ID_Carro as 'Cód. Carro em Estoque', mar.Nome as 'Marca', mod.Nome, car.Cor, car.Ano, car.Placa
    FROM Marca mar 
    JOIN Modelo mod on mod.FK_ID_Marca = mar.ID_Marca
    JOIN Carro car on car.FK_ID_Modelo = mod.ID_Modelo
    JOIN Venda ven on ven.FK_ID_Carro = car.ID_Carro
    WHERE mar.ID_Marca = @idmarca
)
