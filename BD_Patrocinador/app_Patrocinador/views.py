from django.shortcuts import render
from .models import Patrocinador

def home(request):
    return render(request, 'cadastro/home.html')

def cadastros(request):
    novo_Patroconador = Patrocinador()
    novo_Patroconador.nome = request.POST.get('nome')
    novo_Patroconador.atividade = request.POST.get('atividade')
    novo_Patroconador.cnpj = request.POST.get('cnpj')
    novo_Patroconador.save

    #exibindo os usuarios:
    cadastros = {
        'cadastros': Patrocinador.objects.all()
    }

    #retornando os dados para a página
    return render(request, 'cadastro/patrocinadores.html', cadastros)