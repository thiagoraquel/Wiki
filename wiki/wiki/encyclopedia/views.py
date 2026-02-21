from django.shortcuts import render

from . import util


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
    
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "conteudo": conteudo
    })