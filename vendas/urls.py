from django.urls import path
from .views import dash

app_name = "vendas"
urlpatterns = [
    path('dashboard/', dash, name="dash"),
]
