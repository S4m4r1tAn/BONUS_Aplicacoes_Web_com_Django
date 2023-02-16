from django.shortcuts import render
from django.shortcuts import HttpResponse

def pagina_inicial(request):
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
