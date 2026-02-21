from django.shortcuts import render
import markdown2
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
    
    conteudo_convertido = markdown2.markdown(conteudo)
    
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": conteudo_convertido
    })