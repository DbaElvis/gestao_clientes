from django.contrib import admin
from clientes.actions import nfe_emitida, nfe_nao_emitida
from .models import Venda, ItemPedido

#@admin.register(ItemPedido)
class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    readonly_fields = ('valor',)
    #raw_id_fields = ('pessoa',)
    autocomplete_fields = ('pessoa',)
    list_filter = ('pessoa__doc', 'desconto')
    list_display = ('id', 'pessoa', 'nfe_emitida')
    search_fields = ('id', 'pessoa__first_name', 'pessoa__doc__num_doc')
    actions = [nfe_emitida, nfe_nao_emitida]
    inlines = [ItemPedidoInline]
    #filter_horizontal = ['produtos',]

    def get_total(self, obj):
        return obj.get_total()

    get_total.short_description= 'Total vendas'


@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ('venda', 'produto', 'qtd')
