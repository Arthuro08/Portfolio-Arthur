USE Concessionaria
GO

CREATE OR ALTER FUNCTION set_desconto_geral(@valor decimal(10,2), @desconto decimal(10,2))
RETURNS DECIMAL(10,2)
BEGIN
    RETURN @valor - @desconto
END
-- essa função vai receber dois parametros (o valor de venda do carro e o valor a ser descontado por carro) e realizar o calculo

