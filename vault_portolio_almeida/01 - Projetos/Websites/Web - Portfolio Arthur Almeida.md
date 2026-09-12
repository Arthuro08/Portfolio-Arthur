---
title: Web - Portfolio Arthur Almeida
tipo: projeto
area: front-end & portfolio
tecnologias: [JavaScript, HTML5, CSS3, Chart.js, ScrollReveal]
status: concluído
tags: [projeto, web, portfolio, institucional, responsividade, chartjs, animations]
data_criacao: 2026-09-11
repositorio: "websites/site_sobre_mim"
---

# 🌐 Web - Portfólio Pessoal Arthur Almeida

## 📌 Visão Geral
Website institucional e vitrine profissional de Arthur Almeida. Desenvolvido com HTML5 semântico, folhas de estilo CSS3 customizadas e modularizadas para design responsivo (`style.css` e `responsive.css`), além de scripts [[JavaScript]] para animações de rolagem e visualização de dados interativa com **Chart.js**.

---

## 🎨 Seções da Aplicação
1. **Header com Navegação Suave:** Âncoras para as seções Sobre Mim, Habilidades e Contato.
2. **Hero Section:** Apresentação visual, foto de perfil, linguagens dominadas e cargo (*Aspiring Full-Stack Developer*).
3. **Trajetória Acadêmica:**
   - Ensino Médio Técnico em Desenvolvimento de Sistemas (ETEC de Taboão da Serra | 2022–2024).
   - Ensino Superior / Bacharelado em Sistemas de Informação (IFSP Campus São Paulo | 2025–2028).
4. **Habilidades & Gráfico Interativo:**
   - Gráfico tipo pizza (*pie chart*) estilizado com Chart.js demonstrando competências em HTML/CSS, JS, C/C++, SQL e Python.
   - Grade de badges com ícones oficiais de cada tecnologia.
5. **Rodapé & Contato:** Links diretos para LinkedIn, GitHub e E-mail com ícones FontAwesome.
6. **Botão Voltar ao Topo:** Componente dinâmico que detecta a rolagem vertical (`window.scrollY > 10`) e retorna suavemente ao início.

---

## 💡 Destaque Técnico: Animações & Gráfico
- **ScrollReveal:** Efeito de revelação progressiva dos elementos ao navegar pela página:
  ```javascript
  const sr = ScrollReveal({delay: 200, origin: 'bottom', distance: '60px'});
  sr.reveal('.principal', {reset: false});
  sr.reveal('.trajetoria', {delay: 100, reset: true});
  ```
- **Chart.js:** Customização de cores, bordas, fontes (Poppins) e legenda responsiva à direita do canvas.

---

## 🔗 Links e Notas Relacionadas
- **Tecnologias:** [[JavaScript]]
- **Evolução:** [[Roadmap & Backlog]]

