from django.shortcuts import render
from django.conf import settings


def index(request):
    ''' Função para Reenderizar index.html '''
    return render(request, "index.html", {
        'debug':settings.DEBUG,
        'environment':settings.ENVIRONMENT
        })