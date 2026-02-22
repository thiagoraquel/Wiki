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