# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Tabela

def index(request):
    var = "Projeto em Django com banco de dados simples, publicado no GIT, para executar testes de códigos"
    lista = Tabela.objects.all()
    return render(request, 'index.html',{'var':var,'registro':lista})

    ########## insira seu codigo de testes aqui---- ##############




















    ########### ---- ##############
