from django import forms
from .models import ItemPedido

class ItemPedidoForm(forms.Form):
    produto_id = forms.CharField(label='ID do Produto', max_length=100)
    qtd = forms.IntegerField(label='Quantidade')
    desconto = forms.DecimalField(label='Desconto', max_digits=4, decimal_places=2)


class ItemDoPedidoModelForm(forms.ModelForm):
    class Meta:
        model = ItemPedido
        fields = ['qtd', 'desconto',]
