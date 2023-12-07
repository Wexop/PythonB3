from django.http import *
from django.shortcuts import render


def index(request):
    context = {"name": 'Matt', "list_article": ["Dévelopement", "Réseau", "Jeux", "Sécurité", "Tech"]}

    return render(request, 'myapp/index.html', context=context)


def info(request):
    return HttpResponse("<h2>Page d'informations</h2>")


def blog(request, number, string):
    return HttpResponse("<h1>Blog n°{0}</h1><p>Vous êtes sur le blog {0} qui parle de {1}.</p>".format(number, string))
