from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import Venda
from .models import ItemPedido
from .forms import ItemPedidoForm, ItemDoPedidoModelForm
from django.utils.formats import sanitize_separators

class DashboardView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('vendas.ver_dashboard'):
            return HttpResponse('Acesso Negado, voce precisa de permissao')

        return super(DashboardView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        data = {}
        data['media'] = Venda.objects.media()
        data['media_desc'] = Venda.objects.media_desc()
        data['soma'] = Venda.objects.soma()
        data['min'] = Venda.objects.min()
        data['max'] = Venda.objects.max()
        data['n_count'] = Venda.objects.n_count()
        data['n_count_nfe'] = Venda.objects.n_count_nfe()


        return render(request, 'vendas/dashboard.html', data)

class NovoPedido(View):
    def get(self, request):
        return render(request, 'vendas/novo-pedido.html')

    def post(self, request):
        data = {}
        data['form_item'] = ItemPedidoForm()
        data['numero'] = int(request.POST['numero'])
        data['desconto'] = sanitize_separators(request.POST['desconto'])
        data['venda_id'] = request.POST['venda_id']

        if data['venda_id']:
            venda = Venda.objects.get(id=data['venda_id'])
            venda.desconto = data['desconto']
            venda.numero = data['numero']
            venda.save()
        else:
            venda = Venda.objects.create(numero=data['numero'], desconto=data['desconto'])

        itens = venda.itempedido_set.all()
        data['venda'] = venda
        data['itens'] = itens
        return render( request, 'vendas/novo-pedido.html', data)



class NovoItemPedido(View):
    def get(self, request, pk):
        pass

    def post(self, request, venda):
        data = {}
        item = ItemPedido.objects.filter(produto_id=request.POST['produto_id'], venda_id=venda)
        if item:
            data['mensagem'] = 'Item já incluido na lista de venda'
            item = item[0]
        else:
            item = ItemPedido.objects.create(
                produto_id=request.POST['produto_id'],
                qtd=request.POST['qtd'],
                desconto=request.POST['desconto'], venda_id=venda
            )
            
        data['item'] = item
        data['form_item'] = ItemPedidoForm()
        data['numero'] = item.venda.numero
        data['desconto'] = item.venda.desconto
        data['venda'] = item.venda
        data['itens'] = item.venda.itempedido_set.all()

        return render(request, 'vendas/novo-pedido.html', data)


class ListaVendas(View):
    def get(self, request):
        vendas = Venda.objects.all()
        return render(request, 'vendas/listavendas.html', {'vendas': vendas })


class EditPedido(View):
    def get(self, request, venda):
        data = {}
        venda = Venda.objects.get(id=venda)
        data['form_item'] = ItemPedidoForm()
        data['numero'] = venda.numero
        data['desconto'] = float(venda.desconto)
        data['venda'] = venda
        data['itens'] = venda.itempedido_set.all()
        return render(request, 'vendas/novo-pedido.html', data)


class DeletePedido(View):
    def get(self, request, venda):
        venda = Venda.objects.get(id=venda)
        return render(request, 'vendas/delete-pedido-confirm.html', {'venda': venda})

    def post(self, request, venda):
        venda = Venda.objects.get(id=venda)
        venda.delete()
        return redirect('vendas:listavendas')


class DeleteItemPedido(View):
    def get(self, request, item):
        item_pedido = ItemPedido.objects.get(id=item)
        return render(
            request, 'vendas/delete-itempedido-confirm.html', {'item_pedido': item_pedido })

    def post(self, request, item):
        item_pedido = ItemPedido.objects.get(id=item)
        venda_id = item_pedido.venda.id
        item_pedido.delete()
        request.method = 'GET'
        return redirect('vendas:edit_pedido', venda=venda_id)


class EditItemPedido(View):
    def get(self, request, item):
        item_pedido = ItemPedido.objects.get(id=item)
        form = ItemDoPedidoModelForm(instance=item_pedido)
        return render(
            request, 'vendas/edit-itempedido.html', {'item_pedido': item_pedido, 'form': form })

    def post(self, request, item):
        item_pedido = ItemPedido.objects.get(id=item)
        item_pedido.qtd = request.POST['qtd']
        item_pedido.desconto = request.POST['desconto']

        item_pedido.save()
        venda_id = item_pedido.venda.id
        return redirect('vendas:edit_pedido', venda=venda_id)


dash = DashboardView.as_view()
novo_pedido = NovoPedido.as_view()
novoItemPedido = NovoItemPedido.as_view()
listavendas = ListaVendas.as_view()
edit_Pedido = EditPedido.as_view()
delete_Pedido = DeletePedido.as_view()
delete_ItemPedido = DeleteItemPedido.as_view()
edit_ItemPedido = EditItemPedido.as_view()


























'''
'''
