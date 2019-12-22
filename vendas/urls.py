from django.urls import path
from .views import (
             dash, novo_pedido, novoItemPedido, delete_ItemPedido,
             listavendas, edit_Pedido, delete_Pedido, edit_ItemPedido )

app_name = "vendas"
urlpatterns = [
    path('', listavendas, name="listavendas"),
    path('novo-pedido/', novo_pedido, name="novo_pedido"),
    path('novo-item-pedido/<int:venda>/', novoItemPedido, name="novo_item_pedido"),
    path('edit-pedido/<int:venda>/', edit_Pedido, name="edit_pedido"),
    path('delete-item-pedido/<int:item>/', delete_ItemPedido, name="delete_item_pedido"),
    path('edit-item-pedido/<int:item>/', edit_ItemPedido, name="edit_item_pedido"),
    path('delete-pedido/<int:venda>/', delete_Pedido, name="delete_pedido"),
    path('dashboard/', dash, name="dash"),
]
