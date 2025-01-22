from django.shortcuts import render, redirect
from .models import Produtos
from django.contrib import messages
# Create your views here.


def index(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        categoria = request.POST.get('categoria')
        preco = request.POST.get('preco')
        quantidade = request.POST.get('quantidade')

        if nome and categoria and preco and quantidade:
        # Salva no banco de dados
            Produtos.objects.create(
                nome=nome,
                categoria=categoria,
                preco=preco,
                quantidade=quantidade
            )
            messages.success(request, f'O produto {nome} foi cadastrado com sucesso!')
        else:
            messages.error(request, 'Preencha todos os campos para cadastrar o produto.')
            
        return redirect('index')  # Redireciona após o salvamento
        

    return render(request, 'index/index.html')



def produtos(request):
    produtos = Produtos.objects.all()
    return render(request, 'produtos/produtos.html', {'produtos': produtos})