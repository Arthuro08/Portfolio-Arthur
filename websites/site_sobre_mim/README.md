# 🌐 Web Portfólio Pessoal - Arthur Almeida

## 📌 Sobre o Projeto
Este projeto é o website institucional e portfólio pessoal de **Arthur Almeida**, desenvolvido com foco em apresentação profissional, trajetória acadêmica e exposição de competências técnicas. O site combina design moderno, responsividade para múltiplos dispositivos móveis e desktops, animações dinâmicas de revelação de conteúdo e visualização gráfica interativa das tecnologias dominadas.

## 🚀 Funcionalidades
- **Apresentação & Hero Section:** Saudação introdutória com foto de perfil, papel de atuação (*Aspiring Full-Stack Developer*) e lista das principais linguagens.
- **Trajetória Acadêmica:** Timeline estruturada destacando a formação técnica em Desenvolvimento de Sistemas (ETEC de Taboão da Serra, 2022–2024) e graduação em Sistemas de Informação (IFSP Campus São Paulo, 2025–2028).
- **Painel Visual de Habilidades (Skills):**
  - Gráfico interativo em pizza (*pie chart*) renderizado via biblioteca Chart.js ilustrando a distribuição de domínio entre HTML/CSS, JavaScript, C/C++, SQL e Python.
  - Vitrine de tecnologias com ícones das linguagens, frameworks e bancos de dados (C#, React, MySQL, SQL Server, Bootstrap, Git, etc.).
- **Animações Fluidas:** Efeitos visuais de surgimento (*fade-in* e *scroll-up*) em tempo real acionados durante a rolagem da página.
- **Botão Voltar ao Topo (Back to Top):** Botão flutuante dinâmico que surge após rolar a página e realiza o retorno suave ao início.
- **Área de Contato:** Links diretos para perfis profissionais (GitHub, LinkedIn) e correio eletrônico.
- **Design Totalmente Responsivo:** Adaptação completa de layouts e fontes para smartphones, tablets e monitores widescreen.

## 🛠️ Tecnologias, Ferramentas e Bibliotecas
- **Linguagens Base:** HTML5 semântico, CSS3 e Vanilla JavaScript (ES6+)
- **Bibliotecas Externas (CDN):**
  - **Chart.js:** Renderização do gráfico interativo de proficiências no elemento `<canvas>`.
  - **ScrollReveal:** Biblioteca JavaScript para acionamento de animações orientadas a rolagem.
  - **Font Awesome:** Pacote de ícones vetoriais para links de contato e navegação.
  - **Google Fonts:** Tipografia moderna utilizando a família de fontes *Poppins*.

## 🧠 Conceitos Aplicados
- **Layout Responsivo:** Utilização de Media Queries CSS (`responsive.css`), Flexbox e CSS Grid para adaptação flexível de telas.
- **Manipulação do DOM e Event Listeners:**
  - Monitoramento do evento de rolagem da janela (`window.addEventListener('scroll', ...)`) para exibir/ocultar o botão flutuante.
  - Evento de clique para rolagem programática ao topo com `window.scrollTo(0, 0)`.
- **Customização de Gráficos em Canvas:** Configuração global de temas, fontes e legendas responsivas utilizando a API do Chart.js.
- **Organização Modular de Assets:** Separação estrita de arquivos em diretórios dedicados (`css/`, `js/` e `imagens/`).

## 📂 Estrutura do Projeto
```text
site_sobre_mim/
│
├── index.html              # Estrutura principal da página web e seções
│
├── css/
│   ├── style.css           # Estilos globais, temas de cores e tipografia
│   └── responsive.css      # Regras de media queries para telas menores
│
├── js/
│   ├── script.js           # Controle de animações (ScrollReveal) e botão voltar ao topo
│   └── charts.js           # Inicialização e estilização do gráfico com Chart.js
│
└── imagens/                # Fotografias, ícones de stacks técnicas e brasões institucionais
```

## ▶️ Como Visualizar

### 1. Pré-requisitos
- Um navegador web moderno (Google Chrome, Firefox, Microsoft Edge, Safari ou Opera).

### 2. Execução Local
1. Navegue até o diretório `websites/site_sobre_mim/`.
2. Dê um duplo clique no arquivo `index.html` para abri-lo diretamente no navegador.
3. *(Opcional)* Se estiver utilizando o Visual Studio Code, você pode clicar com o botão direito em `index.html` e selecionar **Open with Live Server**.
