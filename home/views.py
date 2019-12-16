from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import logout
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views import View

def home(request):
    return render(request, 'home/home.html')


def politica_de_privacidade(request):
        return render(request, 'home/politica-de-privacidade.html')


def my_logout(request):
    logout(request)
    return redirect('home')

class HomePageView(TemplateView):
    template_name = 'home3.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['minha_variavel'] = 'Ola seja bemvindo ao CURSO DJANGO'

        return context

class MyView(View):

    def get(self, request, *args, **kwargs):
        response = render_to_response('home/home3.html')
        response.set_cookie('color', 'red', max_age=1000)
        mycookie = request.COOKIES.get('color')
        print(mycookie)
        return response

    def post(self, request, *args, **kwargs):
        return HttpResponse('My Post')











        '''
        fim
        '''
