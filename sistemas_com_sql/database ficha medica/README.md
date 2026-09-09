# 🏥 Sistema de Ficha Médica - SQL Server, Python & Flask

## 📌 Sobre o Projeto
Este projeto é um sistema integrado para gestão de prontuários e fichas médicas hospitalares. A solução contempla a modelagem relacional completa do histórico médico de pacientes e uma aplicação web desenvolvida com o microframework Flask (Python), permitindo que recepcionistas ou médicos preencham fichas cadastrais completas através de um formulário web e persistam os dados de forma transacional no banco de dados Microsoft SQL Server.

O projeto inclui documentação detalhada em PDF com todo o processo de levantamento de requisitos, normalização e regras de modelagem aplicadas.

## 🚀 Funcionalidades
- **Cadastro Centralizado de Paciente:** Registro de dados pessoais (Nome, RG, Data de Nascimento, Sexo, Convênio e Estado Civil) com garantia de unicidade de documento.
- **Relacionamentos 1:N Automatizados:**
  - Cadastro de endereço vinculado ao paciente gerado.
  - Cadastro de múltiplos contatos telefônicos.
  - Registro de consultas médicas (médico responsável, data e diagnóstico).
  - Associação de exames solicitados diretamente vinculados à consulta médica.
- **Prevenção de Duplicidade:** Validação via SQL para impedir múltiplos cadastros com o mesmo RG.
- **Gestão Transacional com Chaves Geradas:** Utilização da cláusula `OUTPUT INSERTED` do T-SQL para capturar chaves primárias recém-geradas pelo banco e vincular registros dependentes em tempo real.
- **Interface Web:** Formulário HTML intuitivo (`templates/index.html`) para submissão direta dos dados.

## 🛠️ Tecnologias, Ferramentas e Bibliotecas
- **Back-End:** Python 3
- **Framework Web:** Flask (`render_template`, `request`, `jsonify`)
- **Banco de Dados:** Microsoft SQL Server (T-SQL)
- **Conector de Banco:** `pyodbc`
- **Front-End:** HTML5 / CSS3
- **Documentação e Modelagem:** BrModelo, PDF descritivo e diagramas conceituais/lógicos em PNG

## 🧠 Conceitos Aplicados
- **Modelagem Relacional de Dados:** Cardinalidades 1:N entre Paciente, Endereço, Telefone, Consulta e Exames.
- **Transações e Integridade Referencial:** Encapsulamento de múltiplos `INSERT`s com `config.commit()` para manter a integridade dos registros correlacionados.
- **Cláusula T-SQL `OUTPUT INSERTED`:** Resgate seguro e atômico da chave de auto-incremento sem depender de `@@IDENTITY` ou `SCOPE_IDENTITY()`.
- **Arquitetura Web Cliente-Servidor:** Roteamento de requisições `GET` e tratamento de payloads de formulário via `POST`.
- **Validação de Entrada:** Tratamento prévio para duplicidade de documentos no banco.

## 📂 Estrutura do Projeto
```text
database ficha medica/
│
├── database_ficha.sql                  # Script DDL com criação das tabelas e chaves estrangeiras
├── fichaAPI.py                         # Servidor Flask com rotas e integração via pyodbc
├── templates/
│   └── index.html                      # Interface visual do formulário de cadastro médico
│
├── Modelo Conceitual - Ficha Médica.png # Diagrama conceitual de entidades
├── Modelo Lógico - Ficha Médica.png    # Diagrama lógico com chaves primárias e estrangeiras
├── Ficha Médica.png                    # Exemplo visual da ficha cadastral
└── Projeto - Ficha Médica em SQL.pdf   # Documentação técnica e memorial descritivo completo
```

## ▶️ Como Executar

### 1. Pré-requisitos
- Python 3.8+ instalado.
- Instância ativa do Microsoft SQL Server.
- Driver ODBC para SQL Server configurado.
- Dependências Python:
  ```bash
  pip install flask pyodbc
  ```

### 2. Configuração do Banco de Dados
1. Abra o **SQL Server Management Studio (SSMS)** ou ferramenta equivalente.
2. Execute o script `database_ficha.sql` para criar o banco de dados `Ficha_Medica` e as tabelas `Paciente`, `Endereco`, `Telefone`, `Consulta` e `Exame`.

### 3. Configuração e Execução do Servidor Web
1. No arquivo `fichaAPI.py`, confira se a string de conexão aponta para o seu servidor local:
   ```python
   config = pyodbc.connect(
       'Driver={SQL Server};'
       'Server=SEU_SERVIDOR;'
       'Database=Ficha_Medica;'
       'Trusted_Connection=yes;'
   )
   ```
2. Inicie o servidor Flask:
   ```bash
   python fichaAPI.py
   ```
3. Abra o navegador e acesse:
   ```text
   http://127.0.0.1:5000/
   ```
4. Preencha os dados no formulário e clique em cadastrar para testar a persistência no banco de dados.