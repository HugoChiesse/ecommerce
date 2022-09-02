from ast import mod
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User


class Pedido(models.Model):
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Usuário')
    total = models.FloatField(default=0, verbose_name='Total')
    qtd_total = models.PositiveBigIntegerField(verbose_name='Qtd Total')
    status = models.CharField(default='C', max_length=1, choices=(
        ('A', 'Aprovado'),
        ('C', 'Criado'),
        ('R', 'Reprovado'),
        ('P', 'Pendente'),
        ('E', 'Enviado'),
        ('F', 'Finalizado'),
    ), verbose_name='Status')
    
    
    def __str__(self) -> str:
        return f'Pedido Nº {self.pk}'


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, verbose_name='Pedido')
    produto = models.CharField(max_length=255, verbose_name='Produto')
    produto_id = models.PositiveIntegerField(verbose_name='ID do Produto')
    variacao = models.CharField(max_length=255, verbose_name='Variação')
    variacao_id = models.PositiveIntegerField(verbose_name='ID da Variação')
    preco = models.FloatField(verbose_name='Preço')
    preco_promocional = models.FloatField(default=0, verbose_name='Preço Promocional')
    quantidade = models.FloatField(verbose_name='Quantidade')
    imagem = models.CharField(max_length=255)
    
    
    def __str__(self) -> str:
        return f'Item do {self.pedido}'
    
    
    class Meta:
        verbose_name = 'Item do Pedido'
        verbose_name_plural = 'Itens do Pedido'