 #CARACTERES UTF-8
from __future__ import unicode_literals

#renderizar (montar) nosso modelo
from django.shortcuts import render

#IMPORTA A "TABELA" DO BANCO CRIADA EM MODELS
from .models import Tabela

# IMPORTA DO DJANGO A FUNÇÃO CSV
import csv

 #CONTEM METADADOS SOBRE A REQUISIÇÃO
from django.http import HttpResponse




# ESTA FUNÇÃO PERMITE QUE A PAGINA INDEX SEJA EXBIDA
def index(request):

    # PODENDO INSER VARIÁVEIS
    var = "Projeto em Django com banco de dados simples, publicado no GIT, para executar testes de códigos"

    #E ATÉ A LISTA DE UMA BASE DE dados
    lista = Tabela.objects.all()

    # O  return render, RENDERIZA TUDO E RETORNA PARA O INDEX CONSUMIR
    return render(request, 'index.html',{'var':var,'registro':lista})


# ESTA FUNÇÃO É CHAMADA LÁ NO HTML, AQUI COMEÇA A SER CRIADO O ARQUIVO CSV
def export_users_csv(request):

    # response É UMA VARAÁVEL QUE RECEBE AS INFORMAÇOES NECESSÁRIAS PARA CRIAR O ARQUIVO
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Tabela.csv"'

    # O É MONTADO O CABEÇALHO DA TABELA (NOME DOS CAMPOS) PODENDO SER "DATA DE NASCIMENTO" AO INVES DE "dt_nasc"
    writer = csv.writer(response)
    writer.writerow(['id', 'nome', 'email', 'dt_nasc', 'telefone'])

    #LÊ O BANCO E ARMAZENA NA VARIAVEL LISTA TODOS  OS REGISTROS
    lista = Tabela.objects.all().values_list('id', 'nome', 'email', 'dt_nasc', 'telefone')

    #A CONDIÇÃO "FOR" VARRE TODOS OS REGISTROS MONTANDO A TABEA NO ARQUIVO.CSV
    for registro in lista:
        writer.writerow(registro)

    #RETORNA COM O ARQUIVO MONTADO.
    return response















    ########### ---- ##############
