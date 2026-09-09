# 📬 Consultor de Endereço via API ViaCEP

## 📌 Sobre o Projeto
Este projeto é uma aplicação web interativa desenvolvida com HTML5, CSS3, Bootstrap 5 e JavaScript Moderno (ES6+) para consulta e localização de logradouros em todo o território nacional. A aplicação consome a API REST pública do serviço **ViaCEP**, enviando requisições assíncronas para obter dados completos de endereço a partir do Código de Endereçamento Postal (CEP) digitado pelo usuário.

## 🚀 Funcionalidades
- **Higienização e Sanitização do CEP:** Remoção automática de hífens (`-`) permitindo que o usuário digite o CEP formatado ou apenas em dígitos.
- **Validação Defensiva no Front-End:**
  - Verificação de tamanho exato (8 dígitos numéricos).
  - Bloqueio de caracteres alfabéticos ou especiais com aviso imediato de erro.
- **Consumo Assíncrono de API REST:** Requisição em tempo real para os endpoints públicos do ViaCEP (`https://viacep.com.br/ws/{cep}/json/`).
- **Tratamento de CEP Inexistente:** Checagem da flag `erro` retornada pelo serviço web.
- **Renderização Dinâmica do Endereço:** Exibição estruturada no DOM com:
  - Rua / Logradouro
  - Complemento
  - Bairro
  - Cidade / Localidade
  - Unidade Federativa (UF / Estado)
- **Interface com Dark Mode:** Integração com Bootstrap 5 configurado para tema escuro nativo.

## 🛠️ Tecnologias, Ferramentas e Bibliotecas
- **Front-End:** HTML5 semântico e CSS3
- **Linguagem:** JavaScript (ES6+ / Vanilla JS)
- **Framework CSS:** Bootstrap 5.3 (via CDN) com atributo `data-bs-theme="dark"`
- **API Externa:** [ViaCEP WebService](https://viacep.com.br/) (REST / JSON)

## 🧠 Conceitos Aplicados
- **Programação Assíncrona:** Utilização de `async/await` e da Fetch API nativa para comunicação assíncrona sem recarregar a página (*Single Page behavior*).
- **Manipulação do DOM:** Seleção de nós com `document.getElementById` e injeção dinâmica de conteúdo via `innerText`.
- **Expressões Regulares e Tratamento de Strings:** Remoção global de caracteres indesejados (`replace(/-/g, "")`).
- **Design Responsivo e UI:** Ajustes visuais com flexbox e classes utilitárias do Bootstrap.

## 📂 Estrutura do Projeto
```text
consumo_api_cep/
│
├── index.html      # Estrutura visual, formulário de busca e links de CDN
├── script.js       # Lógica assíncrona, validações e consumo da API ViaCEP
└── style.css       # Estilizações complementares da interface
```

## ▶️ Como Executar

### 1. Pré-requisitos
- Um navegador de internet atualizado (Chrome, Edge, Firefox, etc.).
- Conexão com a internet (para download dos assets do Bootstrap e consumo da API ViaCEP).

### 2. Execução
1. Navegue até a pasta `websites/consumo_api_cep/`.
2. Abra o arquivo `index.html` com um duplo clique no navegador, ou utilize a extensão **Live Server** no VS Code.
3. Digite um CEP válido (com ou sem hífen, ex: `01001-000` ou `01001000`) e clique no botão **Buscar CEP**.

