from django.shortcuts import render, redirect
from app.forms import ReceitasForm, ContasForm, DespesasForm
from app.models import Receita


def home(request):
    data = {}
    data['db'] = Receita.objects.all()
    return render(request, 'index.html', data)

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
        return redirect('/')

def view(request, pk):
    data = {}
    data['db'] = Receita.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Receita.objects.get(pk=pk)
    data['form'] = ReceitasForm(instance=data['db'])
    return render(request, 'form_receita.html', data)

def update(request, pk):
    data = {}
    data['db'] = Receita.objects.get(pk=pk)
    form = ReceitasForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('/')

def delete(request, pk):
    db = Receita.objects.get(pk=pk)
    db.delete()
    return redirect('/')

