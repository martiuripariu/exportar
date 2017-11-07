# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Tabela(models.Model):
	nome = models.CharField(max_length=30)
	email= models.EmailField(blank=True)
	dt_nasc = models.DateField()
	telefone = models.CharField(max_length=100, blank=True)
