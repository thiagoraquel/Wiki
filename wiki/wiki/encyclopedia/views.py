from django.shortcuts import render, redirect
import markdown2
from . import util
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    conteudo = util.get_entry(title)

    if conteudo is None:
        return render(request, "encyclopedia/error.html", {
            "message": "A página '{title}' não foi encontrada."
        })
    
    conteudo_convertido = markdown2.markdown(conteudo)
    
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": conteudo_convertido
    })

def search(request):
    query = request.GET.get('q', '')

    todas_paginas = util.list_entries()

    for pagina in todas_paginas:
        if query.lower() == pagina.lower():
            return redirect('entry', title=pagina)
        
    resultados_parciais = []
    for pagina in todas_paginas:
        if query.lower() in pagina.lower():
            resultados_parciais.append(pagina)

    return render(request, "encyclopedia/search.html", {
        "resultados": resultados_parciais,
        "query": query
    })

def random_page(request):
    todas_paginas = util.list_entries()

    pagina_sorteada = random.choice(todas_paginas)

    return redirect('entry', title=pagina_sorteada)

def create(request):
    if request.method == "POST":
        titulo = request.POST.get("title")
        conteudo = request.POST.get("content")

        if util.get_entry(titulo) is not None:
            return render(request, "encyclopedia/error.html", {
                "message": f"Erro: A enciclopédia já possui um artigo chamado '{titulo}'."
            })
        else:
            util.save_entry(titulo, conteudo)
            
            return redirect('entry', title=titulo)
        
    return render(request, "encyclopedia/create.html")

def edit(request, title):
    if request.method == "POST":
        novo_conteudo = request.POST.get("content")
        util.save_entry(title, novo_conteudo)
        return redirect('entry', title=title)
    
    else:
        conteudo_original = util.get_entry(title)

        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": conteudo_original
    })