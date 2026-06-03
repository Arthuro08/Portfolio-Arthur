USE Concessionaria

select v.Data_Venda, v.Valor_Venda, c.Ano, m.Nome, a.Nome as Marca from Venda v join Carro c on FK_ID_Carro = ID_Carro join Modelo m on FK_ID_Modelo = ID_Modelo join Marca a on FK_ID_Marca = ID_Marca

select Pais, count(*) as Quantidade_Marcas from Marca group by Pais

select Nome, Pais from Marca

select * from Marca