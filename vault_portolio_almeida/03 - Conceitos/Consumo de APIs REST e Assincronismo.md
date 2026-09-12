---
title: Consumo de APIs REST e Assincronismo
tipo: conceito
area: web & integracao
tecnologia_principal: JavaScript
tags: [conceito, web, api, rest, async-await, fetch, json, promises]
data_criacao: 2026-09-11
---

# 🌐 Consumo de APIs REST & Assincronismo em JavaScript

A comunicação cliente-servidor moderna baseia-se em requisições assíncronas através do protocolo HTTP, consumindo endpoints no padrão REST (*Representational State Transfer*) e trafegando dados em formato JSON.

---

## ⚡ 1. O Modelo Assíncrono com `async / await`
Em [[JavaScript]], operações de rede não bloqueiam a thread principal do navegador. Ao marcar uma função como `async`, podemos utilizar `await` para pausar a execução local até que uma `Promise` seja resolvida de maneira limpa e legível.

```javascript
// Exemplo em [[Web - Consumo API ViaCEP]]:
async function buscar() {
    const response = await fetch(`https://viacep.com.br/ws/${cep}/json/`);
    const data = await response.json();
    console.log(data.logradouro);
}
```

---

## 🔍 2. Ciclo de Vida da Requisição
1. **Trigger de Evento:** Clique de botão ou submissão de formulário.
2. **Sanitização:** Limpeza de máscaras e caracteres não numéricos (`replace(/-/g, "")`).
3. **Validação Defensiva:** Verificação prévia de formato para evitar requisições desnecessárias ao servidor externo.
4. **Fetch HTTP:** Disparo da requisição `GET`.
5. **Parsing:** Deserialização do payload JSON em objeto JavaScript manipulável.
6. **Atualização do DOM:** Injeção seletiva dos dados recebidos na interface do usuário.

---

## 🔗 Projetos Relacionados
- [[Web - Consumo API ViaCEP]]
- [[Database - Ficha Medica]]

