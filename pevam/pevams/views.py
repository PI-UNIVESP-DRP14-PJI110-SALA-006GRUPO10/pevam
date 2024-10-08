from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import Cadastro, ContatoEmergencia, Lotacao
from .forms import CadastroForm, ContatoEmergenciaForm, EventoCritico, LotacaoForm

def home(request):
    return render(request, 'sections/home.html')

def cadastro(request):
    cadastros = Cadastro.objects.all()  # Obtenha todos os cadastros

    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o formulário diretamente no banco de dados
            return JsonResponse({'status': 'success', 'message': 'Pessoa cadastrada com sucesso!'})
        else:
            # Se o formulário não for válido, retorna os erros
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    else:
        form = CadastroForm()  # Exibe o formulário vazio para uma requisição GET

    return render(request, 'sections/cadastro.html', {'form': form, 'cadastros': cadastros})  # Adicione 'cadastros' ao contexto

def contato_emergencia(request):
    if request.method == 'POST':
        form = ContatoEmergenciaForm(request.POST)
        if form.is_valid():
            # Salva o contato de emergência no banco de dados
            contato_emergencia = form.save()
            return JsonResponse({'status': 'success', 'message': 'Contato de emergência cadastrado com sucesso!'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    else:
        form = ContatoEmergenciaForm()

    return render(request, 'sections/contato_emergencia.html', {'form': form})

class CadastrarEventoCritico(View):
    def get(self, request):
        return render(request, 'sections/cadastrar_evento_critico.html')

    def post(self, request):
        tipo_evento = request.POST.get('tipo_evento')

        if tipo_evento:
            evento_critico = EventoCritico(tipo_evento=tipo_evento)
            evento_critico.save()
            return JsonResponse({'status': 'success', 'message': 'Evento crítico cadastrado com sucesso!'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Tipo de evento não selecionado.'})
        

def cadastrar_lotacao(request):
    if request.method == 'POST':
        form = LotacaoForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o formulário no banco de dados
            return JsonResponse({'status': 'success', 'message': 'Lotação cadastrada com sucesso!'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    else:
        form = LotacaoForm()

    return render(request, 'sections/cadastrar_lotacao.html', {'form': form})