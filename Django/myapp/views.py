from django.http import *


def index(request):
    text = "<h1>Bienvenue sur mon application django !</h1> <p>Vous pouvez poursuivre la visite du site</p> "

    return HttpResponse(text)


def info(request):
    return HttpResponse("<h2>Page d'informations</h2>")


def blog(request, number, string):
    return HttpResponse("<h1>Blog n°{0}</h1><p>Vous êtes sur le blog {0} qui parle de {1}.</p>".format(number, string))
