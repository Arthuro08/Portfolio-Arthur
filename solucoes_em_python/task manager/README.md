# ✅ Gerenciador de Tarefas em Python

## 📌 Sobre o Projeto

Este projeto é um gerenciador de tarefas simples desenvolvido em Python para execução no terminal.

Ele permite adicionar, listar, remover e salvar tarefas em um arquivo, funcionando como uma lista de afazeres básica.

O objetivo é praticar manipulação de listas, arquivos e estruturas de controle.

---

## ⚙️ Funcionalidades

- Adicionar tarefas
- Listar tarefas cadastradas
- Remover tarefas por índice
- Salvar tarefas em arquivo
- Carregar tarefas salvas
- Menu interativo no terminal

---

## 🧠 Regras do Sistema

- As tarefas são armazenadas em uma lista em memória
- Cada tarefa recebe um número automaticamente
- A remoção é feita pelo número da tarefa
- Os dados podem ser salvos em arquivo para persistência

---

## 🏗 Estrutura do Código

O projeto utiliza:

- `os` → limpeza do terminal  
- Lista (`list`) → armazenamento das tarefas  
- Arquivos `.txt` → persistência dos dados  

### Principais funções:

- `adicionar()` → adiciona uma nova tarefa  
- `listar()` → exibe todas as tarefas  
- `remover()` → remove uma tarefa  
- `salvar()` → salva no arquivo `tarefas.txt`  
- `carregar()` → carrega tarefas do arquivo  

---

## 💾 Arquivo Gerado

- `tarefas.txt` → armazena a lista de tarefas

---

## ▶️ Como Executar

1. Execute o arquivo:

```bash id="z8n2kl"
python nome_do_arquivo.py
