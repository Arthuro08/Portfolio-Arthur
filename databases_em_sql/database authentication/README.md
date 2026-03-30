# 🔐 Sistema de Autenticação com SQL Server (Python)

## 📌 Sobre o Projeto

Este projeto é um sistema de autenticação de usuários desenvolvido em Python com integração ao SQL Server.

Ele permite cadastro, login e gerenciamento de usuários, incluindo uma área administrativa com controle sobre os registros armazenados no banco de dados.

O objetivo é praticar integração com banco de dados, manipulação de dados e lógica de autenticação.

---

## ⚙️ Funcionalidades

- Cadastro de usuários
- Sistema de login
- Validação de credenciais
- Área administrativa protegida por senha
- Listagem de usuários
- Remoção de usuários
- Integração com SQL Server

---

## 🧠 Regras do Sistema

- **Username**
  - Máximo de 20 caracteres
  - Não pode ser duplicado

- **Senha**
  - Entre 8 e 20 caracteres
  - Deve ser confirmada no cadastro

- **Administrador**
  - Acesso por senha fixa no código
  - Pode listar e remover usuários

---

## 🏗 Estrutura do Código

Bibliotecas utilizadas:

- `pyodbc` → conexão com SQL Server  
- `os` → limpeza do terminal  
- `time` → delays e controle de execução  

### Principais funções:

- `cadastrar()` → registra novos usuários  
- `login()` → autentica usuários  
- `adm()` → menu administrativo  
- `admlistar()` → exibe usuários  
- `admremover()` → remove usuários  

---

## 🗄 Banco de Dados

Execute o script abaixo no SQL Server para criar o banco:

```sql
CREATE DATABASE Users_Sistema
GO
USE Users_Sistema

CREATE TABLE Usuario(
    ID_Usuario int PRIMARY KEY IDENTITY(1,1) NOT NULL,
    Username varchar(20) NOT NULL,
    Senha VARCHAR(20) NOT NULL
);

INSERT INTO Usuario(Username, Senha) VALUES
('NpcTeste1', '1234abcd'),
('NpcTeste2', '4321dcba');

SELECT * FROM Usuario;
