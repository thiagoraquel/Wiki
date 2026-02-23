# CS50W - Project 1: Wiki 📚

Uma enciclopédia online no estilo Wikipédia, desenvolvida como o segundo projeto do curso **CS50’s Web Programming with Python and JavaScript** de Harvard.

## 🎯 Objetivo do Projeto
O objetivo deste projeto é construir uma aplicação web dinâmica utilizando o framework **Django** (Python). Diferente de sites estáticos, esta aplicação processa rotas, lê e grava dados no servidor e converte marcações de texto dinamicamente utilizando a arquitetura MVT (Model-View-Template).

## ✨ Funcionalidades
* **Página de Artigos (Entry Page):** Acesso a conteúdos dinâmicos através de rotas (`/wiki/TITLE`). O sistema renderiza arquivos `.md` e os converte nativamente para HTML.
* **Busca Inteligente (Search):** * Redirecionamento automático para a página do artigo em caso de correspondência exata.
  * Geração dinâmica de uma página de "Resultados" listando correspondências parciais se a busca não for exata.
* **Criação de Páginas (New Page):** Formulário processado via requisição **POST** que permite aos usuários criar novos artigos usando sintaxe Markdown e salva os arquivos fisicamente no servidor, com validação contra títulos duplicados.
* **Edição de Páginas (Edit Page):** Funcionalidade que pré-carrega o conteúdo Markdown existente de um artigo em um formulário (GET) e permite sua atualização no servidor (POST).
* **Página Aleatória (Random Page):** Um botão que utiliza a biblioteca nativa do Python para sortear e redirecionar o usuário para um artigo aleatório da enciclopédia.
* **Conversão Markdown-HTML:** Utilização da biblioteca `markdown2` para o processamento léxico e conversão do conteúdo salvo para a exibição no front-end.

## 🛠️ Tecnologias Utilizadas
* **Back-end:** Python, Django (Rotas, Views, Templates)
* **Front-end:** HTML5, CSS3, Bootstrap (Sistema de Grid Responsivo)
* **Processamento de Dados:** Manipulação direta de arquivos Markdown (`.md`)

## 🚀 Como Executar o Projeto Localmente

Para rodar este projeto na sua máquina, siga os passos abaixo:

1. Clone este repositório:
   ```bash
   git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)

2.   Acesse a pasta do projeto:
    cd wiki

3.  Crie e ative um ambiente virtual (recomendado):
    python -m venv venv
    # No Windows:
    .\venv\Scripts\activate
    # No Mac/Linux:
    source venv/bin/activate

4.  Instale as dependências:
    pip install Django markdown2

5. Incie o servidor de desenvolvimento:
    python manage.py runserver

6.  Acesse http://127.0.0.1:8000/