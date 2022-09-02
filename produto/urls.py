from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    path('', views.ListaProdutos.as_view(), name='lista'),
    path('<slug>', views.DetalheProduto.as_view(), name='detalhe'),
    path('adicionar_ao_carrinho/', views.AdicionarAoCarrinho.as_view(),
         name='adicionar_ao_carrinho'),
    path('remover_ao_carrinho/', views.RemoverDoCarrinho.as_view(),
         name='remover_ao_carrinho'),
    path('carrinho/', views.Carrinho.as_view(), name='carrinho'),
    path('resumo_da_compra/', views.ResumoDaCompra.as_view(), name='resumo_da_compra'),
    path('busca/', views.Busca.as_view(), name='busca'),
]
