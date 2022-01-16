from django.shortcuts import render, redirect
from app.forms import ReceitasForm, ContasForm, DespesasForm

# Create your views here.

from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')

def cadastro_receita(request):
    data = {}
    data['form'] = ReceitasForm()
    return render(request, 'form_receita.html', data)

def contas(request):
    data= {}
    data['form'] = ContasForm()
    return render(request, 'form_contas.html', data)

def despesas(request):
    data = {}
    data['form'] = DespesasForm
    return render(request, 'form_despesas.html', data)

def create(request):
    form = ReceitasForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')


