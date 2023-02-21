from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Investimento
from .forms import InvestimentoForm

""" def pagina_inicial(request):
    return HttpResponse('Pronto para investir!')

def contato(request):
    return HttpResponse('Para duvidas enviar email para: S4m4r1t4N@devaprender.com')

def minha_historia(request):
    pessoa = {
        'nome': 'Jeff',
        'idade': '28',
        'hobby': 'Games',
    }
    return render(request, 'investimentos/minha_historia.html', pessoa)

def novo_investimento(request):
    return render(request, 'investimentos/novo_investimento.html')

def investimento_registrado(request):
    investimento = {
        'tipo_investimento': request.POST.get('TipoInvestimento')
    }
    return render(request, 'investimentos/investimento_registrado.html', investimento) """

def investimentos(request):
    dados = {
        'dados': Investimento.objects.all()
    }
    return render(request, 'investimentos/investimentos.html', context=dados)

def detalhe(request, id_investimento):
    dados = {
        'dados': Investimento.objects.get(pk=id_investimento)
    }
    return render(request, 'investimentos/detalhe.html', dados)

def criar(request):
    investinento_form = InvestimentoForm()
    formulario = {
        'formulario': investinento_form
    }
    return render(request, 'investimentos/novo_investimento.html', context=formulario)