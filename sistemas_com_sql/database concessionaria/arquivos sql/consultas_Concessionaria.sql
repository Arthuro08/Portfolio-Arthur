USE Concessionaria

select v.Data_Venda, v.Valor_Venda, c.Ano, c.Quilometragem, m.Nome, a.Nome as Marca from Venda v join Carro c on FK_ID_Carro = ID_Carro join Modelo m on FK_ID_Modelo = ID_Modelo join Marca a on FK_ID_Marca = ID_Marca
select Pais, count(*) as Quantidade_Marcas from Marca group by Pais
select Nome, Pais from Marca
select * from Marca
select * from sys.tables

-- consultas com Functions (ver as functions no functions_Concessionaria.sql)
SELECT car.ID_Carro, mar.Nome, mod.Nome, car.Valor as 'Valor Antigo', dbo.set_desconto_geral(car.Valor, 15000.00) as 'Valor com Desconto' 
FROM Marca mar 
join Modelo mod on mod.FK_ID_Marca = mar.ID_Marca
join Carro car on car.FK_ID_Modelo = mod.ID_Modelo
join Venda ven on ven.FK_ID_Carro = car.ID_Carro