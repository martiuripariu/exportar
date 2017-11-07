from django.conf.urls import url
from core.views import index 
from core import views


urlpatterns = [

    # se o usuário nao digitar um endereço específico, vai oara o index
    url(r'^$', index),

    # registra o caminho e faz o link da função export_users_csv no arquivo views.py
    url(r'^export/csv/$', views.export_users_csv, name='export_users_csv'),

]
