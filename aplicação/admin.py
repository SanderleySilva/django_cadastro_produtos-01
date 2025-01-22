from django.contrib import admin
from .models import Produtos

@admin.register(Produtos)
class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'preco', 'quantidade')  # Campos exibidos no admin
    search_fields = ('nome', 'categoria')  # Campos pesquisáveis
