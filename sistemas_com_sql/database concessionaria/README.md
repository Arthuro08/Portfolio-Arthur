# 🚗 Concessionária - Banco de Dados e Dashboard Analytics

## 📌 Sobre o Projeto
Este projeto consiste na modelagem e implementação de um banco de dados para uma concessionária de veículos, utilizando SQL Server. Além da estruturação dos dados, foi desenvolvido um dashboard no Power BI para análise de vendas, estoque e indicadores do negócio.

## 🛠️ Tecnologias Utilizadas
* **Banco de Dados:** SQL Server (T-SQL)
* **Visualização de Dados:** Power BI
* **Modelagem de Dados:** Diagrama Entidade-Relacionamento (Conceitual e Lógico)

## 🗂️ Estrutura do Repositório

### modelagem (Modelagem de Dados)
* `Modelo Conceitual - Concessionaria.png`: Visão de alto nível das entidades e seus relacionamentos.
* `Modelo Lógico - Concessionaria.png`: Estrutura detalhada do banco, mapeando chaves primárias (PK), chaves estrangeiras (FK) e os tipos de dados.

### arquivos sql (Scripts SQL)
* `create_Concessionaria.sql`: Script de criação do banco de dados e das tabelas principais (`Marca`, `Modelo`, `Carro` e `Venda`).
* `constraints_Concessionaria.sql`: Aplicação de regras de integridade e negócio, utilizando restrições `UNIQUE` e `CHECK`.
* `insert_Concessionaria.sql`: Carga inicial com dados realistas para simular o ambiente de vendas e estoque da concessionária.
* `consultas_Concessionaria.sql`: Scripts contendo junções (`JOIN`) e agregações (`GROUP BY`) utilizadas para a extração de métricas.

### dashboard (Business Intelligence)
* `Dashboard_De_Vendas_E_Estoque.pbix`: Arquivo do Power BI contendo o painel interativo.
* O dashboard apresenta KPIs essenciais para o negócio, incluindo:
  * Faturamento mensal e total de vendas.
  * Média de valor dos carros vendidos.
  * Distribuição e quantidade de carros vendidos por marca e por categoria (SUV, Sedan e Hatch).

## 🚀 Como Executar o Projeto

1. **Configurando o Banco de Dados:**
   * Abra o SQL Server Management Studio (SSMS) ou a IDE de sua preferência.
   * Conecte-se à sua instância local e execute os scripts na seguinte ordem para garantir a integridade referencial:
     1. `create_Concessionaria.sql`
     2. `constraints_Concessionaria.sql`
     3. `insert_Concessionaria.sql`
   * Utilize o arquivo `consultas_Concessionaria.sql` para testar o banco e validar o retorno dos dados.

2. **Acessando o Dashboard:**
   * Certifique-se de ter o [Power BI Desktop](https://powerbi.microsoft.com/desktop/) instalado na sua máquina.
   * Abra o arquivo `Dashboard_De_Vendas_E_Estoque.pbix`.
   * *Nota:* Caso deseje conectar o painel diretamente ao seu banco de dados local recém-criado, acesse a aba "Transformar Dados" (Power Query) e atualize as credenciais e a fonte da conexão.