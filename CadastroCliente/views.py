from django.shortcuts import render

# Create your views here.
def index(request):
    meu_nome = "Gomes"
    lista_frutas = ["Laranja", "Maça", "Banana"]
    context = {
        "nome" : meu_nome,
    }
    return render(request, "index.html", context)
