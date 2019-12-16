from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Venda

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


dash = DashboardView.as_view()
