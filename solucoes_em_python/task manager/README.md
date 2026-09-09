# ✅ Gerenciador de Tarefas em Python

## 📌 Sobre o Projeto
Este projeto é uma aplicação de gerenciamento de tarefas (*To-Do List*) para terminal desenvolvida em Python. O sistema permite criar, visualizar e excluir tarefas pendentes com indexação dinâmica, além de oferecer suporte à persistência em arquivo de texto plano (`tarefas.txt`), permitindo que o usuário salve e recupere suas anotações entre diferentes execuções do programa.

## 🚀 Funcionalidades
- **Adicionar Tarefas:** Inserção de novos itens na lista de afazeres em memória.
- **Listar Tarefas:** Exibição enumerada de todas as tarefas cadastradas no momento.
- **Remover Tarefas:** Exclusão de itens pelo índice correspondente apresentado na listagem.
- **Salvar Lista:** Gravação das tarefas ordenadas em arquivo local (`tarefas.txt`).
- **Carregar Lista:** Leitura e importação de tarefas previamente salvas direto para a memória da aplicação.
- **Menu Interativo:** Navegação simplificada por terminal com atualização de tela.

## 🛠️ Tecnologias, Ferramentas e Bibliotecas
- **Linguagem:** Python 3 (Python 3.10+ recomendado pelo uso de `match-case`)
- **Módulos Nativos Utilizados:**
  - `os`: Limpeza do terminal (`os.system("cls")`) a cada iteração do menu principal.

## 🧠 Conceitos Aplicados
- **Manipulação de Coleções Dinâmicas:** Uso de listas (`list`) com operações de inserção (`append`), remoção por índice (`pop`) e limpeza (`clear`).
- **Persistência de Dados em Arquivo de Texto:** Uso de gerenciadores de contexto (`with open(...)`) nos modos de escrita (`'w'`) e leitura (`'r'`).
- **Tratamento de Exceções (`try / except`):** Captura segura de `FileNotFoundError` ao tentar carregar a lista antes de um arquivo ter sido criado.
- **Estruturas de Seleção:** Organização das rotas do menu através da diretiva `match-case`.

## 📂 Estrutura do Projeto
```text
task manager/
│
├── gerenciadortarefas.py   # Código-fonte principal com funções do CRUD e laço de execução
└── tarefas.txt             # Arquivo texto gerado para armazenamento persistente das tarefas
```

## ▶️ Como Executar

### 1. Pré-requisitos
- Python 3.10+ instalado.

### 2. Execução
No terminal, entre na pasta do projeto e execute:
```bash
python gerenciadortarefas.py
```

### 3. Como Utilizar
1. Digite `1` para adicionar novas tarefas.
2. Digite `2` para visualizar a lista com seus respectivos números identificadores.
3. Digite `3` e insira o número correspondente para remover uma tarefa concluída.
4. Digite `5` para gravar suas tarefas em `tarefas.txt` e `4` para recarregá-las futuramente.
