
from django.db import models

class Receita(models.Model):
    valor = models.CharField(max_length=200)
    data_recebimento =  models.CharField(max_length=200)
    data_recebimento_esperado =  models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    conta = models.CharField(max_length=200)
    tipo_receita = models.CharField(max_length=200)

class Contas(models.Model):
    saldo = models.CharField(max_length=200)
    tipo_conta = models.CharField(max_length=200)
    instituicao_financeira = models.CharField(max_length=200)

class Despesas(models.Model):
    valor = models.CharField(max_length=200)
    data_pagamento = models.CharField(max_length=200)
    data_pagamento_esperado = models.CharField(max_length=200)
    tipo_despesa = models.CharField(max_length=200)
    conta = models.CharField(max_length=200)





