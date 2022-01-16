from django.forms import ModelForm
from app.models import Receita, Contas, Despesas

class ReceitasForm(ModelForm):
    class Meta:
        model = Receita
        fields = ['valor', 'data_recebimento', 'data_recebimento_esperado', 'descricao', 'conta', 'tipo_receita']

class ContasForm(ModelForm):
    class Meta:
        model = Contas
        fields = ['saldo', 'tipo_conta', 'instituicao_financeira']

class DespesasForm(ModelForm):
    class Meta:
        model = Despesas
        fields = ['valor', 'data_pagamento', 'data_pagamento_esperado', 'tipo_despesa', 'conta']