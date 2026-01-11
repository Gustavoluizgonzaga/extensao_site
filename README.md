# Extensão Site – Aplicação Web com Flask

Projeto desenvolvido com o objetivo de praticar os fundamentos do desenvolvimento web utilizando o framework Flask. A aplicação consiste em um site institucional simples, com múltiplas rotas e páginas renderizadas a partir de templates HTML.

## Tecnologias Utilizadas
- Python
- Flask
- HTML (templates)

## Funcionalidades
- Página inicial (Homepage)
- Página de produtos
- Página de produto dinâmica via parâmetro na URL
- Página de receitas
- Página de contato
- Página institucional (história)

## Estrutura da Aplicação
A aplicação utiliza o conceito de rotas do Flask para renderizar diferentes páginas HTML:

- `/` → Página inicial  
- `/produtos` → Listagem de produtos  
- `/produtos/<nome_produto>` → Página dinâmica de produto  
- `/receitas` → Página de receitas  
- `/contato` → Página de contato  
- `/historia` → Página institucional  

Cada rota retorna um template HTML utilizando a função `render_template`.

## Objetivo do Projeto
Projeto de caráter educacional, desenvolvido para consolidar conhecimentos em:
- Criação de aplicações web com Flask
- Definição e organização de rotas
- Renderização de templates HTML
- Estrutura básica de um projeto web em Python

## Como Executar o Projeto
1. Clone o repositório
2. Crie um ambiente virtual (opcional, mas recomendado)
3. Instale o Flask:
```bash
pip install flask
