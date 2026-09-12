---
title: Web - Consumo API ViaCEP
tipo: projeto
area: front-end & integracao
tecnologias: [JavaScript, HTML5, CSS3, Bootstrap, REST]
status: concluído
tags: [projeto, web, javascript, async-await, fetch, viacep, api, bootstrap]
data_criacao: 2026-09-11
repositorio: "websites/consumo_api_cep"
---

# 📬 Web - Consultor de Endereço via API ViaCEP

## 📌 Visão Geral
Aplicação web front-end desenvolvida com HTML5, CSS3, [[Bootstrap]] e [[JavaScript]] moderno (ES6+) para busca dinâmica de endereços e logradouros em todo o território nacional. A aplicação consome de forma assíncrona o Web Service público do **ViaCEP**, atualizando a tela em tempo real sem recarregar a página (*SPA experience*).

---

## 🚀 Arquitetura & Fluxo Assíncrono ([[Consumo de APIs REST e Assincronismo]])
A função `buscar()` no arquivo `script.js` encapsula todo o pipeline:

```javascript
async function buscar(){
    var cep = document.getElementById("cep").value;
    cep = cep.replace(/-/g , ""); // Sanitização de caracteres

    // Validação defensiva (tamanho e dígitos numéricos)
    if(cep.length != 8 || isNaN(cep)){
        document.getElementById("resultado").innerText = "ERRO: CEP Inválido!";
        return;
    }

    // Requisição HTTP GET assíncrona
    const response = await fetch(`https://viacep.com.br/ws/${cep}/json/`);
    const data = await response.json();

    if(data.erro){
        document.getElementById("resultado").innerText = "ERRO: CEP não encontrado.";
    } else {
        var result = `Rua: ${data.logradouro}\nComplemento: ${data.complemento}\nBairro: ${data.bairro}\nCidade: ${data.localidade}\nEstado: ${data.uf}\n`;
        document.getElementById("resultado").innerText = result;
    }
}
```

---

## 🎨 Interface e Estilização
- Uso do framework [[Bootstrap]] versão 5.3 com modo escuro nativo ativado via atributo `data-bs-theme="dark"`.
- Estilização customizada complementar em `style.css`.

---

## 🔗 Links e Notas Relacionadas
- **Tecnologias:** [[JavaScript]], [[Bootstrap]]
- **Conceitos:** [[Consumo de APIs REST e Assincronismo]]
- **Evolução:** [[Roadmap & Backlog]]

