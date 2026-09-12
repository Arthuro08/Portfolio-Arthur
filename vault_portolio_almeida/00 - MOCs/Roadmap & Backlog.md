---
title: Roadmap & Backlog de Melhorias
tipo: planejamento
tags: [planejamento, roadmap, backlog, melhorias]
data_criacao: 2026-09-11
---

# 🚀 Roadmap & Backlog de Evolução dos Projetos

Este documento centraliza as ideias de expansão, refatoração e novas features para cada projeto do portfólio. É um artefato ideal para guiar estudos e demonstrar mentalidade de melhoria contínua de software.

---

## 🗄️ Sistemas com SQL & BI

### [[Database - Concessionaria]]
- [ ] **Módulo de Vendedores & Comissões:** Adicionar tabela `Vendedor` e calcular comissão percentual via Stored Procedure.
- [ ] **Auditoria de Histórico de Preços:** Criar uma trigger (`AFTER UPDATE ON Carro`) que registra alterações de valor em uma tabela `Historico_Preco_Carro`.
- [ ] **Índices de Performance:** Criar índices não-clusterizados (`NONCLUSTERED INDEX`) na coluna `Placa` e nas chaves estrangeiras para otimizar os JOINs.

### [[Database - Ficha Medica]]
- [ ] **Segurança de Acesso:** Implementar autenticação de usuários (médicos e atendentes) usando sessões ou tokens JWT no [[Flask]].
- [ ] **Busca de Pacientes na Web:** Criar rota de busca por RG com retorno assíncrono em JSON na interface web.
- [ ] **Dashboard Hospitalar:** Conectar o [[Power BI]] ao banco `Ficha_Medica` para monitorar tempo médio entre consultas e exames mais solicitados.

### [[Database - Authentication]]
- [ ] **Criptografia de Senhas:** Substituir o armazenamento de senhas em texto puro por hashing seguro com `bcrypt` ou `hashlib` (SHA-256 com salt).
- [ ] **Bloqueio por Tentativas:** Implementar bloqueio temporário de conta após 3 tentativas consecutivas de login incorreto.

---

## 💻 Soluções em C

### [[C - Sistema Cadastro de Alunos]]
- [ ] **Alocação Dinâmica de Memória:** Substituir o vetor estático de 100 posições por memória alocada dinamicamente via `malloc()` e `realloc()`.
- [ ] **Persistência em Arquivo Binário ou CSV:** Salvar os dados dos alunos em disco para não perder os cadastros ao fechar o programa.
- [ ] **Algoritmo de Ordenação:** Implementar ordenação por média decrescente ou ordem alfabética de nomes (usando Bubble Sort ou Quick Sort).

### [[C - Calculadora Cientifica]]
- [ ] **Histórico de Operações:** Guardar os últimos 5 cálculos realizados em uma pilha (stack) ou vetor para consulta rápida.
- [ ] **Operações Trigonométricas:** Adicionar suporte a seno (`sin`), cosseno (`cos`) e tangente (`tan`).

---

## 🐍 Soluções em Python

### [[Python - Jogo Crash]]
- [ ] **Suporte Multiplataforma:** Abstrair o módulo `msvcrt` para permitir execução nativa em Linux/macOS com `curses` ou `termios`.
- [ ] **Gráfico Ascii do Multiplicador:** Renderizar uma linha ou foguete subindo visualmente no terminal enquanto o multiplicador aumenta.

### [[Python - Analise com Pandas]]
- [ ] **Visualização de Dados com Matplotlib / Seaborn:** Gerar gráficos de histograma e dispersão a partir das colunas da planilha.
- [ ] **Tratamento de Dados Nulos:** Adicionar etapas de limpeza (imputação de média/mediana para campos ausentes com `fillna()`).

---

## 🌐 Websites

### [[Web - Consumo API ViaCEP]]
- [ ] **Preenchimento Automático em Formulário:** Permitir preencher automaticamente campos de rua, bairro e cidade de um formulário de checkout a partir do CEP digitado.
- [ ] **Integração com Leaflet / OpenStreetMap:** Exibir um mapa com a localização aproximada do município consultado.

### [[Web - Portfolio Arthur Almeida]]
- [ ] **Seção Dinâmica de Projetos:** Renderizar os cards de projetos consumindo a API pública do GitHub (`https://api.github.com/users/Arthuro08/repos`).
- [ ] **Toggle Dark/Light Mode:** Adicionar alternador de tema com persistência no `localStorage`.

