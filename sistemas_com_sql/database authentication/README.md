# 🔐 Sistema de Autenticação com SQL Server e Python

## 📌 Sobre o Projeto
Este projeto é uma aplicação de autenticação e gerenciamento de usuários desenvolvida em Python com integração direta ao banco de dados relacional Microsoft SQL Server. O sistema opera via interface de linha de comando (CLI), permitindo cadastrar novos usuários com validações rigorosas de credenciais, autenticar acessos e gerenciar contas através de um módulo administrativo protegido. Além disso, todas as ações críticas de cadastro são registradas com data e hora em um arquivo de log para fins de auditoria.

## 🚀 Funcionalidades
- **Cadastro de Usuários:** Criação de novas contas com verificação de unicidade de nome de usuário e validação de tamanho e confirmação de senha.
- **Login e Autenticação:** Validação de credenciais diretamente contra a tabela do banco de dados.
- **Painel Administrativo:** Área restrita protegida por senha mestre, permitindo:
  - Listagem completa dos usuários cadastrados com seus respectivos identificadores (`ID_Usuario`).
  - Exclusão de usuários do banco de dados por ID.
- **Auditoria e Logs:** Registro automático de cadastros em arquivo de texto (`logs.txt`), incluindo data e hora exatas do evento.
- **Interface Interativa:** Menu intuitivo no terminal com limpeza automática de tela para melhor legibilidade.

## 🛠️ Tecnologias, Ferramentas e Bibliotecas
- **Linguagem:** Python 3
- **Banco de Dados:** Microsoft SQL Server (T-SQL)
- **Bibliotecas Python:**
  - `pyodbc`: Comunicação e execução de queries SQL parametrizadas junto ao SQL Server.
  - `datetime`: Captura e formatação de carimbos de data/hora para os logs.
  - `os`: Manipulação de comandos do sistema operacional (limpeza de terminal com `cls`).
  - `time`: Controle de pausas e fluxo de mensagens temporizadas no terminal.

## 🧠 Conceitos Aplicados
- **Integração Python + SGBD:** Abertura de conexões, gerenciamento de cursores e confirmação de transações (`commit`).
- **Segurança e Prevenção a Injeção de SQL:** Uso de queries parametrizadas com placeholders (`?`) no `pyodbc`.
- **Validação e Tratamento de Regras de Negócio:**
  - `Username`: obrigatório, máximo de 20 caracteres e checagem de duplicação.
  - `Senha`: entre 8 e 20 caracteres e confirmação obrigatória de senha idêntica.
- **Controle de Acesso Baseado em Papéis:** Separação entre fluxo de usuário comum e permissões administrativas com credencial mestra.
- **Auditoria e Persistência em Arquivo:** Abertura de arquivos em modo append (`'a'`) para registro contínuo de eventos.

## 📂 Estrutura do Projeto
- `autenticacao.py`: Script principal contendo o fluxo CLI, menus, validações e chamadas SQL.
- `database_users.sql`: Script DDL para criação da base de dados `Users_Sistema`, tabela `Usuario` e carga inicial de teste.
- `logs/logs.txt`: Arquivo de texto gerado para armazenamento do histórico de cadastros.

## ▶️ Como Executar

### 1. Pré-requisitos
- Python 3.8+ instalado.
- Instância ativa do Microsoft SQL Server.
- Driver ODBC para SQL Server configurado.
- Instalação da biblioteca `pyodbc`:
  ```bash
  pip install pyodbc
  ```

### 2. Configuração do Banco de Dados
1. Abra o SQL Server Management Studio (SSMS) ou Azure Data Studio.
2. Execute o script `database_users.sql` para criar o banco de dados `Users_Sistema` e a tabela `Usuario`.

### 3. Execução da Aplicação
1. No arquivo `autenticacao.py`, certifique-se de que a string de conexão aponte para o seu servidor local (ajuste o parâmetro `Server` se necessário):
   ```python
   config = pyodbc.connect(
       'Driver={SQL Server};'
       'Server=SEU_SERVIDOR;'
       'Database=Users_Sistema;'
       'Trusted_Connection=yes;'
   )
   ```
2. Execute o script via terminal:
   ```bash
   python autenticacao.py
   ```
3. Utilize as opções numéricas do menu para cadastrar, logar ou acessar o menu administrativo.
