from django.urls import path
from .views import home, my_logout, HomePageView, MyView, politica_de_privacidade
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', home, name="home"),
    path('politica-de-privacidade', politica_de_privacidade, name="politica_de_privacidade"),
    path('logout/', my_logout, name="logout"),
    path('home2/', TemplateView.as_view(template_name='home2.html'), name="home2"),
    path('home3/', HomePageView.as_view(template_name='home3.html'), name="home3"),
    path('view/', MyView.as_view()),
]
