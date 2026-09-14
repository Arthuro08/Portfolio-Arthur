# 💼 Portfólio de Projetos - Arthur Almeida

Bem-vindo ao meu repositório central de projetos e estudos em desenvolvimento de software, engenharia de dados e inteligência artificial! Aqui estão reunidos projetos desenvolvidos ao longo da minha trajetória acadêmica — iniciada no curso técnico em **Desenvolvimento de Sistemas na ETEC de Taboão da Serra** (2022–2024) e continuada no bacharelado em **Sistemas de Informação no IFSP Campus São Paulo** (2025–2028) —, além de projetos pessoais externos desenvolvidos para produção e pesquisa.

O portfólio está organizado em cinco pilares técnicos estruturados:

---

## 🗂️ Mapeamento dos Projetos

### 🤖 Inteligência Artificial & Machine Learning (Projetos em Destaque)
Aplicações de Ciência de Dados e Aprendizado de Máquina supervisionado, processamento de dados (ETL) e modelagem preditiva com Scikit-Learn.

| Projeto | Descrição | Principais Tecnologias | Link / Repositório |
| :--- | :--- | :--- | :---: |
| **NayarIA - Previsão de Custos de Carro** | Modelo de Machine Learning supervisionado para precificação e previsão de custos automotivos com base em atributos históricos (modelo, marca, ano, quilometragem). | Python, Scikit-Learn, Pandas, Regressão Linear, Árvores de Decisão, One-Hot Encoding | [🔗 Ver Repositório no GitHub](https://github.com/Arthuro08/NayarIA---Previsao-de-Custos-de-Carro) |
| **NayarIA - RH (People Analytics)** | Modelo de Machine Learning para previsão de promoções de funcionários com base em métricas históricas de desempenho, controle de overfitting e validação com train/test split. | Python, Scikit-Learn, Árvores de Decisão (`DecisionTreeClassifier`), Pandas, Excel (.xlsx), CLI Colorida | [🔗 Ver Repositório no GitHub](https://github.com/Arthuro08/NayarIA---RH) |


---

### 🗄️ Sistemas com SQL & Business Intelligence (`sistemas_com_sql/`)
Aplicações de banco de dados relacional (Microsoft SQL Server / T-SQL), modelagens conceituais e lógicas, rotinas programáveis e dashboards analíticos no Power BI.

| Projeto | Descrição | Principais Tecnologias | Documentação |
| :--- | :--- | :--- | :---: |
| **Database Concessionária** | Modelagem relacional para revenda de veículos, restrições de integridade, views, stored procedures, functions e dashboard no Power BI. | SQL Server, T-SQL, Power BI | [Acessar README](sistemas_com_sql/database%20concessionaria/README.md) |
| **Database Ficha Médica** | Sistema para gestão hospitalar com formulário Web em Flask, chaves automáticas via `OUTPUT INSERTED` e documentação técnica. | Python, Flask, SQL Server, pyodbc, HTML5 | [Acessar README](sistemas_com_sql/database%20ficha%20medica/README.md) |
| **Database Futebol BR** | Modelagem relacional e laboratório avançado de consultas, junções (`LEFT`/`RIGHT JOIN`), agregações e dashboard no Power BI. | SQL Server, T-SQL, Power BI | [Acessar README](sistemas_com_sql/database%20futebol/README.md) |
| **Database Authentication** | Sistema de cadastro, login seguro e controle de acesso administrativo via CLI com auditoria em arquivo de logs. | Python, SQL Server, pyodbc | [Acessar README](sistemas_com_sql/database%20authentication/README.md) |

---

### 💻 Soluções em Linguagem C (`solucoes_em_c/`)
Aplicações com foco em fundamentos da ciência da computação, gerenciamento de memória, algoritmos iterativos, structs e validações matemáticas em baixo nível.

| Projeto | Descrição | Principais Conceitos | Documentação |
| :--- | :--- | :--- | :---: |
| **Sistema de Cadastro de Alunos** | Sistema acadêmico com cadastro, busca por matrícula, média geral e cálculo percentual de aprovação. | `struct`, ponteiros, busca linear, vetores | [Acessar README](solucoes_em_c/sistema%20cadastro%20de%20alunos/README.md) |
| **Calculadora Científica** | Calculadora interativa de terminal com operações aritméticas, exponenciação e radiciação com tratamento de exceções. | Modularização, `<math.h>`, `switch-case` | [Acessar README](solucoes_em_c/calculadora/README.md) |
| **Validador de Calendário** | Validador rigoroso de datas do calendário gregoriano com cálculo automático do dia seguinte (virada de mês/ano). | Lógica booleana, condicionais compostas | [Acessar README](solucoes_em_c/calendario/README.md) |
| **Cálculo de Fatorial** | Utilitário para cálculo sequencial de fatoriais com laços otimizados e parada por valor sentinela. | Laços de repetição (`while`, `for`), acumulador | [Acessar README](solucoes_em_c/fatorial/README.md) |

---

### 🐍 Soluções em Python (`solucoes_em_python/`)
Projetos explorando a versatilidade do ecossistema Python: automações, jogos de terminal em tempo real, manipulação de arquivos e análise de dados com Pandas.

| Projeto | Descrição | Principais Recursos | Documentação |
| :--- | :--- | :--- | :---: |
| **Jogo Crash** | Simulação do jogo Crash com apostas, multiplicador dinâmico em tempo real e captura de teclado via `msvcrt`. | Polling de teclado, `msvcrt`, controle de tempo | [Acessar README](solucoes_em_python/crash/README.md) |
| **Jogo de Adivinhação** | Jogo de adivinhação com três níveis de dificuldade, dicas inteligentes, persistência em JSON e tracking de tempo. | `random`, `json`, manipulação de arquivos | [Acessar README](solucoes_em_python/jogo%20adivinha/README.md) |
| **MathMania** | Desafio de agilidade matemática com expressões geradas dinamicamente e histórico de pontuação com timestamp. | Geração procedural, logs temporais, `match-case` | [Acessar README](solucoes_em_python/mathmania/README.md) |
| **Gerenciador de Tarefas** | CRUD de afazeres (*To-Do List*) em terminal com persistência e importação de arquivo `.txt`. | Coleções (`list`), persistência em texto | [Acessar README](solucoes_em_python/task%20manager/README.md) |
| **Análise com Pandas** | Análise exploratória de dados (EDA) a partir de planilha Excel com resumos estatísticos descritivos. | `pandas`, `openpyxl`, DataFrames | [Acessar README](solucoes_em_python/pandas/README.md) |

---

### 🌐 Aplicações Web Front-End, APIs & Deploy (`websites/` & Projetos Live)
Projetos voltados para interfaces de usuário, design responsivo, consumo assíncrono de Web Services REST e deploys em nuvem.

| Projeto | Descrição | Principais Tecnologias | Links de Acesso |
| :--- | :--- | :--- | :---: |
| **Consultor de CEP (Deploy Vercel)** | Aplicação web para consulta e localização de endereços consumindo a API ViaCEP em tempo real, hospedada em nuvem. | HTML5, CSS3, JavaScript ES6+, Bootstrap 5, Fetch API, Vercel | [🌐 Acessar Projeto Online](https://consultor-de-cep-eight.vercel.app/) • [🔗 Repositório](https://github.com/Arthuro08/Consultor-de-CEP) |
| **Consumo de API ViaCEP (Local)** | Versão local da aplicação web com Bootstrap Dark Theme e consumo assíncrono. | HTML5, CSS3, JavaScript ES6+, Fetch API, Bootstrap | [Acessar README](websites/consumo_api_cep/README.md) |
| **Web Portfólio Pessoal** | Website institucional com apresentação profissional, timeline acadêmica, animações e gráfico com Chart.js. | HTML5, CSS3 Responsivo, JavaScript, Chart.js, ScrollReveal | [Acessar README](websites/site_sobre_mim/README.md) |


