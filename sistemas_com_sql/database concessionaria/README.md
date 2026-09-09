# 🚗 Concessionária - Engenharia de Banco de Dados & Power BI Analytics

## 📌 Sobre o Projeto
Este projeto compreende o ciclo completo de desenvolvimento de uma solução de dados para o setor automotivo: desde o levantamento de requisitos e modelagem relacional (conceitual e lógica), passando pela implementação física em Microsoft SQL Server (T-SQL) com tabelas, restrições de integridade, rotinas programáveis (Views, Procedures e Functions) e cargas de dados realistas, até a construção de um painel interativo de Business Intelligence no Power BI para análise estratégica de vendas, estoque e desempenho comercial.

## 🚀 Funcionalidades
- **Modelagem Relacional Completa:** Estrutura normalizada mapeando o relacionamento entre Marcas, Modelos, Veículos em Estoque e Histórico de Vendas.
- **Integridade Referencial e Regras de Negócio:** Aplicação de restrições `FOREIGN KEY`, restrições de unicidade (`UNIQUE`) para evitar que um veículo seja vendido mais de uma vez e restrições de validação (`CHECK`) para impedir valores ou quilometragens negativas.
- **Rotinas Programáveis (T-SQL):**
  - **View (`Consolidado_Tabela`):** Centraliza os dados analíticos de vendas, veículos, marcas e modelos para simplificar relatórios e conexões externas.
  - **Stored Procedures:**
    - `sp_num_vendas`: Calcula o volume total de vendas consolidadas por marca.
    - `sp_media_preco`: Calcula e exibe o ticket médio de um modelo e marca específicos com validação prévia de existência.
  - **User-Defined Function (`set_desconto_geral`):** Função escalar que calcula dinamicamente o valor de venda de um veículo aplicando descontos parametrizados.
- **Consultas Analíticas:** Scripts de consultas avançadas utilizando junções múltiplas (`INNER JOIN`), agregações (`COUNT`, `SUM`, `AVG`) e agrupamentos (`GROUP BY`).
- **Dashboard Executivo (Power BI):**
  - Faturamento total e volume mensal de vendas.
  - Média de preço dos veículos comercializados.
  - Distribuição percentual e quantitativa de vendas por marca e por categoria de veículo (SUV, Sedan e Hatch).
  - Análise do portfólio de estoque remanescente.

## 🛠️ Tecnologias, Ferramentas e Bibliotecas
- **SGBD:** Microsoft SQL Server (T-SQL)
- **Ferramenta de Consulta & Administração:** SQL Server Management Studio (SSMS) / Azure Data Studio
- **Business Intelligence & Visualização:** Microsoft Power BI Desktop
- **Modelagem de Dados:** BrModelo / Ferramentas CASE para Diagramas de Entidade-Relacionamento (DER)

## 🧠 Conceitos Aplicados
- **Modelagem de Dados:** Diagrama Entidade-Relacionamento (Conceitual e Lógico) e Formas Normais.
- **DDL & DML:** Criação de schemas, definição de tipos de dados (`decimal`, `char`, `varchar`, `date`), auto-incremento (`IDENTITY`) e cargas massivas de dados.
- **Integridade de Dados:** Chaves primárias (`PK`), chaves estrangeiras (`FK`), `UNIQUE constraints` e `CHECK constraints`.
- **Programação em Banco de Dados:** Views, Stored Procedures com parâmetros e condicionais, Scalar Functions.
- **Business Intelligence (BI):** Extração de KPIs, criação de visualizações interativas e modelagem analítica voltada para tomadas de decisão.

## 📂 Estrutura do Projeto
```text
database concessionaria/
│
├── modelagem/
│   ├── Modelo Conceitual - Concessionaria.png  # Diagrama de entidades e relacionamentos de alto nível
│   └── Modelo Lógico - Concessionaria.png      # Mapeamento detalhado de tabelas, chaves e tipos
│
├── arquivos sql/
│   ├── create_Concessionaria.sql               # Criação da database e tabelas principais
│   ├── constraints_Concessionaria.sql          # Restrições de integridade (CHECK e UNIQUE)
│   ├── insert_Concessionaria.sql               # Carga inicial com 72 carros e 30 vendas
│   ├── insert_claude_Concessionaria.sql        # Carga massiva ampliada (+500 veículos e vendas)
│   ├── consultas_Concessionaria.sql            # Consultas de métricas, agregações e filtros
│   ├── views_Concessionaria.sql                # Criação da view Consolidado_Tabela
│   ├── procedures_Concessionaria.sql           # Stored Procedures para volume e ticket médio
│   └── functions_Concessionaria.sql            # Scalar Functions para cálculo de descontos
│
└── dashboard/
    ├── Dashboard_De_Vendas_E_Estoque.pbix      # Arquivo interativo do Power BI
    ├── Dashboard_De_Vendas_E_Estoque.pdf       # Relatório executivo exportado em PDF
    └── Dashboard de Vendas e Estoque - Concessionaria.png # Prévia visual do painel
```

## ▶️ Como Executar

### 1. Configuração e Criação do Banco de Dados
1. Abra o **SQL Server Management Studio (SSMS)** ou sua ferramenta SQL de preferência e conecte-se à sua instância local.
2. Execute os scripts localizados na pasta `arquivos sql/` na ordem cronológica recomendada para manter a integridade referencial:
   ```text
   1. create_Concessionaria.sql       -> Cria o banco Concessionaria e as tabelas
   2. constraints_Concessionaria.sql  -> Adiciona as restrições de integridade
   3. insert_Concessionaria.sql       -> Popula as marcas, modelos, estoque e vendas
   4. views_Concessionaria.sql        -> Cria as views analíticas
   5. procedures_Concessionaria.sql   -> Registra as stored procedures
   6. functions_Concessionaria.sql    -> Registra as funções de apoio
   ```
3. *(Opcional)* Caso deseje testar consultas com um volume maior de registros, execute o script adicional `insert_claude_Concessionaria.sql`.
4. Execute `consultas_Concessionaria.sql` para testar os relatórios e consultas prontas.

### 2. Acesso ao Dashboard (Power BI)
1. Instale o [Microsoft Power BI Desktop](https://powerbi.microsoft.com/desktop/).
2. Abra o arquivo `dashboard/Dashboard_De_Vendas_E_Estoque.pbix`.
3. Se desejar atualizar os dados com a sua instância do SQL Server, clique em **Transformar Dados > Configurações da Fonte de Dados** e aponte para o nome do seu servidor SQL local.
4. Para visualização rápida sem necessidade do Power BI instalado, consulte o arquivo `dashboard/Dashboard_De_Vendas_E_Estoque.pdf` ou a imagem `Dashboard de Vendas e Estoque - Concessionaria.png`.